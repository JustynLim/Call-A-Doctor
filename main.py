from tkinter import *
from tkinter import messagebox, simpledialog, ttk
from tkinter import Label, Toplevel
from PIL import Image, ImageTk
from plyer import notification
from tkcalendar import Calendar
import datetime; import os; import sqlite3; import hashlib; import uuid


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
username_input1         = '' 
username_input2         = ''
password_input1         = ''
password_input2         = ''
confirm_password_input  = ''

# Global variable declarations
user_table_definition = """
CREATE TABLE USERS (USERNAME TEXT, PASSWORD_HASH TEXT,RECORD_ID TEXT)"""

# Connect to db. Create entity
path_db_file = os.path.join(db_path, "account.db")
connection = sqlite3.connect(path_db_file)                  # sqlite3.connect(global_path+DB_NAME)                                                                 #   Insert global path
cursor_master = connection.cursor()
cursor_master.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USERS'")
if cursor_master.fetchone() is None:
    cursor = connection.cursor()
    cursor.execute(user_table_definition)
    connection.commit()
    cursor.close()


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
        global username_input1; global password_input1
        on_leave_username(None); on_leave_password(None)
        username = username_input1; password = password_input1

#   Login auth (version 1)
        if username is None or password is None:
            display_status(0)
            #print("Line 83")
        else:
            db_conn = sqlite3.connect(path_db_file)
            cursor_user = db_conn.cursor()
            cursor_user.execute("SELECT username,password_hash,record_id FROM Users WHERE username=?", (username,))
            row = cursor_user.fetchone()
        
        if row is not None:
            salt_db = row[2]
            password_hash_db = row[1]
            password_hash = encrypt_pw(salt_db,password)
            if password_hash_db != password_hash:
                display_status(0)
                #print("Line 96")

            else:
                global form_type
                display_status(1)
                login_root.after(1000,lambda:login_root.destroy())
                form_type = 3

        else:
            display_status(0)
        #print("Line 105")
        pw.focus_set()
        if pw.get() == " Password":
            pw.delete(0,'end')
            password_input1 = ''

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            login_status.config(text="Invalid username/password",fg='red',bg='white')
            
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
    def on_enter_username(e):
        if  username_input1 == '':
            user.delete(0,'end')

    def on_leave_username(e):
        name = user.get()
        #print("On leave user")
        if name == '':
            global username_input1
            user.insert(0,' Username')
            username_input1 = ''

        elif user.get() == ' Username':
            username_input1 = ''

        else:
            username_input1 = user.get()      

    user = Entry(frame,width = 25,fg = 'black',border = 0,bg = "white",font = (font_1,11)) # Cannot use: .place(x=30,y=80),causes error
    user.place(x = 30,y = 80)
    user.insert(0,' Username')
    user.bind('<FocusIn>', on_enter_username) and user.bind('<FocusOut>', on_leave_username)

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

        global username_input2; global password_input2; global confirm_password_input

        on_leave_username(None); on_leave_password(None); on_leave_confirm_password(None)

        username=username_input2; password=password_input2; verify_password=confirm_password_input
        #print (username_input2,password_input2,confirm_password_input)
        
        isError = False
        if username is None or username == '':
            display_status(0)
            isError = True
        

        elif password is None or verify_password is None or password == '' or verify_password == '':
            display_status(1)
            isError = True 
            
        elif password != verify_password:
            display_status(2)
            isError = True
        
        if isError:
            #print("isError")
            confirm_pw.focus_set()
            if confirm_pw.get() == " Confirm Password":
                confirm_pw.delete(0,'end')
                confirm_password_input = ''
            return
        
        path_db_file = os.path.join(db_path, "account.db")
        db_conn = sqlite3.connect(path_db_file)
        cursor_user = db_conn.cursor()
        cursor_user.execute("SELECT * FROM Users WHERE username=?", (username,))
        existing_user = cursor_user.fetchone()

        if existing_user is not None:
            display_status(3)
            confirm_pw.focus_set()
            if confirm_pw.get() == " Confirm Password":
                confirm_pw.delete(0,'end')
                confirm_password_input = ''

        
        else:
            salt = uuid.uuid4().hex
            cursor_user.execute("INSERT INTO Users (USERNAME,PASSWORD_HASH,RECORD_ID) VALUES (?,?,?)", (username, encrypt_pw(salt,password),salt))
            db_conn.commit()
            display_status(4)

        cursor_user.close()
        db_conn.close()

    def encrypt_pw(salt,password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt
    
    def display_status(status):
        if status == 0:
            register_status.config(text="Username field cannot be blank", fg = 'red', bg = 'white')
        elif status == 1:
            register_status.config(text="Password field(s) cannot be blank", fg = 'red', bg = 'white')
        elif status == 2:
            register_status.config(text="Passwords do not match", fg = 'red', bg = 'white')
        elif status == 3:
            register_status.config(text="Username already exist", fg = 'red', bg = 'white')
        elif status == 4:
            register_status.config(text="Successful Registration", fg = 'green', bg = 'white')



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
    def on_enter_username(e):
        if  username_input2 == '':
            user.delete(0,'end')

    def on_leave_username(e):
        name = user.get()
        if name == '':
            global username_input2
            user.insert(0,' Username')
            username_input2 = ''

        elif user.get() == ' Username':
            username_input2 = ''

        else:
            username_input2 = user.get()

    user = Entry(frame,width=25,fg='black',border=0,bg="White",font=(font_1,11))
    user.place(x=30,y=80)
    user.insert(0,' Username')
    user.bind('<FocusIn>', on_enter_username) and user.bind('<FocusOut>', on_leave_username)

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

    sign_up_button=Button(frame,width=39,pady=7,text='Sign Up',bg='#57a1f8',fg='white',border=0,command=signup).place(x=35,y=240)
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

def main_app():

    ### Global Variable ###
    global_path     = os.path.dirname(__file__)
    resources_path  = os.path.join(global_path, "resources")
    db_path         = os.path.join(global_path, "db")
    global destroy_state
    global refresh_task_list


    # Database
    path_db_file = os.path.join(db_path, "account.db")
    Connect = sqlite3.connect(path_db_file)
    cursor = Connect.cursor()


######################################################################################################################################
    ###--- Window ---###
    # Tkinter window
    app_root = Tk()

    # Window title
    app_root.title("To-Do List")

    # Window size
    app_root.geometry("925x500")
    app_root.resizable(False, False)

    # Background
    app_root.configure(bg = "white")

    task_list =[]
    destroy_state = False
    refresh_task_list   = False
    
######################################################################################################################################
    ###--- Background design ---###
    # App Icon
    path_icon1 = os.path.join(resources_path, "Icon1.png") #Path to image
    Image_icon = PhotoImage(file = path_icon1)
    app_root.iconphoto(False, Image_icon)
    
    # Topbar

    Image_path2 = os.path.join(resources_path, "amethyst.jpg")
    image1 = Image.open(Image_path2)    # Resize the image

    background_width = 1600   # Set size of the image
    background_height = 71

    resized_image = image1.resize((background_width, background_height), Image.LANCZOS)

    New_topbar = ImageTk.PhotoImage(resized_image)
    label_1 = Label(app_root, image = New_topbar)
    label_1.pack()

    # Sidebar
    newside_width = 100   # Set size of the image
    newside_height = 500

    resized_Side = image1.resize((newside_width, newside_height), Image.LANCZOS)

    New_Sidebar = ImageTk.PhotoImage(resized_Side)
    label_2 = Label(app_root, image = New_Sidebar, bg = "white")
    label_2.place(x = 850, y = 72)

    # Top heading
    greet_user = username_input1
    Heading = Label(app_root, text=f"HI {greet_user.upper()}",  font = "arial 20 bold", fg = "white", bg = "#9960D1")       ###### Initial code: Heading = Label(root, text="TASK",  font = "arial 20 bold", fg = "white", bg = "#9960D1")
    Heading.place(x = 400, y = 20)

    # darkmode image path
    Image_path3 = os.path.join(resources_path, "topback.png")
    image2 = Image.open(Image_path3)

    resized_topbar = image2.resize((background_width, background_height), Image.LANCZOS)

    dark_topbar = ImageTk.PhotoImage(resized_topbar)

    resized_dsidebar = image2.resize((newside_width, newside_height), Image.LANCZOS)

    dark_sidebar = ImageTk.PhotoImage(resized_dsidebar)

    selected_date = ""
    global task_notification
    task_notification = True

######################################################################################################################################
    ###--- Function ---###
    def self_refresh():                             # <<<<< added func to continuously refresh list
        global refresh_task_list
        global destroy_state
        if refresh_task_list:
            load_tasks()
            refresh_task_list = False
        if destroy_state == False:
            app_root.after(500,self_refresh)        #print ("Refresh list")

    # Input error
    def error_intput() :
        if task_entry.get() == "" :
            messagebox.showerror("Error","Task Name cannot be blank!")
            return 0
        return 1

    # Clear task
    def clear_taskField() :
        task_entry.delete(0, END)

    # Insert task
    def add_task():
        global username_input1
        global task_notification
        task_notification = False
        value = error_intput()
        if value == 0:
            return
        select_date()                               # <<<<< added call func

    def add_task2():                                # <<<<< added a 2nd part function from manual input to adding entry directly into db using calendar
        global selected_date
        #select_date()
        content = task_entry.get()      
        #print("add_task2")
        deadline = selected_date
        #print (deadline)
        if deadline:
            current_date = datetime.datetime.now().date()
            deadline_date = datetime.datetime.strptime(deadline, "%m/%d/%y").date()
            #print (deadline_date)

            if deadline_date >= current_date:
                cursor.execute("""INSERT INTO TASK (USERNAME, TASK_NAME, TASK_DUEDATE, COMPLETED) 
                VALUES (?, ?, ?, 0)""", 
                (username_input1, content, deadline_date))
                Connect.commit()

                task_list.append((content, deadline_date))
                load_tasks()

            else:
                messagebox.showerror("Invalid Deadline", "The deadline cannot be in the past.")

        clear_taskField()
        
    def select_date():                                      # <<<<<< creates a calendar using a separate window
        def on_date_select():
            global selected_date
            selected_date = cal.get_date()
            #print("Selected Date:", selected_date)
            top.destroy()
            add_task2()                                     # <<<<<< executes func to add task + if-else conditions
            return

        top = Toplevel(app_root)
        top.title("Select Date")

        cal = Calendar(top, selectmode='day')
        cal.pack(pady=10)

        confirm_btn = Button(top, text="Confirm Date", command=on_date_select)
        confirm_btn.pack(pady=10)
        #print ("on_date_select")





    # Load task
    def load_tasks():
        global username_input1
        global task_list           # <<<<<< added global
        global task_notification
        cursor.execute(f"SELECT TASK_NAME, TASK_DUEDATE, TASK_ID FROM TASK WHERE COMPLETED = 0 and USERNAME = ? order by TASK_DUEDATE",(username_input1,))
        #print (username_input1)
        #tasks = cursor.fetchall()
        row = cursor.fetchone()
        task_list =[]
        #task_tree.delete(0,999)     
        #task_tree.delete(*task_tree.get_children())
        for item in task_tree.get_children():
            task_tree.delete(item)
        task_tree.size 
        current_date = datetime.datetime.now().date()

        #for task in tasks:
        while row is not None:

            content = row[0]; deadline = row[1]; column3 = row[2]         # Store Unique ID from table (to delete tasks)
            deadline_date = datetime.datetime.strptime(deadline, "%Y-%m-%d").date()
            days_left = (deadline_date - current_date).days

            if task_notification:

                if days_left < 0:
                    notification_title = "Task Reminder"
                    notification_message = f"Task:'{content}' is overdue!"
                    notification.notify(title=notification_title, message=notification_message, timeout = 5)
                elif days_left == 0:
                    notification_title = "Task Reminder"
                    notification_message = f"Task: {content}\n\nDue date: Today"
                    notification.notify(title=notification_title, message=notification_message, timeout = 5)
                elif days_left == 1:
                    notification_title = "Task Reminder"
                    notification_message = f"Task:'{content}' is due tomorrow!"
                    notification.notify(title=notification_title, message=notification_message, timeout = 5)  
                elif days_left > 1 and days_left <= 7:
                    notification_title = "Task Reminder"
                    notification_message = f"Task: {content}\n\nDue date: {days_left} days"
                    notification.notify(title=notification_title, message=notification_message, timeout = 5)

            task_list.append((content, deadline))
            #task_tree.insert(END, f"{content} \nDeadline: {deadline}, Days Left: {days_left})")
            task_tree.insert("", END, values=(content, deadline, days_left, column3))
            row = cursor.fetchone()


    # Delete task
    def delete_task():
        global task_notification
        selected_task = task_tree.selection() #[0]
        record_id = int(task_tree.item(selected_task, "value")[3])
        #print (record_id)
        #print ("Delete Task")

        if record_id > 0:           # <<<<<< safeguard

            try:
                cursor.execute("DELETE FROM TASK WHERE TASK_ID = ?", (record_id,)) # <<<<<< using id instead of task name; prevents deletion of tasks with same name
                Connect.commit()
                task_notification = False
                load_tasks()
                #task_list.pop(index)
                #listbox.delete(index)
            except sqlite3.Error as error:
                print("Error deleting task:", error)

    # Edit task
    def edit_task():
        selected_task = task_tree.selection()    # Initial: selected_task = task_tree.curselection()[0]
        record_id = int(task_tree.item(selected_task, "value")[3])
        global refresh_task_list

        if record_id > 0:
            #print ("Select task")
            #print(int(selected_task[1:])-1)
            #change_task = task_id [int(selected_task[1:])-1] # change_task = (task_id [int(selected_task[1:])])
            #print(change_task)
            refresh_task_list = False
            edit_task2(record_id)



    # Complete task
    def complete_task():
        global task_notification
        selected_task = task_tree.selection() #[0]
        record_id = int(task_tree.item(selected_task, "value")[3])
        task_name = task_tree.item(selected_task, "value")[0]

        #task_name = selected_item.split(' (Deadline:')[0]  # Extract task name from selected item
        if record_id > 0:

            try:
                cursor.execute("UPDATE TASK SET COMPLETED = 1 WHERE TASK_ID = ?", (record_id,))
                Connect.commit()
                task_notification = False
                load_tasks()
        
                notification_title = "Task Completed"
                notification_message = f"Task: {task_name} has been completed!"
                notification.notify(title = notification_title, message = notification_message, timeout = 5)

            except sqlite3.Error as error:
                print("Error completing task:", error)

    # Log out function
    def log_out():
        global destroy_state
        destroy_state = True
        global form_type
        form_type = 1
        app_root.after(700,on_destroy)
        global task_notification
        task_notification = False
        #app_root.destroy()
        #app_root.quit()  # Close the main window
    
    def on_destroy():
        app_root.destroy()    

    # Display calendar
    def display_calendar():
        global task_list
        calendar_window = Toplevel(app_root)
        calendar_window.title("Calendar")
        calendar_window.geometry("400x400")
        calendar_window.configure(bg = "black")
        
        calendar = Calendar(calendar_window, selectmode="day", background="white", foreground="black", selectbackground="blue", font="arial 16")
        calendar.pack(pady=10)
        #print("calendar func")
        
        tasks = []
        for task in task_list:
            task_name = task[0]
            deadline = task[1]
            task_info = f"Task: {task_name}\nDeadline: {deadline}"
            tasks.append(task_info)
        
        tags = ["task{}".format(i) for i in range(len(tasks))]
        for tag in tags:
            calendar.tag_config(tag, background="#2E1A47")
        
        for i, task in enumerate(tasks):
            date = datetime.datetime.strptime(task_list[i][1], "%Y-%m-%d").date()
            calendar.calevent_create(date, "Task", tags=tags[i])
        
        def show_task_details(event):
            selected_date = calendar.selection_get()
            task_details_label.config(text="")
            tasks_on_selected_date = []
            #print(selected_date)

            for i, task in enumerate(task_list):
                task_date = datetime.datetime.strptime(task[1], "%Y-%m-%d").date()
                if selected_date == task_date:
                    tasks_on_selected_date.append(tasks[i])

            if tasks_on_selected_date:
                task_details = "\n\n".join(tasks_on_selected_date)
                task_details_label.config(text=task_details)
        
        task_details_label = Label(calendar_window, text="", font="arial 12", bg="black", fg="white")
        task_details_label.pack(pady=10)
        
        calendar.bind("<<CalendarSelected>>", show_task_details)

    # Change Theme
    def system_theme():
        global button_mode

        if button_mode:
            #messagebox.showerror('Dark',"Dark Mode")
            toggle_mode.config(image = darkmode_button ,bg = '#26242f',activebackground = "#26242f")
            app_root.config(bg = "#26242f")
            Usr_frame.config(bg = "white")
            label_1.config(image = dark_topbar)
            label_2.config(image= dark_sidebar)
            Heading.config(bg = "#2E1A47")
            frame1.config(bg = "#2E1A47")
            #listbox.config(bg = "#2E1A47")
            #delete_button.config(image = darkmode_del_button)
            delete_button.config(bg = "#2E1A47")
            #edit_button.config(image = darkmode_edit_button)
            edit_button.config (image = darkmode_edit_button,bg = "#2E1A47")
            #complete_button.config(darkmode_complete_button)
            complete_button.config(bg = "#2E1A47")
            calendar_button.config(bg = "#2E1A47")
            toggle_mode.config(bg = "#2E1A47")

            button_mode = False

        else:
            #messagebox.showerror('Light',"Light Mode")
            #delete_button.config(image = lightmode_deletebtn)
            toggle_mode.config(image = lightmode_button, bg = "white", activebackground = "white")
            app_root.config(bg = "white")
            Usr_frame.config(bg ="#9960D1")
            label_1.config(image = New_topbar)
            label_2.config(image= New_Sidebar)
            Heading.config(bg = "#9960D1")
            frame1.config(bg = "#9960D1")
            #listbox.config(bg = "#9960D1")
            #delete_button.config(image = lightmode_del_button)
            delete_button.config(bg = "#9960D1")
            #edit_button.config(image = lightmode_edit_button)
            edit_button.config(image = lightmode_edit_button,bg = "#9960D1")
            complete_button.config(bg = "#9960D1")
            calendar_button.config(bg = "#9960D1")
            toggle_mode.config(bg = "#9960D1")

            button_mode = True
        
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
    ######################################################################################################################################
    ###--- Main UI ---###
    # Frame of user input box
    Usr_frame = Frame(app_root, width = 410, height = 50, bg = "#9960D1")
    Usr_frame.place(x = 260, y = 105)

    # User input box
    task = StringVar()
    task_entry = Entry(Usr_frame, width = 20, font = "arial 20", bd = 0, bg= "white", fg = "black")
    task_entry.place(x = 10, y = 7)
    task_entry.focus()

    # Task list frame
    frame1 = Frame(app_root, bd = 3, width = 700, height = 280, bg ="#9960D1" )
    frame1.pack(padx = (50,0),pady = (100,0))

    # Treeview to display tasks
    task_tree = ttk.Treeview(frame1, columns=("Task Name", "Deadline", "Days Left", "Task_ID"), show="headings")
    task_tree.pack(side= LEFT, fill= BOTH)

    

    # Task List box
    #listbox = Listbox(frame1, font = "arial 12 bold", width = 80, height = 15, bg = "#9960D1", fg = "white", cursor = "hand2" , selectbackground = "black")
    #listbox.pack(side = LEFT, fill = BOTH, padx= 2)

    # Scroll bar
    scrollbar = Scrollbar(frame1)
    scrollbar.pack(side = RIGHT , fill = BOTH)

    task_tree.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = task_tree.yview)

    #   Column headers
    task_tree.column("Task Name", anchor = CENTER, width = 300, minwidth = 200, stretch = True )
    task_tree.heading("Task Name", text = "Task Name")
    task_tree.column("Deadline", anchor = CENTER, width = 70, minwidth = 70, stretch = False )
    task_tree.heading("Deadline", text = "Deadline")
    task_tree.column("Days Left", anchor = CENTER, width = 70, minwidth = 70, stretch = False )
    task_tree.heading("Days Left", text = "Days Left")
    task_tree.column("Task_ID", anchor = CENTER, width = 0, minwidth = 0, stretch = False )
    task_tree.heading("Task_ID", text = "Task_ID")

    load_tasks()

    ######################################################################################################################################
    ###--- Button ---###

    # Add task button
    Add_button = Button(Usr_frame, text = "ADD", font = "arial 20 bold", width = 5, bg = "#8D50C7", fg = "white", bd=0, command = add_task)
    Add_button.place(x = 320, y = 0)
    ToolTip(Add_button, "Add Task")

    # Delete task buttton
    Image_path4 = os.path.join(resources_path, "delete.png")
    image3 = Image.open(Image_path4)

    delete_icon = ImageTk.PhotoImage(image3)
    
    delete_button = Button(app_root, image = delete_icon , bg = "#9960D1", bd = 0, command = delete_task)
    delete_button.place(x = 862, y = 180)
    ToolTip(delete_button, "Delete Task")

    # Edit task button
    Image_path5 = os.path.join(resources_path, "edit_light.png")
    image4 = Image.open(Image_path5)

    Image_path5a = os.path.join(resources_path, "edit_dark.png")
    image4a = Image.open(Image_path5a)

    lightmode_edit_button = ImageTk.PhotoImage(image4)
    darkmode_edit_button = ImageTk.PhotoImage(image4a)

    edit_button = Button(app_root, image = lightmode_edit_button, bg="#9960D1", bd = 0, command = edit_task)
    edit_button.place(x = 865, y = 280)
    ToolTip(edit_button, "Edit Task")

    # Complete task button
    Image_path6 = os.path.join(resources_path, "complete.png")
    image5 = Image.open(Image_path6)

    complete_icon = ImageTk.PhotoImage(image5)

    complete_button = Button(app_root, image= complete_icon, bg="#9960D1", bd=0, command=complete_task)
    complete_button.place(x=862, y=380)
    ToolTip(complete_button, "Mark as done")

    # Log out button
    logout_button = Button(app_root, text="Log Out",bg= "purple", fg="white", font="arial 14 bold", width=10, command=log_out)
    logout_button.place(x=100, y=20)

    # Calendar button
    Image_path7 = os.path.join(resources_path, "calendar.png")
    image6 = Image.open(Image_path7)

    calendar_icon = ImageTk.PhotoImage(image6)

    calendar_button = Button(app_root, image=calendar_icon, bg="#9960D1", bd=0, command= display_calendar)
    calendar_button.place(x=15,y=15)
    ToolTip(calendar_button, "Task Calendar")

    # Theme change buton
    Image_path8 = os.path.join(resources_path, "light_mode.png")
    image7 = Image.open(Image_path8)

    Image_path9 = os.path.join(resources_path, "dark_mode.png")
    image8 = Image.open(Image_path9)

    lightmode_button = ImageTk.PhotoImage(image7)
    darkmode_button = ImageTk.PhotoImage(image8)

    global button_mode
    button_mode = True

    toggle_mode = Button(app_root, width=173,height = 69, pady=7, image = lightmode_button, bd=0, bg = "#9960D1", command = system_theme)
    toggle_mode.place(x = 750, y = 2)
    ToolTip(toggle_mode, "Switch Theme")

    self_refresh()

    app_root.mainloop()

def edit_task2(task_id):                # get task_id to edit
    def on_date_select():
        global refresh_task_list
        global task_notification
        selected_date = cal.get_date()
        #print(selected_date,entry.get())
        # Update record into table
        current_date = datetime.datetime.now().date()
        deadline_date = datetime.datetime.strptime(selected_date, "%m/%d/%y").date()
        #print (deadline_date)

        if deadline_date >= current_date:
            #print ("Update task")
            db_conn = sqlite3.connect(path_db_file)
            cursor_user = db_conn.cursor()
            cursor_user.execute("UPDATE TASK SET TASK_NAME = ?, TASK_DUEDATE = ? WHERE TASK_ID = ?" , (entry.get(), deadline_date, task_id))
            db_conn.commit()
            cursor_user.close()
            db_conn.close()
            
            refresh_task_list = True
            task_notification = True

        else:
            print ("Error saving changes")
            messagebox.showerror("Invalid Deadline", "The deadline cannot be in the past.")

        root.destroy()
    
    root = Tk()
    root.title("To-Do List")
        
    entry = Entry(root, width=30)
    entry.pack()
    cal = Calendar(root, selectmode="day")
    cal.pack()
    select_button = Button(root, text="Save changes", command=on_date_select)
    select_button.pack()

    db_conn = sqlite3.connect(path_db_file)
    cursor_user = db_conn.cursor()

# open db, select task_name, task_duedate from task where task_id = ?
    cursor_user.execute(f"SELECT TASK_NAME, TASK_DUEDATE FROM TASK WHERE TASK_ID = ?",(task_id,))
    row = cursor_user.fetchone()

    if row is not None:
        entry.delete(0,'end')
        entry.insert(0,row[0])

    cursor_user.close()
    db_conn.close()
    

    
    # Selected date label
    selected_date = StringVar()
    
    
    root.mainloop()

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
            main_app()
            #print ("Logging out...")
        else:
            break
################################################################################      

state()





"""
1)  Why is root destroyed before going to next screen?
    Releases memory (otherwise keeps opening new window; increases RAM usage)

2)  Why form_type is used instead of directly calling specific modules
    The previous windows do not terminate when done so, it just opens new window (increases memory usage over time)
    ; hence the state must be defined in order to terminate previous windows (releases memory usage)
"""