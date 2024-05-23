import gspread
from google.oauth2.service_account import Credentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv
import os; import sqlite3

load_dotenv()

### Global variable ###
global_path         = os.path.dirname(__file__)
db_path             = os.path.join(global_path, "db") #db is the name of the folder you wish to enter
credentials_path    = os.path.join(global_path,"credentials")
service_acc_cred    = os.path.join(credentials_path,"credentials.json")


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(service_acc_cred, scopes = scope)
client = gspread.authorize(credentials)

worksheet = client.open('Clinic Registration (Applications)').worksheet('Applicants')  # Replace with your sheet's name
responses = worksheet.get_all_records()

root = tk.Tk()
root.title("Applicants")

#   Database config
def create_tables():
    conn = sqlite3.connect(os.path.join(db_path, "database.db")) 
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS CLINICS 
        (
            CLINIC_NAME TEXT PRIMARY KEY UNIQUE NOT NULL,
            CLINIC_ADDRESS TEXT NOT NULL,
            EMAIL TEXT,
            PASSWORD TEXT,
            ACTIVATION_CODE TEXT UNIQUE NOT NULL,
            FOREIGN KEY (ACTIVATION_CODE) REFERENCES KEY_LIST(ACTIVATION_CODE)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS KEY_LIST 
        (
            ACTIVATION_CODE TEXT PRIMARY KEY UNIQUE NOT NULL,
            EMAIL TEXT NOT NULL,
            ACTIVATION_STATUS TEXT DEFAULT 'Not Activated',
            FOREIGN KEY (EMAIL) REFERENCES CLINICS(EMAIL)
            
        )''')

    conn.commit()
    conn.close()

create_tables()

# Treeview widget for sheet data
tree = ttk.Treeview(root, columns=("Timestamp","Clinic Name","Address","Email"), show = "headings")
tree.heading("#1", text = "Timestamp")
tree.heading("#2", text = "Clinic Name")
tree.heading("#3", text = "Address")
tree.heading("#4", text = "Email")

tree.column("#1", width = 200, anchor = "center")
tree.column("#2", width = 200, anchor = "center")
tree.column("#3", width = 200, anchor = "center")
tree.column("#4", width = 200, anchor = "center")

# Get new responses
new_responses = worksheet.get_all_records(empty2zero=False, head=1)  # Adjust if needed

for i, response in enumerate(responses):
    tree.insert("", "end", text=f"Response {i+1}", values=(response["Timestamp"], response["Clinic Name"], response["Address"], response["Email Address"]))

# Pack treeview
tree.pack(fill = "both", expand = True)
    #Old logic# Label(root, text=f"Response {i+1}: {response}").pack()
# # Apply your approval logic here (Gemini's approach)
# for response in new_responses:
#     if evaluate_response(response):  # Replace with your evaluation function
#         worksheet.update_cell(response['row'], 'Status Column Number', 'Approved')  
#     else:
#         worksheet.update_cell(response['row'], 'Status Column Number', 'Rejected')  

def on_select(event):
     selected_item = tree.focus()
     if selected_item:
          values = tree.item(selected_item, "values")   # Fetch values from selected row
          print(f"Selected Data: {values}")

tree.bind("<<TreeviewSelect>>",on_select)

# Pagination
ITEMS_PER_PAGE = 20
current_page = 0
total_pages = (len(responses) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE   # Calculate total pages

def populate_tree():
    start_index = current_page * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(responses))

    tree.delete(*tree.get_children())  # Clear previous items

    for i, response in enumerate(responses[start_index:end_index]):
        tree.insert("", "end", text=f"Response {i + start_index + 1}", values=(response["Timestamp"], response["Clinic Name"], response["Address"], response["Email Address"]))

    page_label.config(text=f"Page {current_page + 1} of {total_pages}")

def next_page():
    global current_page
    if current_page < total_pages - 1:
        current_page += 1
        populate_tree()

def prev_page():
    global current_page
    if current_page > 0:
        current_page -= 1
        populate_tree()

# Pagination's UI
bottom_frame = tk.Frame(root)
bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

next_button = tk.Button(bottom_frame, text="Next", command=next_page)
next_button.pack(side=tk.RIGHT)

page_label = tk.Label(bottom_frame, text=f"Page {current_page + 1} of {total_pages}")
page_label.pack(side=tk.RIGHT, padx=10)

prev_button = tk.Button(bottom_frame, text="Previous", command=prev_page)
prev_button.pack(side=tk.RIGHT)

populate_tree()


# Application logics
def approve_registration():
    
#   Generate activation code
    activation_code = generate_activation_code()

    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, "values")
        timestamp, clinic_name, clinic_address, email = values[0], values[1], values[2], values[3]



        #   Update database
        try:
            conn = sqlite3.connect(os.path.join(db_path, "database.db"))
            cursor = conn.cursor()

            cursor.execute("INSERT INTO KEY_LIST (ACTIVATION_CODE, EMAIL, ACTIVATION_STATUS) VALUES (?,?,'Not Activated')", (activation_code,email))
            cursor.execute("INSERT INTO CLINICS (CLINIC_NAME, CLINIC_ADDRESS, ACTIVATION_CODE) VALUES (?,?,?)", 
                           (clinic_name, clinic_address, activation_code))

            conn.commit()
            #conn.close()
        except sqlite3.Error as e:
            print("Database error:", e)
            return  # Exit early on error
        
        finally:
            if conn:
                conn.close
        
        try:
            # 1. Find the row in the worksheet based on email and timestamp
            cell = worksheet.find(query=email)

            for cell in worksheet.findall(query=email):
                row_values = worksheet.row_values(cell.row)
                if row_values[0] == timestamp:  # Check if timestamp matches
                    row_number = cell.row
                    break  # Found the correct row
            else:
                raise gspread.CellNotFound  # If no match is found

            # 2. Update the Review Status cell
            status_column_letter = 'E'  # Adjust if needed
            worksheet.update_cell(row_number, status_column_letter, "Approved")

        except gspread.CellNotFound:
            print(f"Email and timestamp combination not found in the worksheet.")
        except Exception as e:
            print("Error updating Google Sheet:", e)

        #   Send approval email (include activation code)
        ##send_approved_email(email, activation_code)


def reject_registration():
     send_rejected_email()


# Activation code generator
def generate_activation_code():
     import random; import string
     return ''.join(random.choices(string.ascii_letters + string.digits, k = 6))


# Email Functions

def send_approved_email(clinic_name, clinic_address, email, activation_code):

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Use the appropriate port
        sender_email = os.environ.get('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')        # Email address
        sender_password = os.environ.get('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')  # Email password

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)


            body =  f"""<html>
                        <body>
                            <p>This is a confirmation email to acknowledge that your application has been approved. Please find your activation code attached below</p>
                            <p>Registration Summary: </p>
                            <p>Clinic Name: {clinic_name}</p>
                            <p>Clinic Address: {clinic_address}</p>
                            <p>Activation Code: {activation_code}</p>
                            <p></p>
                            <p></p>
                            <p>Head on over to our registration page to create an account for your clinic.</p>
                            <p>The activation code is only valid for a single use. Please do not share it to anybody else</p>
                            <p></p>
                            <p>Regards,</p>
                            <p>Administration of Call a Doctor</p>
                        </body>
                        </html>"""
                
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = "Application Status"
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            text = msg.as_string()
            server.sendmail(sender_email, email, text)

            # Close the connection
            server.quit()

            print("Transaction successful! Email has been sent to user's email address.")
        except Exception as e:
            print("Email error:", e)
            print("Email sending failed. Please check your email settings.")

def send_rejected_email(email):

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Use the appropriate port
        sender_email = os.environ.get('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')        # Email address
        sender_password = os.environ.get('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')  # Email password

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)


            body =  f"""<html>
                        <body>
                            <p>This is a confirmation email to acknowledge that your application has been rejected:</p>
                            <p>Please ensure that you have submitted all the proper documents before trying again</p>
                            <p>Regards,</p>
                            <p>Admin of Call a Doctor</p>
                        </body>
                        </html>"""
                
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = email
            msg['Subject'] = "Application Status"
            msg.attach(MIMEText(body, 'html'))

            # Send the email
            text = msg.as_string()
            server.sendmail(sender_email, email, text)

            # Close the connection
            server.quit()

            print("Transaction successful! Email has been sent to user's email address.")
        except Exception as e:
            print("Email error:", e)
            print("Email sending failed. Please check your email settings.")

def b1():
     selected_item = tree.focus()
     if selected_item:
          values = tree.item(selected_item, "values")
          clinic_name, clinic_address, email = values[1], values[2], values[3]

          # Generate activation code
          activation_code = generate_activation_code()
     #print("Approved")
     print(f"Name: {clinic_name}\n Address: {clinic_address}\n Email: {email}\n Code: {activation_code}")

     #approve_registration(clinic_name, clinic_address, email, activation_code)

def b2():
     print("Rejected")

Button(root, text ="Approve", command = approve_registration).pack()
Button(root, text ="Reject", command = b2).pack()#command = reject_registration).pack()

root.mainloop()