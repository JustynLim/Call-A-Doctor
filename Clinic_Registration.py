import gspread
from google.oauth2.service_account import Credentials
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import *
import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import ttk
from dotenv import load_dotenv
import os; import sqlite3
from datetime import datetime

load_dotenv()

### Global variable ###
global_path         = os.path.dirname(__file__)
db_path             = os.path.join(global_path, "db") #db is the name of the folder you wish to enter
credentials_path    = os.path.join(global_path,"credentials")
service_acc_cred    = os.path.join(credentials_path,"credentials.json")


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(service_acc_cred, scopes = scope)
client = gspread.authorize(credentials)

worksheet = client.open('Clinic Registration (Applications)').worksheet('Applicants')  # Replace with desired sheet name
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
            PASSWORD_HASH TEXT,
            RECORD_ID TEXT,
            ACTIVATION_CODE TEXT UNIQUE NOT NULL,
            FOREIGN KEY (ACTIVATION_CODE) REFERENCES KEY_LIST(ACTIVATION_CODE)
        )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS KEY_LIST 
        (
            ACTIVATION_CODE TEXT PRIMARY KEY UNIQUE NOT NULL,
            ASSIGNED_TO_EMAIL TEXT NOT NULL,
            ACTIVATION_STATUS TEXT DEFAULT 'Not Activated'
        )''')
    # cursor.execute('''CREATE TABLE IF NOT EXISTS KEY_LIST 
    #     (
    #         ACTIVATION_CODE TEXT PRIMARY KEY UNIQUE NOT NULL,
    #         EMAIL TEXT NOT NULL,
    #         ACTIVATION_STATUS TEXT DEFAULT 'Not Activated',
    #         FOREIGN KEY (EMAIL) REFERENCES CLINICS(EMAIL)
            
    #     )''')

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

def reload_responses():
    global responses
    responses = worksheet.get_all_records()

def populate_tree():
    global responses; global total_pages; global current_page
    reload_responses()

    filtered_responses = [response for response in responses if response.get("Approval Status") not in ["Approved", "Rejected"]]

    # Recalculate pagination
    total_pages = (len(filtered_responses) + ITEMS_PER_PAGE - 1) // ITEMS_PER_PAGE
    current_page = 0  # Reset to first page after filtering

    tree.delete(*tree.get_children())  # Clear previous items
    start_index = current_page * ITEMS_PER_PAGE
    end_index = min(start_index + ITEMS_PER_PAGE, len(filtered_responses))


    for i, response in enumerate(filtered_responses[start_index:end_index]):
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

def auto_refresh_list():
    populate_tree()
    root.after(10000, auto_refresh_list)    # Refreses list every 10 secs

root.after(10000, auto_refresh_list)    # Calls auto refresh function every 10 secs


# Application logics
def approve_registration():
    
#   Generate activation code
    activation_code = generate_activation_code()

    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, "values")
        timestamp, clinic_name, clinic_address, email = values[0], values[1], values[2], values[3]

        print(f"Raw timestamp from Treeview: {timestamp}")
        try:
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        
        except ValueError:
            print("Invalid timestamp format")
            return

        #   Update database
        try:
            conn = sqlite3.connect(os.path.join(db_path, "database.db"))
            cursor = conn.cursor()

            cursor.execute("INSERT INTO KEY_LIST (ACTIVATION_CODE, ASSIGNED_TO_EMAIL, ACTIVATION_STATUS) VALUES (?,?,'Not Activated')", (activation_code,email))
            cursor.execute("INSERT INTO CLINICS (CLINIC_NAME, CLINIC_ADDRESS, ACTIVATION_CODE) VALUES (?,?,?)", 
                           (clinic_name, clinic_address, activation_code))

            conn.commit()

        except sqlite3.IntegrityError as e:
            if 'UNIQUE constraint failed: CLINICS.CLINIC_NAME' in str(e):
                messagebox.showerror("Error","Clinic name already exists in the database")
                
                if conn:
                    conn.close()
                    return
                
        except sqlite3.Error as e:
            print("Database error:", e)
            return  # Exit early on error
        
        finally:
            if conn:
                conn.close
        
        try:
            # 1. Find the row in the worksheet based on email and timestamp
            cell = worksheet.find(email)
            row_number = None

            for cell in worksheet.findall(email):
                row_values = worksheet.row_values(cell.row)
                sheet_timestamp = datetime.strptime(row_values[0], "%m/%d/%Y %H:%M:%S")
                
                if sheet_timestamp == timestamp:  # Check if timestamp matches
                    row_number = cell.row
                    break  # Found the correct row
            
            else:
                raise ValueError(f"Email and timestamp combination not found in the worksheet.") # If no match is found

            #   Update the Approval Status cell
            status_column_index = 5  # Adjust to match target column
            worksheet.update_cell(row_number, status_column_index, "Approved")

        except ValueError as e:
            print(str(e))
        except Exception as e:
            print("Error updating Google Sheet:", e)
        finally:
            tree.delete(selected_item) # Remove approved applicant from view
            populate_tree() # Refreshes list

        #   Send approval email (include activation code), disable this for testing
        send_approved_email(clinic_name, clinic_address, email, activation_code)


def reject_registration():
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, "values")
        timestamp, clinic_name, clinic_address, email = values[0], values[1], values[2], values[3]

        try:
            timestamp = datetime.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        except ValueError:
            print("Invalid timestamp format")
            return

        try:
            #   Finds the row in the worksheet based on email and timestamp
            cell = worksheet.find(email)
            row_number = None

            for cell in worksheet.findall(email):
                row_values = worksheet.row_values(cell.row)
                sheet_timestamp = datetime.strptime(row_values[0], "%m/%d/%Y %H:%M:%S")
                if sheet_timestamp == timestamp:
                    row_number = cell.row
                    break
            else:
                raise ValueError(f"Email and timestamp combination not found in the worksheet.")

            #   Updates the Approval Status cell
            status_column_index = 5  # Adjust to match target column
            worksheet.update_cell(row_number, status_column_index, "Rejected")

        except ValueError as e:
            print(str(e))

        except Exception as e:
            print("Error updating Google Sheet:", e)
        
        finally:
            # Remove the rejected item from the Treeview
            tree.delete(selected_item)

            # Refresh to show changes and maintain filtering
            populate_tree()

        # Send rejection email
        send_rejected_email(clinic_name, clinic_address, email)



# Activation code generator
def generate_activation_code():
     import random; import string
     return ''.join(random.choices(string.ascii_letters + string.digits, k = 6))


# Email Functions

def send_approved_email(clinic_name, clinic_address, email, activation_code):

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Gmail's appropriate port
        sender_email = os.environ.get('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')      
        sender_password = os.environ.get('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS') 

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

            print(f"Approved email has been sent to user's email address:{email}")
        except Exception as e:
            print("Email error:", e)
            print("Email sending failed. Please check your email settings.")

def send_rejected_email(clinic_name, clinic_address, email):

        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Gmail's appropriate port
        sender_email = os.environ.get('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')       
        sender_password = os.environ.get('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')  

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)


            body =  f"""<html>
                        <body>
                            <p>This email is to inform you that your application has been rejected. Here are the details that you have provided us:</p>
                            <p>Registration Summary: </p>
                            <p>Clinic Name: {clinic_name}</p>
                            <p>Clinic Address: {clinic_address}</p>
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

            print(f"Rejected email has been sent to user's email address:{email}")
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
Button(root, text ="Reject", command = reject_registration).pack()

root.mainloop()