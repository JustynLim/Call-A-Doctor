from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from tkinter import Label, Toplevel
from PIL import Image, ImageTk
from plyer import notification
from tkcalendar import Calendar
import datetime; import os; import sqlite3; import hashlib; import uuid
#from Clinic_Registration import *


### Global variable ###
font_1              = 'Microsoft YaHei UI Light'
global_path         = os.path.dirname(__file__)
resources_path      = os.path.join(global_path, "resources")
db_path             = os.path.join(global_path, "db")
form_type           = 1



### Button config ###
theme_button_mode               = True
password_button1_mode           = True             # True = show password, False = hide password
password_button2_mode           = True
confirm_password_button_mode    = True

### Form config ###
email_input1            = '' 
email_input2            = ''
password_input1         = ''
password_input2         = ''
confirm_password_input  = ''
activation_code_input   = ''

# Global variable to store logged-in email
logged_in_email = ''

# Connect to db. Create entity
path_db_file = os.path.join(db_path, "database.db")
connection = sqlite3.connect(path_db_file)                  # sqlite3.connect(global_path+DB_NAME)                                                                 #   Insert global path
cursor_master = connection.cursor()
cursor_master.execute
('''CREATE TABLE IF NOT EXISTS CLINICS 
    (
        CLINIC_NAME TEXT PRIMARY KEY UNIQUE NOT NULL,
        CLINIC_ADDRESS TEXT NOT NULL,
        EMAIL TEXT,
        PASSWORD_HASH TEXT,
        RECORD_ID TEXT,
        ACTIVATION_CODE TEXT UNIQUE NOT NULL,
        FOREIGN KEY (ACTIVATION_CODE) REFERENCES KEY_LIST(ACTIVATION_CODE)
    )
''')

cursor_master.execute
('''CREATE TABLE IF NOT EXISTS KEY_LIST 
        (
            ACTIVATION_CODE TEXT PRIMARY KEY UNIQUE NOT NULL,
            ASSIGNED_TO_EMAIL TEXT NOT NULL,
            ACTIVATION_STATUS TEXT DEFAULT 'Not Activated'
        )
''')

cursor_master.close(); connection.close()



def login():
    global password_button1_mode
    password_button1_mode = True
    
    global form_type
    form_type = 0

# Create a Tkinter window
    login_root = Tk()

#################---(Removing window title)---##################
    
    login_root.title("")
    login_root.attributes('-topmost', False),('-alpha', 0.8),('-toolwindow', True),('-style', 'dialog')

################################################################

    # Set the window size
    win_width = 925; win_height = 500
    login_root.geometry(f'{win_width}x{win_height}+300+200')
    login_root.configure(bg="#fff")
    login_root.resizable(FALSE,FALSE)

    path_show_password_button = os.path.join(resources_path, "show_password.png")
    show_password_button = PhotoImage(file=path_show_password_button)                                             ## Locate image ##

    path_hide_password_button = os.path.join(resources_path, "hide_password.png")
    hide_password_button = PhotoImage(file=path_hide_password_button)

    def on_enter(event):
        signin()
        
    def signin():
        global email_input1; global password_input1; global logged_in_email
        on_leave_email(None); on_leave_password(None)
        email = email_input1; password = password_input1

#   Login auth (version 1)
        if email is None or password is None:
            display_status(0)

            #print("Line 108")
        else:
            db_conn = sqlite3.connect(path_db_file)
            cursor_user = db_conn.cursor()
            cursor_user.execute("SELECT EMAIL,PASSWORD_HASH,RECORD_ID FROM CLINICS WHERE email=?", (email,))
            row = cursor_user.fetchone()
        
        if row is not None:
            salt_db = row[2]
            password_hash_db = row[1]
            password_hash = encrypt_pw(salt_db,password)
            if password_hash_db != password_hash:
                display_status(0)
                #print("Line 121")

            else:
                global form_type
                display_status(1)
                logged_in_email = email
                login_root.after(1000,lambda:login_root.destroy())
                form_type = 3

        else:
            display_status(0)
        #print("Line 132")
        pw.focus_set()
        if pw.get() == " Password":
            pw.delete(0,'end')
            password_input1 = ''

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            login_status.config(text="Invalid email/password",fg='red',bg='white')
            
        else:
            login_status.config(text="Login successful", fg='green', bg='white')


#####################################################################
    #   Load the vector file (.eps) using PIL
    path_login_logo = os.path.join(resources_path, "login.eps")
    image = Image.open (path_login_logo)                       

    #   Resize
    new_width, new_height = 398,332
    image = image.resize((new_width,new_height))

    #   Convert .eps file to Tkinter-compatible format                                 
    tk_image = ImageTk.PhotoImage(image=image)

    #   Create label for image
    Label(login_root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)


    #Login box frame (PV)
    frame= Frame(login_root,width=350, height=350,bg='white')                                         #Don't '.place' here, shifts frame to the other side
    frame.place(x=480,y=90)                                                                           #edited 70 -> 90

    heading=Label(frame,text='Sign In',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
    heading.place(x=100,y=5)

### This part handles changing icon and sets global value ###
    def toggle_password():
        global password_button1_mode

        #print("Toggle password triggered (Line: 170)")

        if password_button1_mode:
            password_toggle_mode.config(image = show_password_button)
            password_button1_mode = False

        else:
            password_toggle_mode.config(image = hide_password_button)
            password_button1_mode = True

        password_mode()

##########- Shows/Hide password -##########
    def password_mode():
        password = pw.get()
        #print("password_mode() ->Leave password     (Line: 185)")
        #print(password)
        if password != '' and password != ' Password':
            global password_input1
            password_input1 = password
        
        else:
            password_input1 = ''         

        if password_input1 == '':
            pw.config(show = '')
            pw.delete(0,'end')
            pw.insert(0,' Password')
        
        elif password_button1_mode:
            pw.config(show = '')
            
        else:
            pw.config(show = '*')            
###########################################
    def registrationX():
        global form_type
        form_type = 2
        login_root.after(1000,lambda:login_root.destroy())        
###########################################
########################################################################################
    def on_enter_email(e):
        if  email_input1 == '':
            user.delete(0,'end')

    def on_leave_email(e):
        name = user.get()
        #print("On leave user")
        if name == '':
            global email_input1
            user.insert(0,' Email')
            email_input1 = ''

        elif user.get() == ' Email':
            email_input1 = ''

        else:
            email_input1 = user.get()      

    user = Entry(frame,width = 25,fg = 'black',border = 0,bg = "white",font = (font_1,11)) # Cannot use: .place(x=30,y=80),causes error
    user.place(x = 30,y = 80)
    user.insert(0,' Email')
    user.bind('<FocusIn>', on_enter_email) and user.bind('<FocusOut>', on_leave_email)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107) #25,107
########################################################################################
    def on_enter_password(e):
       if  password_input1 == ''or pw.get() == ' Password':
        pw.delete(0,'end')
        
        if password_button1_mode:                
            pw.config(show = '')
        
        else:
            pw.config(show = '*')        

    def on_leave_password(e):
        password_mode()
########################################################################################
##############################################################################
    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11)) # Cannot use: .place(x=30,y=150)
    pw.place(x=30,y=150)
    pw.bind('<FocusIn>', on_enter_password) and pw.bind('<FocusOut>', on_leave_password)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
##############################################################################

    sign_in_button=Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0,command=signin ).place(x=35,y=240)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)
    
    sign_up = Button(frame,width= 6,text='Sign up', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command = registrationX).place(x=225,y=300)

    password_toggle_mode = Button(login_root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_password)
    password_toggle_mode.place(x=770,y=238)

    login_status = Label(frame,text="",fg='white',bg='white')     
    login_status.place(x=75,y=330)

    login_root.bind('<Return>', on_enter)

    toggle_password()                           # Triggers function once, turns to false state

    # run the window
    login_root.mainloop()


def registration():
    global password_button2_mode; global confirm_password_button_mode
    password_button2_mode = True; confirm_password_button_mode = True
    global form_type
    form_type = 0

    registration_root = Tk()
    registration_root.title("")
    registration_root.attributes('-topmost', False),('-alpha', 0.8),('-toolwindow', True),('-style', 'dialog')

    # Set the window size
    win_width = 925; win_height = 500
    registration_root.geometry(f'{win_width}x{win_height}+300+200')
    registration_root.configure(bg="#fff")
    registration_root.resizable(FALSE,FALSE)

    path_show_password_button = os.path.join(resources_path, "show_password.png")
    show_password_button = PhotoImage(file=path_show_password_button)                                             ## Locate image ##

    path_hide_password_button = os.path.join(resources_path, "hide_password.png")
    hide_password_button = PhotoImage(file=path_hide_password_button)

    def on_enter(event):
        signup()

    def signup():

        global email_input2; global password_input2; global confirm_password_input, activation_code_input

        on_leave_email(None); on_leave_password(None); on_leave_confirm_password(None); on_leave_activation_code(None)

        email=email_input2; password=password_input2; verify_password=confirm_password_input; activation_code = activation_code_input
        #print (email_input2,password_input2,confirm_password_input)
        
        isError = False
        if email is None or email == '':
            display_status(0)
            isError = True
        

        elif password is None or verify_password is None or password == '' or verify_password == '':
            display_status(1)
            isError = True 
            
        elif password != verify_password:
            display_status(2)
            isError = True

        elif activation_code is None or activation_code == '':
            display_status(4)
            isError= True
        
        if isError:
            #print("isError")
            confirm_pw.focus_set()
            if confirm_pw.get() == " Confirm Password":
                confirm_pw.delete(0,'end')
                confirm_password_input = ''
            return

        conn = sqlite3.connect(path_db_file)      
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT EMAIL FROM CLINICS WHERE EMAIL=?", (email,))
            email_exists = cursor.fetchone()

            if email_exists is not None:
                display_status(3)
                confirm_pw.focus_set()
                if confirm_pw.get() == " Confirm Password":
                    confirm_pw.delete(0, 'end')
                    confirm_password_input = ''
                cursor.close()
                conn.close()
                return 
            
            cursor.execute("SELECT ACTIVATION_STATUS FROM KEY_LIST WHERE ACTIVATION_CODE=?", (activation_code,))
            activation_status = cursor.fetchone()

            if activation_status is None or activation_status[0] != 'Not Activated':
                display_status(6)
                confirm_pw.focus_set()
                if confirm_pw.get() == " Confirm Password":
                    confirm_pw.delete(0,'end')
                    confirm_password_input = ''
                cursor.close()
                conn.close()
                return

            salt = uuid.uuid4().hex
            password_hash = encrypt_pw(salt,password)
            cursor.execute("UPDATE CLINICS SET EMAIL=?, PASSWORD_HASH=?, RECORD_ID=? WHERE ACTIVATION_CODE=?", (email, password_hash, salt, activation_code))
            cursor.execute("UPDATE KEY_LIST SET ACTIVATION_STATUS='Activated' WHERE ACTIVATION_CODE=?", (activation_code,))
            conn.commit()
            display_status(6)
        
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            display_status(7)

        finally:
            cursor.close()
            conn.close()


    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            register_status.config(text="Email field cannot be blank", fg = 'red', bg = 'white')
        elif status == 1:
            register_status.config(text="Password field(s) cannot be blank", fg = 'red', bg = 'white')
        elif status == 2:
            register_status.config(text="Passwords do not match", fg = 'red', bg = 'white')
        elif status == 3:
            register_status.config(text="Email already exist", fg = 'red', bg = 'white')
        elif status == 4:
            register_status.config(text="Activation Code cannot be blank", fg='red', bg='white')
        elif status == 5:
            register_status.config(text="Invalid code/Code has already been used", fg='red', bg='white')
        elif status == 6:   
            register_status.config(text="Successful Registration", fg = 'green', bg = 'white')
        elif status == 7:
            register_status.config(text="Database error occurred. Please try again", fg='red', bg='white')




##########################################################################################################################################            
    #   Load vector file (.eps) using PIL
    path_register_logo = os.path.join(resources_path, "register.eps")
    image = Image.open(path_register_logo)

    #   Resize
    new_width, new_height = 300,320
    image = image.resize((new_width,new_height))

    #   Convert .eps file to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image=image)

    #   Create label for image
    Label(registration_root, image=tk_image,bg='White').place(x=50,y=50, width=400,height=400)

    #Login box frame (PV)
    frame= Frame(registration_root,width=350, height=350,bg='white')
    frame.place(x=480,y=90)

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=(font_1,23,'bold'))
    heading.place(x=100,y=5)

##########- This part handles changing icon and sets global value -##########
    def toggle_password():
        global password_button2_mode

        if password_button2_mode:
            password_toggle_mode.config(image = show_password_button)
            password_button2_mode = False

        else:
            password_toggle_mode.config(image = hide_password_button)
            password_button2_mode = True
            
        password_mode()
        
    def toggle_confirm_password():
        global confirm_password_button_mode

        if confirm_password_button_mode:
            confirm_password_toggle_mode.config(image = show_password_button)
            confirm_password_button_mode = False

        else:
            confirm_password_toggle_mode.config(image = hide_password_button)
            confirm_password_button_mode = True
        
        confirm_password_mode()
###############################################################################
##########- Shows/Hide password -##########
    def password_mode():
        password = pw.get()
        if password != '' and password != ' Password':
            global password_input2
            password_input2 = password
        else:
            password_input2 = ''


        if password_input2 == '':
            pw.config(show = '')
            pw.delete(0,'end')
            pw.insert(0,' Password')
        
        elif password_button2_mode:
            pw.config(show = '')
            
        else:
            pw.config(show = '*')        
###########################################
    def confirm_password_mode():
        confirm_password = confirm_pw.get()
        if confirm_password != '' and confirm_password != ' Confirm Password':
            global confirm_password_input
            confirm_password_input = confirm_password
        else:
            confirm_password_input = ''


        if confirm_password_input == '':
            confirm_pw.config(show = '')
            confirm_pw.delete(0, 'end')
            confirm_pw.insert(0, ' Confirm Password')

        elif confirm_password_button_mode:
            confirm_pw.config(show = '')

        else:
            confirm_pw.config(show = '*')
###########################################
    def loginX():
        global form_type
        form_type = 1
        registration_root.after(1000,lambda:registration_root.destroy())
###########################################
    def on_enter_email(e):
        if  email_input2 == '':
            user.delete(0,'end')

    def on_leave_email(e):
        name = user.get()
        if name == '':
            global email_input2
            user.insert(0,' Email')
            email_input2 = ''

        elif user.get() == ' Email':
            email_input2 = ''

        else:
            email_input2 = user.get()

    user = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    user.place(x=30,y=80)
    user.insert(0,' Email')
    user.bind('<FocusIn>', on_enter_email) and user.bind('<FocusOut>', on_leave_email)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
##############################################################################
    def on_enter_password(e):
       if  password_input2 == '' or pw.get() == ' Password':
        pw.delete(0,'end')
        
        if password_button2_mode:                
            pw.config(show = '')
        
        else:
            pw.config(show = '*')        

    def on_leave_password(e): 
        password_mode()

    pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    pw.place(x=30,y=130)
    pw.bind('<FocusIn>', on_enter_password) and pw.bind('<FocusOut>', on_leave_password)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=157)
##############################################################################
    def on_enter_confirm_password(e):
       if  confirm_password_input == '' or pw.get() == ' Confirm Password':
        confirm_pw.delete(0,'end')
        
        if confirm_password_button_mode:                
            confirm_pw.config(show = '')
        
        else:
            confirm_pw.config(show = '*')        

    def on_leave_confirm_password(e):
        confirm_password_mode()

    confirm_pw = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    confirm_pw.place(x=30,y=180)
    confirm_pw.bind('<FocusIn>', on_enter_confirm_password) and confirm_pw.bind('<FocusOut>', on_leave_confirm_password)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=209)
##############################################################################
    def on_enter_activation_code(e):
        if not activation_code_input or activation_code_entry.get() == ' Activation Code':
            activation_code_entry.delete(0, 'end')

    def on_leave_activation_code(e):
        global activation_code_input
        code = activation_code_entry.get()
        if code == '':
            activation_code_entry.insert(0, ' Activation Code')
            activation_code_input = ''
        else:
            activation_code_input = code

    activation_code_entry = Entry(frame, width=25, fg='black', border=0, bg="White", font=(font_1, 11))
    activation_code_entry.place(x=30, y=230)
    activation_code_entry.insert(0, ' Activation Code')
    activation_code_entry.bind('<FocusIn>', on_enter_activation_code)
    activation_code_entry.bind('<FocusOut>', on_leave_activation_code)
    Frame(frame, width=295, height=2, bg='black').place(x=25, y=257)
##############################################################################

    sign_up_button=Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=290)
    label=Label(frame,text="Already have an account?",fg='black',bg='white',font=(font_1,9)).place(x=75,y=300)

    sign_in = Button(frame,width= 6,text='Sign In', border = 0, bg = 'white',cursor ='hand2', fg='#57a1f8', command =loginX).place(x=225,y=300)

    password_toggle_mode = Button(registration_root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_password)
    password_toggle_mode.place(x=770,y=220)
    
    confirm_password_toggle_mode = Button(registration_root, width=24,height = 24, pady=7, bd = 0, bg = 'white', command = toggle_confirm_password)
    confirm_password_toggle_mode.place(x=770,y=270)

    register_status = Label(frame, text = "",fg = 'white',bg = 'white')
    register_status.place(x=75,y=330)

    registration_root.bind('<Return>', on_enter)

    toggle_password()
    toggle_confirm_password()

    # run the window
    registration_root.mainloop()

   
    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tooltip = None
            self.widget.bind("<Enter>", self.show_tooltip)
            self.widget.bind("<Leave>", self.hide_tooltip)

        def show_tooltip(self, event):
            x = self.widget.winfo_rootx() + self.widget.winfo_width()
            y = self.widget.winfo_rooty() 
            self.tooltip = Toplevel(self.widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            label = Label(self.tooltip, text=self.text, background="#3B3B3B",foreground="white", relief=SOLID, borderwidth=1, padx=5, pady=5)
            label.pack()

        def hide_tooltip(self, event):
            if self.tooltip:
                self.tooltip.destroy()
                self.tooltip = None    

def main_app():
    global logged_in_email  #   Supplies logged in email

    # Database
    path_db_file = os.path.join(db_path, "database.db")
    Connect = sqlite3.connect(path_db_file)
    cursor = Connect.cursor()

    # Fetch details using the logged-in email
    cursor.execute("SELECT CLINIC_NAME, CLINIC_ADDRESS, ACTIVATION_CODE FROM CLINICS WHERE EMAIL=?", (logged_in_email,))
    clinic_details = cursor.fetchone()

    if clinic_details:
        clinic_name = clinic_details[0]
        clinic_address = clinic_details[1]
        activation_code = clinic_details[2]
    else:
        clinic_name = clinic_address = activation_code = 'N/A'  # Default values if no details found

    # Close the database connection
    cursor.close()
    Connect.close()

    ###--- Window ---###
    # Tkinter window
    app_root = Tk()

    # Window title
    app_root.title("Clinic Information")

    # Make window resizable
    app_root.geometry("925x500")
    app_root.configure(bg="white")
    app_root.resizable(True, True)

    # Configure grid layout
    app_root.grid_columnconfigure(0, weight=1)
    app_root.grid_rowconfigure(0, weight=1)

    # Create a Treeview widget
    tree = ttk.Treeview(app_root, columns=("Clinic Name", "Clinic Address", "Activation Code"), show='headings')
    tree.heading("#1", text="Clinic Name")
    tree.heading("#2", text="Clinic Address")
    tree.heading("#3", text="Activation Code")

    tree.column("#1", width = 200, anchor = "center")
    tree.column("#2", width = 200, anchor = "center")
    tree.column("#3", width = 200, anchor = "center")
    
    # Insert the clinic details into the Treeview
    tree.insert("", "end", values=(clinic_name, clinic_address, activation_code))

    # Place the Treeview widget using grid
    tree.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    # Add a scrollbar for the Treeview
    scrollbar = ttk.Scrollbar(app_root, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    # Run the window
    app_root.mainloop()



################################################################################
def state():
    global form_type
    #print ("State successfully executed (Line: 1019)")
    while True:
        if form_type == 1:
            login()
        elif form_type == 2:
            #print ("Registration state executed (Line: 1024)")
            registration()
        elif form_type == 3:
            form_type = 0
            #print("Call ext lib")
            main_app() # Link  with other module
            #print ("Logging out...")
        else:
            break
################################################################################      

state()