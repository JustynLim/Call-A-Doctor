from ui_clinic import Ui_MainWindow
from PySide6.QtWidgets import *
from PySide6.QtCore import Slot
import sqlite3
import os
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Call A Doctor")

        # Show the home page first
        self.switch_to_homePage()

        self.widget_2.setHidden(True)

        # Connect the buttons to respective pages
        self.home_1.clicked.connect(self.switch_to_homePage)
        self.home_2.clicked.connect(self.switch_to_homePage)

        self.adddoctor_1.clicked.connect(self.switch_to_addDoctorPage)
        self.adddoctor_2.clicked.connect(self.switch_to_addDoctorPage)
        self.shortcut_add.clicked.connect(self.switch_to_addDoctorPage)

        self.viewdoctor_1.clicked.connect(self.switch_to_viewDoctorPage)
        self.view_doctor_2.clicked.connect(self.switch_to_viewDoctorPage)
        self.shortcut_view.clicked.connect(self.switch_to_viewDoctorPage)

        self.addschedule_1.clicked.connect(self.switch_to_addSchedulePage)
        self.addschedule_2.clicked.connect(self.switch_to_addSchedulePage)
        self.shortcut_schedule.clicked.connect(self.switch_to_addSchedulePage)

        self.home_1.clicked.connect(self.switch_to_homePage)
        self.home_2.clicked.connect(self.switch_to_homePage)

        self.confirm_button.clicked.connect(self.add_doctor)

        # Connect the delete button to its function
        self.delete_button.clicked.connect(self.delete_selected_doctor)

        # Connect the select doctor button to its function
        self.selectdoctor_button.clicked.connect(self.select_doctor)

        # Connect the add schedule button to its function
        self.addschedule_button.clicked.connect(self.add_schedule)

        # Load data into doctor_table
        self.load_doctors_data()

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_addDoctorPage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_viewDoctorPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.load_doctors_data()  # Reload data whenever switching to the view doctor page

    def switch_to_addSchedulePage(self):
        self.stackedWidget.setCurrentIndex(3)

    def load_doctors_data(self):
        # Define the path to the database file
        db_path = os.path.join(os.path.dirname(__file__), 'db')
        path_db_file = os.path.join(db_path, "database.db")

        # Debug: Print the database path
        print(f"Database path: {path_db_file}")

        # Check if the database file exists
        if not os.path.exists(path_db_file):
            print(f"Database file does not exist at path: {path_db_file}")
            return

        # Connect to SQLite3 database
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()

        # Execute query to retrieve data
        cursor.execute("SELECT DOCTOR_EMAIL, DOCTOR_NAME, DOCTOR_PHONENO, DOCTOR_ADDRESS, CLINIC_NAME FROM DOCTORS")
        rows = cursor.fetchall()

        # Set table row and column count
        self.doctor_table.setRowCount(len(rows))
        self.doctor_table.setColumnCount(5)

        # Set table headers
        headers = ["Doctor's Email", "Doctor's Name", "Doctor's Phone Number", "Doctor's Address", "Clinic Name"]
        self.doctor_table.setHorizontalHeaderLabels(headers)

        # Populate table with data
        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.doctor_table.setItem(row_idx, col_idx, QTableWidgetItem(col_data))

        # Close the database connection
        connection.close()

    @Slot()
    def delete_selected_doctor(self):
        # Get the selected row
        selected_row = self.doctor_table.currentRow()

        if selected_row >= 0:  # Ensure a row is selected
            # Get the doctor email from the selected row (assuming it's in the first column)
            doctor_email = self.doctor_table.item(selected_row, 0).text()

            # Define the path to the database file
            db_path = os.path.join(os.path.dirname(__file__), 'db')
            path_db_file = os.path.join(db_path, "database.db")

            # Connect to SQLite3 database
            connection = sqlite3.connect(path_db_file)
            cursor = connection.cursor()

            # Delete the doctor from the DOCTORS table
            cursor.execute("DELETE FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (doctor_email,))
            # Delete the corresponding entry from the KEY_LIST table
            cursor.execute("DELETE FROM KEY_LIST WHERE ASSIGNED_TO_EMAIL = ?", (doctor_email,))
            connection.commit()

            # Close the database connection
            connection.close()

            # Remove the row from the table
            self.doctor_table.removeRow(selected_row)
        else:
            self.show_no_selection_message()

    def show_no_selection_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("No Selection")
        msg_box.setText("No row selected. Please select a row to delete.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def generate_activation_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def send_approved_email(self, email, activation_code):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # Gmail's appropriate port
        sender_email = os.environ.get('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')
        sender_password = os.environ.get('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')

        if not sender_email or not sender_password:
            print("Error: Email credentials are not set in the environment variables.")
            return

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            body = f"""<html>
                        <body>
                            <p>This is a confirmation email to acknowledge that your application has been approved. Please find your activation code attached below</p>
                            <p>Activation Code: {activation_code}</p>
                            <p></p>
                            <p></p>
                            <p>Head on over to our registration page to create an account for your profile.</p>
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

            print(f"Approved email has been sent to user's email address: {email}")
        except Exception as e:
            print("Email error:", e)
            print("Email sending failed. Please check your email settings.")

    @Slot()
    def add_doctor(self):
        email = self.doc_mail_edit.text()
        name = self.doc_name_edit.text()
        phone = self.doc_phone_edit.text()
        address = self.doc_add_edit.text()
        clinic_name = "Test Clinic"  # Assigning a test clinic name

        if email and name and phone and address:
            activation_code = self.generate_activation_code()

            # Define the path to the database file
            db_path = os.path.join(os.path.dirname(__file__), 'db')
            path_db_file = os.path.join(db_path, "database.db")

            # Connect to SQLite3 database
            connection = sqlite3.connect(path_db_file)
            cursor = connection.cursor()

            # Insert the new doctor and activation code into the database
            placeholder_password_hash = ""  # Use an empty string as a placeholder
            cursor.execute("""
                INSERT INTO DOCTORS (DOCTOR_EMAIL, DOCTOR_NAME, DOCTOR_PHONENO, DOCTOR_ADDRESS, PASSWORD_HASH, ACTIVATION_CODE, CLINIC_NAME)
                VALUES (?, ?, ?, ?, ?, ?, ?)""", (email, name, phone, address, placeholder_password_hash, activation_code, clinic_name))
            cursor.execute("""
                INSERT INTO KEY_LIST (ACTIVATION_CODE, ASSIGNED_TO_EMAIL, ACTIVATION_STATUS)
                VALUES (?, ?, 'Not Activated')""", (activation_code, email))
            connection.commit()

            # Close the database connection
            connection.close()

            # Send the activation email
            self.send_approved_email(email, activation_code)

            # Clear the input fields
            self.doc_mail_edit.clear()
            self.doc_name_edit.clear()
            self.doc_phone_edit.clear()
            self.doc_add_edit.clear()

            # Show confirmation pop-up
            QMessageBox.information(self, "Doctor Added", "Doctor is added and activation email sent.")

            print("Doctor added and activation email sent.")
        else:
            self.show_incomplete_form_message()

    def show_incomplete_form_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("Incomplete Form")
        msg_box.setText("Please fill in all the fields.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    @Slot()
    def select_doctor(self):
        db_path = os.path.join(os.path.dirname(__file__), 'db')
        path_db_file = os.path.join(db_path, "database.db")
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()

        cursor.execute("SELECT DOCTOR_EMAIL, DOCTOR_NAME FROM DOCTORS")
        doctors = cursor.fetchall()

        dialog = QDialog(self)
        dialog.setWindowTitle("Select Doctor")
        dialog.setGeometry(100, 100, 300, 100)
        layout = QVBoxLayout()

        if not doctors:
            label = QLabel("No doctors available.")
            layout.addWidget(label)
        else:
            combo = QComboBox(dialog)
            for doctor in doctors:
                combo.addItem(doctor[1], doctor[0])
            layout.addWidget(combo)

            button = QPushButton("Select", dialog)
            button.clicked.connect(lambda: self.set_selected_doctor(combo, dialog))
            layout.addWidget(button)

        dialog.setLayout(layout)
        dialog.exec()

    def set_selected_doctor(self, combo, dialog):
        selected_doctor = combo.currentText()
        self.doctor_name_label.setText(f"Doctor {selected_doctor}")
        dialog.close()

    @Slot()
    def add_schedule(self):
        # Define the path to the database file
        db_path = os.path.join(os.path.dirname(__file__), 'db')
        path_db_file = os.path.join(db_path, "database.db")
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM APPOINTMENT")
        appointments = cursor.fetchall()

        if not appointments:
            QMessageBox.information(self, "No Appointments", "No appointments available to add to the schedule.")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Add Schedule")
        dialog.setGeometry(100, 100, 400, 200)
        layout = QVBoxLayout()

        self.selectdoctor_button = QPushButton("Select Doctor", dialog)
        self.selectdoctor_button.clicked.connect(self.select_doctor)
        layout.addWidget(self.selectdoctor_button)

        self.doctor_name_label = QLabel(dialog)
        layout.addWidget(self.doctor_name_label)

        combo = QComboBox(dialog)
        for appointment in appointments:
            combo.addItem(f"Appointment {appointment[0]}: {appointment[1]} {appointment[2]} {appointment[3]}")
        layout.addWidget(combo)

        schedule_button = QPushButton("Add to Schedule", dialog)
        schedule_button.clicked.connect(lambda: self.confirm_schedule_addition(combo, dialog))
        layout.addWidget(schedule_button)

        dialog.setLayout(layout)
        dialog.exec()

    def confirm_schedule_addition(self, combo, dialog):
        selected_appointment = combo.currentText()

        # Split the appointment information to extract details
        appointment_details = selected_appointment.split(":")[1].strip().split(" ")
        appointment_id = appointment_details[0]
        appointment_date = appointment_details[1]
        appointment_time = appointment_details[2]

        # Define the path to the database file
        db_path = os.path.join(os.path.dirname(__file__), 'db')
        path_db_file = os.path.join(db_path, "database.db")
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()

        doctor_name = self.doctor_name_label.text().replace("Doctor ", "")
        cursor.execute("INSERT INTO SCHEDULE (APPOINTMENT_ID, DOCTOR_NAME, SCHEDULE_DATE, SCHEDULE_TIME) VALUES (?, ?, ?, ?)",
                       (appointment_id, doctor_name, appointment_date, appointment_time))
        connection.commit()
        connection.close()

        dialog.close()
        QMessageBox.information(self, "Schedule Added", "Schedule has been added successfully.")

if __name__ == "__main__":
    app = QApplication([])
    window = MySideBar()
    window.show()
    app.exec()