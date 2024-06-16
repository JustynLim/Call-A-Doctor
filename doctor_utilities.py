import hashlib, sqlite3, uuid

# Global variable(s)
path_db_file    = "db/database.db"

def login(controller, email, password):
        
        email = email.lower()
        #   Login auth (version 1)
        if email and password:
                try:
                    with sqlite3.connect(path_db_file) as db_conn:
                        cursor_user = db_conn.cursor()
                        cursor_user.execute("SELECT DOCTOR_EMAIL,PASSWORD_HASH,RECORD_ID FROM DOCTORS WHERE DOCTOR_EMAIL=?", (email,))
                        row = cursor_user.fetchone()

                        if row is not None:
                                salt_db = row[2]
                                password_hash_db = row[1]
                                password_hash = encrypt_pw(salt_db,password)
                                
                                if password_hash_db != password_hash:
                                        login_display_status(controller, 0)
                                else:
                                     login_display_status(controller, 1)
                                    #  logged_in_email = email
                                    #  form_type = 3
                        else:
                             login_display_status(controller, 0)
                
                except sqlite3.Error as e:
                      print(f"Database error: {e}")
                      login_display_status(controller, 0)

    
def register(email, password, activation_code):
    status = -1

    
    with sqlite3.connect(path_db_file) as db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT EMAIL FROM CLINICS WHERE EMAIL=?", (email,))
        email_exists = cursor.fetchone()
        print(f"Email exists check: {email_exists}")

        if email_exists:
            print("Email already exist")
            return 3
        

        cursor.execute("SELECT ACTIVATION_STATUS FROM KEY_LIST WHERE ACTIVATION_CODE=?", (activation_code,))
        activation_status = cursor.fetchone()
        print(f"Activation status check: {activation_status}")
    
        if not activation_status or activation_status[0] == 'Activated':
            return 5

        try:
            salt = uuid.uuid4().hex
            password_hash = encrypt_pw(salt,password)
            cursor.execute("UPDATE CLINICS SET EMAIL=?, PASSWORD_HASH=?, RECORD_ID=? WHERE ACTIVATION_CODE=?", (email, password_hash, salt, activation_code))
            cursor.execute("UPDATE KEY_LIST SET ACTIVATION_STATUS='Activated' WHERE ACTIVATION_CODE=?", (activation_code,))
            db_conn.commit()
            status = 6
    
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            status = 7

#     finally:
#         cursor.close()
#         db_conn.close()
            #register_display_status(controller, status)

    return status


def encrypt_pw(salt, password):
        encrypt = hashlib.sha512((salt + password).encode("UTF-8")).hexdigest()
        return encrypt

def login_display_status(controller, status):
    print(f"Controller in login_display_status: {controller}")
    label = controller.login_widget.label_6
    
    if status == 0:
            label.setText("Invalid email/password")
            label.setStyleSheet("color:red")
    
    else:
            controller.login_widget.label_6.setText("Login successful")
            controller.login_widget.label_6.setStyleSheet("color:green")

def register_display_status(register_form, status):
    label = register_form.label_18
    
    if status == 0:
        label.setText("Email field cannot be blank")
        label.setStyleSheet("color:red")
    
    elif status == 1:
        label.setText("Password field(s) cannot be blank")
        label.setStyleSheet("color:red")
    
    elif status == 2:
        label.setText("Passwords do not match")
        label.setStyleSheet("color:red")
    
    elif status == 3:
        label.setText("Email already exist")
        label.setStyleSheet("color:red")
    
    elif status == 4:
        label.setText("Activation Code cannot be blank")
        label.setStyleSheet("color:red")
    
    elif status == 5:
        label.setText("Invalid code/Code has already been used")
        label.setStyleSheet("color:red")
    
    elif status == 6:   
        label.setText("Successful Registration")
        label.setStyleSheet("color:green")
    
    elif status == 7:
        label.setText("Database error occurred. Please try again")
        label.setStyleSheet("color:red")