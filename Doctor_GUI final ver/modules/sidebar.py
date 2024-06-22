import os, sqlite3
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox, QCompleter, QPlainTextEdit, QLineEdit, QPushButton, QCalendarWidget
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPainter
from .ui_doctor import Ui_MainWindow
from LoginController import LoginController
from datetime import datetime

# Global variable(s)
global_path = os.path.dirname(__file__)   # Directory of the current file
parent_dir = os.path.dirname(global_path)  # Parent directory
db_path = os.path.join(parent_dir, "db") 
path_db_file = os.path.join(db_path, "database.db")

class MySideBar(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, doctor_email, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setupUi(self)
        self.ui.Menu_extend.setHidden(True)  # Initially hide the extended menu

        # Initialize label variables (after setupUi)
        self.label_username_fill = self.ui.label_username_fill 
        self.label_clinicName_fill = self.ui.label_clinicName_fill
        self.label_address_fill = self.ui.label_address_fill
        self.label_phoneNumber_fill = self.ui.label_phoneNumber_fill
        self.label_email_fill = self.ui.label_email_fill

        self.doctor_email = doctor_email
        self.setWindowTitle("Call-a-Doctor")

        # Set tables to be read-only
        self.ui.table_todaySchedule.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.list_approval.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.list_patientRecord.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableWidget_schedule.setEditTriggers(QTableWidget.NoEditTriggers)

        # Set selection behavior to select rows
        self.ui.table_todaySchedule.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.list_approval.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.list_patientRecord.setSelectionBehavior(QTableWidget.SelectRows)
        self.ui.tableWidget_schedule.setSelectionBehavior(QTableWidget.SelectRows)

        # Make diagnosis and prescription fields view-only
        self.ui.plainTextEdit_diagnosis.setReadOnly(True)
        self.ui.plainTextEdit_prescription.setReadOnly(True)

        # Connect calendar to the method that shows appointments
        self.ui.calendar_schedule.clicked.connect(self.show_appointments)

        # Initialize calendar with highlighted dates
        self.highlight_appointment_dates()

        # Connect buttons to their respective functions
        self.ui.home_btn_1.clicked.connect(self.switch_to_homePage)
        self.ui.home_btn_2.clicked.connect(self.switch_to_homePage)
        self.ui.schedule_btn_1.clicked.connect(self.switch_to_schedulePage)
        self.ui.schedule_btn_2.clicked.connect(self.switch_to_schedulePage)
        self.ui.patientPrescription_btn_1.clicked.connect(self.switch_to_patientPrescriptionPage)
        self.ui.patientPrescription_btn_2.clicked.connect(self.switch_to_patientPrescriptionPage)
        self.ui.patientRecord_btn_1.clicked.connect(self.switch_to_patientRecordPage)
        self.ui.patientRecord_btn_2.clicked.connect(self.switch_to_patientRecordPage)
        self.ui.profile_btn_1.clicked.connect(self.switch_to_profilePage)
        self.ui.profile_btn_2.clicked.connect(self.switch_to_profilePage)

        # Connect approve and reject buttons
        self.ui.approve_btn.clicked.connect(self.approve_selected)
        self.ui.reject_btn.clicked.connect(self.reject_selected)

        # Connect save button to save_patient_record function
        self.ui.btn_save.clicked.connect(self.save_patient_record)

        # For Patient Record Search functionality
        self.completer = QCompleter(self.load_patient_names())
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit_patientName.setCompleter(self.completer)
        self.ui.lineEdit_patientName_2.setCompleter(self.completer)
        self.ui.search_btn.clicked.connect(self.search_patient_records)
        self.ui.list_patientRecord.cellClicked.connect(self.select_row)
        self.ui.select_btn.clicked.connect(self.display_record_details)

        self.load_appointments()
        self.load_approvals()
        self.populate_profile_info()

    def switch_to_homePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.load_appointments()
        self.load_approvals()

    def switch_to_profilePage(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def switch_to_schedulePage(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.show_appointments(QDate.currentDate())

    def switch_to_patientRecordPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def switch_to_patientPrescriptionPage(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def load_appointments(self):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Get today's date
            today_date = QDate.currentDate().toString("dd-MM-yyyy")

            # Execute query to fetch appointments for today
            cursor.execute(
                """
                SELECT APPOINTMENT.APPOINTMENT_ID, APPOINTMENT.APPOINTMENT_DATE, APPOINTMENT.APPOINTMENT_TIME, PATIENT.PATIENT_NAME
                FROM APPOINTMENT
                JOIN PATIENT ON APPOINTMENT.PATIENT_EMAIL = PATIENT.PATIENT_EMAIL
                WHERE APPOINTMENT.APPOINTMENT_DATE = ? AND APPOINTMENT.DOCTOR_EMAIL = ?
                """,
                (today_date, self.doctor_email)
            )
            appointments = cursor.fetchall()

            # Debug print
            print("Fetched Appointments:", appointments)

            # Set table widget headers
            headers = ["Appointment ID", "Appointment Date", "Appointment Time", "Patient Name"]
            self.ui.table_todaySchedule.setColumnCount(len(headers))
            self.ui.table_todaySchedule.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.ui.table_todaySchedule.setRowCount(len(appointments))
            for row_num, row_data in enumerate(appointments):
                for col_num, data in enumerate(row_data):
                    print(f"Setting item at {row_num, col_num}: {data}")  # Debug print
                    item = QTableWidgetItem(str(data))
                    self.ui.table_todaySchedule.setItem(row_num, col_num, item)

            conn.close()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def highlight_appointment_dates(self):
        try:
            conn = sqlite3.connect(path_db_file)  # Replace with your actual database path
            cursor = conn.cursor()

            # Execute query to fetch all appointment dates
            cursor.execute("SELECT DISTINCT APPOINTMENT_DATE FROM APPOINTMENT WHERE DOCTOR_EMAIL = ?", (self.doctor_email,))
            dates = cursor.fetchall()
            conn.close()

            # Convert dates to QDate and store in a set
            self.appointment_dates = {QDate.fromString(date[0], "dd-MM-yyyy") for date in dates}

            # Override the paintCell method
            original_paint_cell = self.ui.calendar_schedule.paintCell

            def custom_paint_cell(painter, rect, date):
                if date in self.appointment_dates:
                    painter.save()
                    # Set background color without covering the date text
                    brush = painter.brush()
                    painter.setBrush(Qt.red)
                    painter.drawRect(rect)
                    painter.setBrush(brush)
                    painter.restore()

                # Call the original paintCell method to ensure the date text is drawn
                original_paint_cell(painter, rect, date)

            self.ui.calendar_schedule.paintCell = custom_paint_cell
            self.ui.calendar_schedule.updateCells()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def show_appointments(self, date):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Execute query to fetch appointments for the selected date
            cursor.execute(
                """SELECT A.APPOINTMENT_ID, A.APPOINTMENT_DATE, A.APPOINTMENT_TIME, P.PATIENT_NAME, D.DOCTOR_NAME 
                FROM APPOINTMENT A
                LEFT JOIN PATIENT P ON A.PATIENT_EMAIL = P.PATIENT_EMAIL
                LEFT JOIN DOCTORS D ON A.DOCTOR_EMAIL = D.DOCTOR_EMAIL
                WHERE A.APPOINTMENT_DATE = ? AND A.DOCTOR_EMAIL = ?""",
                (date.toString("dd-MM-yyyy"), self.doctor_email)
            )
            appointments = cursor.fetchall()
            conn.close()

            # Set table widget headers
            headers = ["Appointment ID", "Appointment Date", "Appointment Time", "Patient Name", "Doctor Name"]
            self.ui.tableWidget_schedule.setColumnCount(len(headers))
            self.ui.tableWidget_schedule.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.ui.tableWidget_schedule.setRowCount(len(appointments))
            for row_num, row_data in enumerate(appointments):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.ui.tableWidget_schedule.setItem(row_num, col_num, item)

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def load_approvals(self):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Fetch approval requests where the logged-in doctor is the receiver and status is 0
            cursor.execute("""
                SELECT A.APPROVAL_ID, D1.DOCTOR_NAME AS DOCTOR_NAME_SEND, P.PATIENT_NAME, A.RECORD_ID
                FROM PATIENT_RECORD_APPROVAL A
                LEFT JOIN DOCTORS D1 ON A.DOCTOR_EMAIL_SEND = D1.DOCTOR_EMAIL
                LEFT JOIN PATIENT P ON A.PATIENT_EMAIL = P.PATIENT_EMAIL
                WHERE A.DOCTOR_EMAIL_RECEIVED = ?
                AND A.STATUS = 0
            """, (self.doctor_email,))

            approvals = cursor.fetchall()

            self.ui.list_approval.setRowCount(0)  # Clear the table first
            headers = ["Approval ID", "Doctor Name Send", "Patient Name", "Record ID"]
            self.ui.list_approval.setColumnCount(len(headers))
            self.ui.list_approval.setHorizontalHeaderLabels(headers)

            for row_num, row_data in enumerate(approvals):
                self.ui.list_approval.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make the item non-editable
                    self.ui.list_approval.setItem(row_num, col_num, item)

            conn.close()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")


    def approve_selected(self):
        try:
            selected_rows = self.ui.list_approval.selectionModel().selectedRows()

            if not selected_rows:
                QMessageBox.warning(self, "No Selection", "No approval selected")
                return

            with sqlite3.connect(path_db_file) as conn:
                cursor = conn.cursor()

                for index in selected_rows:
                    approval_id = self.ui.list_approval.item(index.row(), 0).text()
                    cursor.execute("UPDATE PATIENT_RECORD_APPROVAL SET STATUS = 1, RESULT = 1 WHERE APPROVAL_ID = ?", (approval_id,))
                    print(f"Approved: {approval_id}")  # Debug print

                conn.commit()

                self.load_approvals()  # Refresh table data
                QMessageBox.information(self, "Success", "Selected approvals have been approved")

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def reject_selected(self):
        try:
            selected_rows = self.ui.list_approval.selectionModel().selectedRows()

            if not selected_rows:
                QMessageBox.warning(self, "No Selection", "No approval selected")
                return

            with sqlite3.connect(path_db_file) as conn:
                cursor = conn.cursor()

                for index in selected_rows:
                    approval_id = self.ui.list_approval.item(index.row(), 0).text()
                    cursor.execute("UPDATE PATIENT_RECORD_APPROVAL SET STATUS = 1, RESULT = 0 WHERE APPROVAL_ID = ?", (approval_id,))
                    print(f"Rejected: {approval_id}")  # Debug print

                conn.commit()

                self.load_approvals()  # Refresh table data
                QMessageBox.information(self, "Success", "Selected approvals have been rejected")

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def save_patient_record(self):
        # Get input values
        patient_name = self.ui.lineEdit_patientName.text().strip()
        diagnosis = self.ui.lineEdit_diagnosis.text().strip()
        prescription = self.ui.lineEdit_prescription.text().strip()

        # Check if any field is empty
        if not (patient_name and diagnosis and prescription):
            QMessageBox.warning(self, "Missing Information", "Please fill in all fields.")
            return

        try:
            # Connect to the database
            with sqlite3.connect(path_db_file) as conn:
                cursor = conn.cursor()

                # Fetch the logged-in doctor's name
                cursor.execute("SELECT DOCTOR_NAME FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (self.doctor_email,))
                doctor_name = cursor.fetchone()[0]

                # Generate current date
                record_date = datetime.now().strftime('%d-%m-%Y')

                # Insert data into PATIENT_RECORD table with current date and doctor name
                cursor.execute("""
                    INSERT INTO PATIENT_RECORD (PATIENT_EMAIL, DOCTOR_EMAIL, DIAGNOSIS, PRESCRIPTION, RECORD_DATE)
                    VALUES ((SELECT PATIENT_EMAIL FROM PATIENT WHERE PATIENT_NAME = ?), 
                            ?, ?, ?, ?)
                    """, (patient_name, self.doctor_email, diagnosis, prescription, record_date))

                # Commit the transaction
                conn.commit()

                QMessageBox.information(self, "Success", "Patient record saved successfully.")

                # Clear input fields after successful save
                self.ui.lineEdit_patientName.clear()
                self.ui.lineEdit_diagnosis.clear()
                self.ui.lineEdit_prescription.clear()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Failed to save patient record: {e}")


    def load_patient_names(self):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT PATIENT_NAME FROM PATIENT")
            patient_names = [row[0] for row in cursor.fetchall()]
            conn.close()
            return patient_names
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return []


    def search_patient_records(self):
        search_name = self.ui.lineEdit_patientName_2.text().strip()
        if not search_name:
            QMessageBox.warning(self, "Missing Information", "Please enter a patient name to search.")
            return

        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Query to fetch patient's email based on entered patient name
            cursor.execute("SELECT PATIENT_EMAIL FROM PATIENT WHERE PATIENT_NAME LIKE ?", ('%' + search_name + '%',))
            patient_email = cursor.fetchone()

            if not patient_email:
                QMessageBox.warning(self, "No Results", "No patient found with the entered name.")
                conn.close()
                return

            patient_email = patient_email[0]  # Extracting the patient_email from the tuple

            # Subquery to get the latest approval request per record and doctor
            subquery = """
            SELECT MAX(APPROVAL_ID) AS MAX_APPROVAL_ID
            FROM PATIENT_RECORD_APPROVAL
            WHERE DOCTOR_EMAIL_SEND = ?
            GROUP BY RECORD_ID
            """

            # Main query to get patient records with necessary joins
            query = f"""
            SELECT pr.RECORD_ID, p.PATIENT_NAME, d.DOCTOR_NAME, pr.RECORD_DATE,
                d.CLINIC_NAME, IFNULL(pra.RESULT, -1) AS APPROVAL_RESULT
            FROM PATIENT_RECORD pr
            JOIN PATIENT p ON pr.PATIENT_EMAIL = p.PATIENT_EMAIL
            JOIN DOCTORS d ON pr.DOCTOR_EMAIL = d.DOCTOR_EMAIL
            LEFT JOIN PATIENT_RECORD_APPROVAL pra ON pr.RECORD_ID = pra.RECORD_ID 
                                                AND pra.APPROVAL_ID IN ({subquery})
            WHERE pr.PATIENT_EMAIL = ?
            """
            
            # Execute the main query with the required parameters
            cursor.execute(query, (self.doctor_email, patient_email))
            records = cursor.fetchall()

            self.ui.list_patientRecord.setRowCount(len(records))
            headers = ["Record ID", "Patient Name", "Doctor Name", "Record Date", "Access"]
            self.ui.list_patientRecord.setColumnCount(len(headers))
            self.ui.list_patientRecord.setHorizontalHeaderLabels(headers)

            # Fetch logged-in doctor's clinic name
            cursor.execute("SELECT CLINIC_NAME FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (self.doctor_email,))
            logged_in_clinic_name = cursor.fetchone()[0]

            for row_num, row_data in enumerate(records):
                record_id, patient_name, doctor_name, record_date, clinic_name, approval_result = row_data
                
                # Determine access status
                if clinic_name == logged_in_clinic_name or approval_result == 1:
                    access_status = "accessible"
                else:
                    access_status = "unaccessible"

                # Populate the table with data
                row_data = [record_id, patient_name, doctor_name, record_date, access_status]
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make the item non-editable
                    self.ui.list_patientRecord.setItem(row_num, col_num, item)

            if not records:
                QMessageBox.information(self, "No Results", "No records found for the entered patient name.")

            conn.close()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")


    def select_row(self, row, column):
        self.ui.list_patientRecord.selectRow(row)

    def display_record_details(self):
        selected_row = self.ui.list_patientRecord.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a record to view details.")
            return

        record_id_item = self.ui.list_patientRecord.item(selected_row, 0)
        doctor_name_item = self.ui.list_patientRecord.item(selected_row, 2)
        access_status_item = self.ui.list_patientRecord.item(selected_row, 4)

        if not record_id_item or not doctor_name_item or not access_status_item:
            QMessageBox.warning(self, "Selection Error", "Selected row is invalid.")
            return

        record_id = int(record_id_item.text())
        doctor_name = doctor_name_item.text()
        access_status = access_status_item.text()

        if access_status == "accessible":
            try:
                conn = sqlite3.connect(path_db_file)
                cursor = conn.cursor()
                cursor.execute("SELECT DIAGNOSIS, PRESCRIPTION FROM PATIENT_RECORD WHERE RECORD_ID = ?", (record_id,))
                record = cursor.fetchone()
                
                if record:
                    diagnosis, prescription = record
                    self.ui.plainTextEdit_diagnosis.setPlainText(diagnosis)
                    self.ui.plainTextEdit_prescription.setPlainText(prescription)
                else:
                    QMessageBox.warning(self, "Record Error", "Record not found in the database.")
                
                conn.close()
            except sqlite3.Error as e:
                print(f"SQLite error: {e}")
                QMessageBox.critical(self, "Error", f"Database error: {e}")

        else:
            reply = QMessageBox.question(self, 'Approval Request', 
                                        f"Do you want to send an approval request to Dr. {doctor_name} to access this record?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                try:
                    conn = sqlite3.connect(path_db_file)
                    cursor = conn.cursor()

                    # Fetch patient_email for the record
                    cursor.execute("SELECT PATIENT_EMAIL FROM PATIENT_RECORD WHERE RECORD_ID = ?", (record_id,))
                    patient_email = cursor.fetchone()[0]

                    # Insert the approval request
                    cursor.execute(
                        """
                        INSERT INTO PATIENT_RECORD_APPROVAL 
                        (DOCTOR_EMAIL_RECEIVED, PATIENT_EMAIL, RECORD_ID, STATUS, DOCTOR_EMAIL_SEND) 
                        VALUES 
                        ((SELECT DOCTOR_EMAIL FROM DOCTORS WHERE DOCTOR_NAME = ?), ?, ?, 0, ?)
                        """, 
                        (doctor_name, patient_email, record_id, self.doctor_email)
                    )

                    conn.commit()
                    conn.close()

                    QMessageBox.information(self, "Request Sent", f"Approval request sent to Dr. {doctor_name}.")
                
                except sqlite3.Error as e:
                    print(f"SQLite error: {e}")
                    QMessageBox.critical(self, "Database Error", f"Failed to send approval request: {e}")


    def populate_profile_info(self):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT DOCTOR_NAME, CLINIC_NAME, DOCTOR_ADDRESS, DOCTOR_PHONENO, DOCTOR_EMAIL FROM DOCTORS WHERE DOCTOR_EMAIL = ?", (self.doctor_email,))
            profile = cursor.fetchone()

            if profile:
                # Debug print statements to verify data
                print(f"Profile fetched: {profile}")

                # Assign data to QLabel widgets
                self.ui.label_username_fill.setText(profile[0])
                self.ui.label_username_fill_2.setText(profile[0])
                self.ui.label_clinicName_fill.setText(profile[1])
                self.ui.label_clinicName_fill_2.setText(profile[1])
                self.ui.label_address_fill.setText(profile[2])
                self.ui.label_phoneNumber_fill.setText(profile[3])
                self.ui.label_email_fill.setText(profile[4])
                

            else:
                print("Profile not found for email:", self.doctor_email)

            conn.close()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")