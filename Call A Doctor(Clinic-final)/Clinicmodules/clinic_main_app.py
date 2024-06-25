from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QComboBox, QDialog, QPushButton, QMessageBox, QApplication
from PySide6.QtCore import Slot, QTimer, Qt
import sqlite3
import os
import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from Clinicmodules.clinicUI import Ui_MainWindow

# Global variable(s)
global_path = os.path.dirname(__file__)  # Directory of the current file
parent_dir = os.path.dirname(global_path)  # Parent directory
db_path = os.path.join(parent_dir, "db")
path_db_file = os.path.join(db_path, "database.db")

# Load environment variables from the .env file
dotenv_path = os.path.join(parent_dir, 'credentials', '.env')
load_dotenv(dotenv_path)

class MySideBar(QMainWindow, Ui_MainWindow):
    __instance = None

    def __new__(cls, clinic_email, parent=None):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, clinic_email, parent=None):
        if not hasattr(self, 'ui'):
            super().__init__(parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.widget_2.setHidden(True)
            self.initial_setup(clinic_email)

    def initial_setup(self, clinic_email):
        self.clinic_email = clinic_email
        self.clinic_name = self.get_clinic_name_by_email(clinic_email)

        self.setWindowTitle("Call A Doctor")

        self.switch_to_homePage()
        self.ui.widget_2.setHidden(True)

        self.ui.home_1.clicked.connect(self.switch_to_homePage)
        self.ui.home_2.clicked.connect(self.switch_to_homePage)
        self.ui.adddoctor_1.clicked.connect(self.switch_to_addDoctorPage)
        self.ui.adddoctor_2.clicked.connect(self.switch_to_addDoctorPage)
        self.ui.shortcut_add.clicked.connect(self.switch_to_addDoctorPage)
        self.ui.viewdoctor_1.clicked.connect(self.switch_to_viewDoctorPage)
        self.ui.view_doctor_2.clicked.connect(self.switch_to_viewDoctorPage)
        self.ui.shortcut_view.clicked.connect(self.switch_to_viewDoctorPage)
        self.ui.request_1.clicked.connect(self.switch_to_RequestPage)
        self.ui.request_2.clicked.connect(self.switch_to_RequestPage)
        self.ui.shortcut_request.clicked.connect(self.switch_to_RequestPage)
        self.ui.addschedule_1.clicked.connect(self.switch_to_addSchedulePage)
        self.ui.addschedule_2.clicked.connect(self.switch_to_addSchedulePage)
        self.ui.shortcut_schedule.clicked.connect(self.switch_to_addSchedulePage)
        self.ui.confirm_button.clicked.connect(self.add_doctor)
        self.ui.delete_button.clicked.connect(self.delete_selected_doctor)

        self.load_doctors_data()

        self.schedule_table = self.findChild(QTableWidget, 'schedule_table')
        self.selectdoctor_button = self.findChild(QPushButton, 'selectdoctor_button')
        self.addschedule_button = self.findChild(QPushButton, 'addschedule_button')
        self.doctor_name_label = self.findChild(QLabel, 'doctor_name_label')

        self.selectdoctor_button.clicked.connect(self.select_doctor)
        self.addschedule_button.clicked.connect(self.add_schedule)

        self.selected_doctor_name = None

        self.patient_request_table = self.findChild(QTableWidget, 'patient_request_table')
        self.accept_request_button = self.findChild(QPushButton, 'accept_request_button')
        self.reject_request_button = self.findChild(QPushButton, 'reject_request_button')

        self.accept_request_button.clicked.connect(self.accept_selected_request)
        self.reject_request_button.clicked.connect(self.reject_selected_request)

        self.load_patient_requests_data()

        self.bring_to_front()

    def bring_to_front(self):
        QTimer.singleShot(100, self.check_visibility)

    def check_visibility(self):
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
        self.raise_()
        self.activateWindow()
        self.show()

        if not self.isVisible():
            QTimer.singleShot(100, self.check_visibility_again)

    def check_visibility_again(self):
        self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
        self.raise_()
        self.activateWindow()
        self.show()

    def get_clinic_name_by_email(self, email):
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT CLINIC_NAME FROM CLINICS WHERE EMAIL = ?", (email,))
        row = cursor.fetchone()
        connection.close()
        return row[0] if row else ""

    def switch_to_homePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_addDoctorPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_viewDoctorPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.load_doctors_data()

    def switch_to_RequestPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.load_patient_requests_data()

    def switch_to_addSchedulePage(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def load_doctors_data(self):
        if not os.path.exists(path_db_file):
            return

        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT DOCTOR_EMAIL, DOCTOR_NAME, DOCTOR_PHONENO, DOCTOR_ADDRESS FROM DOCTORS WHERE CLINIC_NAME = ?", (self.clinic_name,))
        rows = cursor.fetchall()

        self.ui.doctor_table.setRowCount(len(rows))
        self.ui.doctor_table.setColumnCount(4)
        headers = ["Doctor's Email", "Doctor's Name", "Doctor's Phone Number", "Doctor's Address"]
        self.ui.doctor_table.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.ui.doctor_table.setItem(row_idx, col_idx, QTableWidgetItem(col_data))

        connection.close()

    def load_patient_requests_data(self):
        if not os.path.exists(path_db_file):
            return

        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT PATIENT_REQUEST_ID, PATIENT_EMAIL, APPOINTMENT_DATE, APPOINTMENT_TIME FROM PATIENT_REQUEST WHERE CLINIC_NAME = ? AND APPROVAL IS NULL", (self.clinic_name,))
        rows = cursor.fetchall()

        if not self.ui.patient_request_table.isVisible():
            return

        self.ui.patient_request_table.setRowCount(len(rows))
        self.ui.patient_request_table.setColumnCount(4)
        headers = ["Request ID", "Patient Email", "Date", "Time"]
        self.ui.patient_request_table.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.ui.patient_request_table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        connection.close()

    @Slot()
    def delete_selected_doctor(self):
        selected_row = self.ui.doctor_table.currentRow()
        if selected_row >= 0:
            doctor_email = self.ui.doctor_table.item(selected_row, 0).text()
            connection = sqlite3.connect(path_db_file)
            cursor = connection.cursor()
            cursor.execute("DELETE FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (doctor_email,))
            cursor.execute("DELETE FROM KEY_LIST WHERE ASSIGNED_TO_EMAIL = ?", (doctor_email,))
            connection.commit()
            connection.close()
            self.ui.doctor_table.removeRow(selected_row)
            self.show_message("Doctor Deleted", "Doctor deleted successfully.", self)
        else:
            self.show_no_selection_message(self)

    def show_no_selection_message(self, parent):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("No Selection")
        msg_box.setText("No row selected. Please select a row to delete.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def show_message(self, title, message, parent):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def generate_activation_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    def send_approved_email(self, email, activation_code):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        email_address = os.getenv('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')
        email_password = os.getenv('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')

        if not email_address or not email_password:
            self.show_message("Email Error", "Email credentials are not set in the environment variables.", self)
            return

        subject = 'Account Approved'
        body = f'Your account has been approved. Your activation code is {activation_code}.'
        message = MIMEMultipart()
        message['From'] = email_address
        message['To'] = email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, email, message.as_string())
            server.quit()
        except Exception as e:
            print(f'Failed to send email: {e}')

    @Slot()
    def add_doctor(self):
        doctor_email = self.ui.doc_mail_edit.text().lower()
        doctor_name = self.ui.doc_name_edit.text()
        doctor_phone = self.ui.doc_phone_edit.text()
        doctor_address = self.ui.doc_add_edit.text()

        if not (doctor_email and doctor_name and doctor_phone and doctor_address):
            self.show_message("Error", "All fields must be filled out.", self)
            return

        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()

        # Check if the doctor email already exists
        cursor.execute("SELECT COUNT(*) FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (doctor_email,))
        if cursor.fetchone()[0] > 0:
            self.show_message("Error", "Email used. Please try another email.", self)
            connection.close()
            return

        activation_code = self.generate_activation_code()
        cursor.execute("INSERT INTO DOCTORS (DOCTOR_EMAIL, DOCTOR_NAME, DOCTOR_PHONENO, DOCTOR_ADDRESS, CLINIC_NAME) VALUES (?, ?, ?, ?, ?)", (doctor_email, doctor_name, doctor_phone, doctor_address, self.clinic_name))
        connection.commit()
        cursor.execute("INSERT INTO KEY_LIST (ACTIVATION_CODE, ASSIGNED_TO_EMAIL, ACTIVATION_STATUS) VALUES (?, ?, 'Not Activated')", (activation_code, doctor_email))
        connection.commit()
        connection.close()

        self.send_approved_email(doctor_email, activation_code)
        self.show_message("Success", "Doctor added successfully.", self)
        self.ui.doc_mail_edit.clear()
        self.ui.doc_name_edit.clear()
        self.ui.doc_phone_edit.clear()
        self.ui.doc_add_edit.clear()

    @Slot()
    def select_doctor(self):
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT DOCTOR_NAME FROM DOCTORS WHERE CLINIC_NAME = ?", (self.clinic_name,))
        rows = cursor.fetchall()
        connection.close()

        if not rows:
            self.show_no_doctors_message(self)
            return

        combo = QComboBox()
        combo.addItems([row[0] for row in rows])

        dialog = QDialog(self)
        dialog.setWindowTitle("Select Doctor")
        dialog.resize(150, 100)
        layout = QVBoxLayout()
        layout.addWidget(combo)
        button = QPushButton("Select")
        layout.addWidget(button)
        dialog.setLayout(layout)
        button.clicked.connect(lambda: self.set_selected_doctor(combo, dialog))
        dialog.exec()

    def show_no_doctors_message(self, parent):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("No Doctors Available")
        msg_box.setText("There are no doctors available for selection.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def set_selected_doctor(self, combo, dialog):
        self.selected_doctor_name = combo.currentText()
        self.ui.doctor_name_label.setText(f"Doctor: {self.selected_doctor_name}")
        dialog.accept()
        self.display_schedule()

    def display_schedule(self):
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        
        # Retrieve the doctor's email using the selected doctor's name
        cursor.execute("SELECT DOCTOR_EMAIL FROM DOCTORS WHERE DOCTOR_NAME = ? AND CLINIC_NAME = ?", (self.selected_doctor_name, self.clinic_name))
        doctor_email_row = cursor.fetchone()
        if doctor_email_row:
            doctor_email = doctor_email_row[0]
        else:
            self.show_message("Error", "Doctor email not found.", self)
            connection.close()
            return

        # Fetch the schedule using the doctor's email
        cursor.execute("SELECT APPOINTMENT_DATE, PATIENT_EMAIL, APPOINTMENT_TIME FROM APPOINTMENT WHERE DOCTOR_EMAIL = ?", (doctor_email,))
        rows = cursor.fetchall()
        connection.close()

        self.ui.schedule_table.setRowCount(len(rows))
        self.ui.schedule_table.setColumnCount(3)
        headers = ["Date", "Patient Email", "Time"]
        self.ui.schedule_table.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                self.ui.schedule_table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def add_schedule(self):
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT PATIENT_REQUEST_ID, PATIENT_EMAIL, APPOINTMENT_DATE, APPOINTMENT_TIME FROM PATIENT_REQUEST WHERE APPROVAL = 1 AND CLINIC_NAME = ?", (self.clinic_name,))
        rows = cursor.fetchall()

        if not rows:
            self.show_no_request_available_message(self)
            return

        dialog = QDialog(self)
        dialog.setWindowTitle("Select Appointment Request")
        layout = QVBoxLayout()
        combo = QComboBox()
        for row in rows:
            combo.addItem(f"{row[2]} - {row[1]} at {row[3]}", userData=row)
        layout.addWidget(combo)
        button = QPushButton("Add Schedule")
        layout.addWidget(button)
        dialog.setLayout(layout)
        button.clicked.connect(lambda: self.save_schedule(combo, dialog))
        dialog.exec()

    def show_no_request_available_message(self, parent):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("No Request Available")
        msg_box.setText("No approved requests available.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def save_schedule(self, combo, dialog):
        selected_data = combo.currentData()
        request_id, patient_email, date, time = selected_data
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        
        # Retrieve the doctor's email using the selected doctor's name
        cursor.execute("SELECT DOCTOR_EMAIL FROM DOCTORS WHERE DOCTOR_NAME = ? AND CLINIC_NAME = ?", (self.selected_doctor_name, self.clinic_name))
        doctor_email_row = cursor.fetchone()
        if doctor_email_row:
            doctor_email = doctor_email_row[0]
        else:
            self.show_message("Error", "Doctor email not found.", self)
            connection.close()
            return
        
        # Insert the schedule into the APPOINTMENT table
        cursor.execute("INSERT INTO APPOINTMENT (APPOINTMENT_DATE, PATIENT_EMAIL, DOCTOR_EMAIL, APPOINTMENT_TIME) VALUES (?, ?, ?, ?)", (date, patient_email, doctor_email, time))
        connection.commit()
        
        # Update the approval status of the patient request
        cursor.execute("UPDATE PATIENT_REQUEST SET APPROVAL = 2 WHERE PATIENT_REQUEST_ID = ?", (request_id,))
        connection.commit()
        
        connection.close()
        dialog.accept()
        self.display_schedule()

    @Slot()
    def accept_selected_request(self):
        selected_row = self.ui.patient_request_table.currentRow()
        if selected_row >= 0:
            request_id = self.ui.patient_request_table.item(selected_row, 0).text()
            connection = sqlite3.connect(path_db_file)
            cursor = connection.cursor()
            cursor.execute("UPDATE PATIENT_REQUEST SET APPROVAL = 1 WHERE PATIENT_REQUEST_ID = ?", (request_id,))
            connection.commit()
            connection.close()
            self.load_patient_requests_data()
            self.send_approval_email(request_id, approved=True)
            self.show_message("Request Approved", "Patient request approved and email sent.", self)
        else:
            self.show_no_request_selected_message(self)

    @Slot()
    def reject_selected_request(self):
        selected_row = self.ui.patient_request_table.currentRow()
        if selected_row >= 0:
            request_id = self.ui.patient_request_table.item(selected_row, 0).text()
            connection = sqlite3.connect(path_db_file)
            cursor = connection.cursor()
            cursor.execute("UPDATE PATIENT_REQUEST SET APPROVAL = 0 WHERE PATIENT_REQUEST_ID = ?", (request_id,))
            connection.commit()
            connection.close()
            self.load_patient_requests_data()
            self.send_approval_email(request_id, approved=False)
            self.show_message("Request Rejected", "Patient request rejected and email sent.", self)
        else:
            self.show_no_request_selected_message(self)

    def show_no_request_selected_message(self, parent):
        msg_box = QMessageBox(parent)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle("No Selection")
        msg_box.setText("No request selected. Please select a request.")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def send_approval_email(self, request_id, approved):
        connection = sqlite3.connect(path_db_file)
        cursor = connection.cursor()
        cursor.execute("SELECT PATIENT_EMAIL, APPOINTMENT_DATE, APPOINTMENT_TIME FROM PATIENT_REQUEST WHERE PATIENT_REQUEST_ID = ?", (request_id,))
        request_data = cursor.fetchone()
        connection.close()

        if request_data:
            patient_email, appointment_date, appointment_time = request_data
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            sender_email = os.getenv('PYTHON_BACKEND_SENDER_EMAIL_CREDENTIALS')
            sender_password = os.getenv('PYTHON_BACKEND_SENDER_PASSWORD_CREDENTIALS')

            if not sender_email or not sender_password:
                self.show_message("Email Error", "Email credentials are not set in the environment variables.", self)
                return

            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(sender_email, sender_password)

                if approved:
                    subject = 'Appointment Approved'
                    body = f"""<html>
                                <body>
                                    <p>Your appointment on {appointment_date} at {appointment_time} at {self.clinic_name} has been approved.</p>
                                    <p>Thank you.</p>
                                </body>
                            </html>"""
                else:
                    subject = 'Appointment Rejected'
                    body = f"""<html>
                                <body>
                                    <p>Your appointment on {appointment_date} at {appointment_time} at {self.clinic_name} has been rejected.</p>
                                    <p>Please contact the clinic for further assistance.</p>
                                </body>
                            </html>"""

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = patient_email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'html'))

                server.sendmail(sender_email, patient_email, msg.as_string())
                server.quit()

            except Exception as e:
                print(f"Error sending email: {e}")