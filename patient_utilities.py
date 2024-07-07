import hashlib, os, sqlite3, uuid

# Global variable(s)
global_path         = os.path.dirname(__file__)
db_path             = os.path.join(global_path,"db")
path_db_file        = os.path.join(db_path, "database.db")

def login(controller, email, password):
        
        email = email.lower()
        #   Login auth (version 1)
        if email and password:
                try:
                    with sqlite3.connect(path_db_file) as db_conn:
                        cursor_user = db_conn.cursor()
                        cursor_user.execute("SELECT PATIENT_EMAIL,PASSWORD_HASH,RECORD_ID FROM PATIENT WHERE PATIENT_EMAIL=?", (email,))
                        row = cursor_user.fetchone()

                        if row is not None:
                                salt_db = row[2]
                                password_hash_db = row[1]
                                password_hash = encrypt_pw(salt_db,password)
                                
                                if password_hash_db != password_hash:
                                        return 0
                                else:
                                     return 3
                                    #  logged_in_email = email
                                    #  form_type = 3
                        else:
                             return 0
                
                except sqlite3.Error as e:
                      print(f"Database error: {e}")
                      return -1

    
def register(name, email, password, address):
    status = -1

    
    with sqlite3.connect(path_db_file) as db_conn:
        cursor = db_conn.cursor()
        cursor.execute("SELECT PATIENT_EMAIL FROM PATIENT WHERE PATIENT_EMAIL=?", (email,))
        email_exists = cursor.fetchone()
        print(f"Email exists check: {email_exists}")

        if email_exists:
            print("Email already exist")
            return 3

        try:
            salt = uuid.uuid4().hex
            password_hash = encrypt_pw(salt,password)
            cursor.execute("INSERT INTO PATIENT (PATIENT_EMAIL, PATIENT_NAME, PATIENT_ADDRESS, PATIENT_PHONENO, PASSWORD_HASH, RECORD_ID) VALUES (?,?,?,?,?,?)", (email, name, address, "", password_hash, salt))
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