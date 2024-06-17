import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox, QCompleter, QPlainTextEdit, QLineEdit, QPushButton, QCalendarWidget
from PySide6.QtCore import QDate, Qt
from PySide6.QtGui import QPainter
from .ui_doctor import Ui_MainWindow
from datetime import datetime


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.Menu_extend.setHidden(True)  # Initially hide the extended menu

        # Set tables to be read-only
        self.table_todaySchedule.setEditTriggers(QTableWidget.NoEditTriggers)
        self.list_approval.setEditTriggers(QTableWidget.NoEditTriggers)
        self.list_patientRecord.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_schedule.setEditTriggers(QTableWidget.NoEditTriggers)

        # Set selection behavior to select rows
        self.table_todaySchedule.setSelectionBehavior(QTableWidget.SelectRows)
        self.list_approval.setSelectionBehavior(QTableWidget.SelectRows)
        self.list_patientRecord.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget_schedule.setSelectionBehavior(QTableWidget.SelectRows)

        # Make diagnosis and prescription fields view-only
        self.plainTextEdit_diagnosis.setReadOnly(True)
        self.plainTextEdit_prescription.setReadOnly(True)

        # Connect calendar to the method that shows appointments
        self.calendar_schedule.clicked.connect(self.show_appointments)

        # Initialize calendar with highlighted dates
        self.highlight_appointment_dates()

        # Connect buttons to their respective functions
        self.home_btn_1.clicked.connect(self.switch_to_homePage)
        self.home_btn_2.clicked.connect(self.switch_to_homePage)
        self.schedule_btn_1.clicked.connect(self.switch_to_schedulePage)
        self.schedule_btn_2.clicked.connect(self.switch_to_schedulePage)
        self.patientPrescription_btn_1.clicked.connect(self.switch_to_patientPrescriptionPage)
        self.patientPrescription_btn_2.clicked.connect(self.switch_to_patientPrescriptionPage)
        self.patientRecord_btn_1.clicked.connect(self.switch_to_patientRecordPage)
        self.patientRecord_btn_2.clicked.connect(self.switch_to_patientRecordPage)
        self.profile_btn_1.clicked.connect(self.switch_to_profilePage)
        self.profile_btn_2.clicked.connect(self.switch_to_profilePage)
        self.logout_btn_1.clicked.connect(self.logout)
        self.logout_btn_2.clicked.connect(self.logout)

        # Connect approve and reject buttons
        self.approve_btn.clicked.connect(self.approve_selected)
        self.reject_btn.clicked.connect(self.reject_selected)

        # Connect save button to save_patient_record function
        self.btn_save.clicked.connect(self.save_patient_record)

        # For Patient Record Search functionality
        self.completer = QCompleter(self.load_patient_names())
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.lineEdit_patientName_2.setCompleter(self.completer)
        self.search_btn.clicked.connect(self.search_patient_records)
        self.list_patientRecord.cellClicked.connect(self.select_row)
        self.select_btn.clicked.connect(self.display_record_details)

        self.load_appointments()
        self.load_approvals()

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_profilePage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_schedulePage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.show_appointments(QDate.currentDate())

    def switch_to_patientRecordPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_patientPrescriptionPage(self):
        self.stackedWidget.setCurrentIndex(4)

    def logout(self):
        QApplication.instance().quit()

    def load_appointments(self):
        try:
            conn = sqlite3.connect('Python/Doctor_GUI/db/database.db')
            cursor = conn.cursor()

            # Get today's date
            today_date = QDate.currentDate().toString("dd-MM-yyyy")

            # Execute query to fetch appointments for today
            cursor.execute(
                "SELECT APPOINTMENT_ID, APPOINTMENT_DATE, APPOINTMENT_TIME, PATIENT_NAME FROM APPOINTMENT WHERE APPOINTMENT_DATE = ?",
                (today_date,)
            )
            appointments = cursor.fetchall()

            # Debug print
            print("Fetched Appointments:", appointments)

            # Set table widget headers
            headers = ["Appointment ID", "Appointment Date", "Appointment Time", "Patient Name"]
            self.table_todaySchedule.setColumnCount(len(headers))
            self.table_todaySchedule.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.table_todaySchedule.setRowCount(len(appointments))
            for row_num, row_data in enumerate(appointments):
                for col_num, data in enumerate(row_data):
                    print(f"Setting item at {row_num, col_num}: {data}")  # Debug print
                    item = QTableWidgetItem(str(data))
                    self.table_todaySchedule.setItem(row_num, col_num, item)

            conn.close()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def highlight_appointment_dates(self):
        try:
            conn = sqlite3.connect('Python/Doctor_GUI/db/database.db')  # Replace with your actual database path
            cursor = conn.cursor()

            # Execute query to fetch all appointment dates
            cursor.execute("SELECT DISTINCT APPOINTMENT_DATE FROM APPOINTMENT")
            dates = cursor.fetchall()
            conn.close()

            # Convert dates to QDate and store in a set
            self.appointment_dates = {QDate.fromString(date[0], "dd-MM-yyyy") for date in dates}

            # Override the paintCell method
            original_paint_cell = self.calendar_schedule.paintCell

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

            self.calendar_schedule.paintCell = custom_paint_cell
            self.calendar_schedule.updateCells()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def show_appointments(self, date):
        try:
            conn = sqlite3.connect('Python/Doctor_GUI/db/database.db')
            cursor = conn.cursor()

            # Execute query to fetch appointments for the selected date
            cursor.execute(
                "SELECT APPOINTMENT_ID, APPOINTMENT_DATE, APPOINTMENT_TIME, PATIENT_NAME, DOCTOR_NAME FROM APPOINTMENT WHERE APPOINTMENT_DATE = ?",
                (date.toString("dd-MM-yyyy"),)
            )
            appointments = cursor.fetchall()
            conn.close()

            # Set table widget headers
            headers = ["Appointment ID", "Appointment Date", "Appointment Time", "Patient Name", "Doctor Name"]
            self.tableWidget_schedule.setColumnCount(len(headers))
            self.tableWidget_schedule.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.tableWidget_schedule.setRowCount(len(appointments))
            for row_num, row_data in enumerate(appointments):
                for col_num, data in enumerate(row_data):
                    item = QTableWidgetItem(str(data))
                    self.tableWidget_schedule.setItem(row_num, col_num, item)

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def load_approvals(self):
        try:
            conn = sqlite3.connect('Python/Doctor_GUI/db/database.db')
            cursor = conn.cursor()

            # Execute query to fetch patient record approvals where status is 0
            cursor.execute("SELECT APPROVAL_ID, DOCTOR_NAME, PATIENT_NAME, RECORD_ID FROM PATIENT_RECORD_APPROVAL WHERE STATUS = 0")
            approvals = cursor.fetchall()

            # Debug print
            print("Fetched Approvals:", approvals)

            # Set table widget headers
            headers = ["Approval ID", "Doctor Name", "Patient Name", "Record ID"]
            self.list_approval.setColumnCount(len(headers))
            self.list_approval.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.list_approval.setRowCount(len(approvals))
            for row_num, row_data in enumerate(approvals):
                for col_num, data in enumerate(row_data):
                    print(f"Setting item at {row_num}, {col_num}: {data}")  # Debug print
                    item = QTableWidgetItem(str(data))
                    self.list_approval.setItem(row_num, col_num, item)

            conn.close()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")


    def approve_selected(self):
        try:
            selected_rows = self.list_approval.selectionModel().selectedRows()

            if not selected_rows:
                QMessageBox.warning(self, "No Selection", "No approval selected")
                return

            with sqlite3.connect('Python\\Doctor_GUI\\db\\database.db') as conn:
                cursor = conn.cursor()

                for index in selected_rows:
                    approval_id = self.list_approval.item(index.row(), 0).text()
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
            selected_rows = self.list_approval.selectionModel().selectedRows()

            if not selected_rows:
                QMessageBox.warning(self, "No Selection", "No approval selected")
                return

            with sqlite3.connect('Python\\Doctor_GUI\\db\\database.db') as conn:
                cursor = conn.cursor()

                for index in selected_rows:
                    approval_id = self.list_approval.item(index.row(), 0).text()
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
        patient_name = self.lineEdit_patientName.text().strip()
        diagnosis = self.lineEdit_diagnosis.text().strip()
        prescription = self.lineEdit_prescription.text().strip()

        # Check if any field is empty
        if not (patient_name and diagnosis and prescription):
            QMessageBox.warning(self, "Missing Information", "Please fill in all fields.")
            return

        try:
            # Connect to the database
            with sqlite3.connect('Python\\Doctor_GUI\\db\\database.db') as conn:
                cursor = conn.cursor()

                # Generate current date
                record_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Insert data into PATIENT_RECORD table with current date
                cursor.execute("INSERT INTO PATIENT_RECORD (PATIENT_NAME, DOCTOR_NAME, DIAGNOSIS, PRESCRIPTION, RECORD_DATE) VALUES (?, ?, ?, ?, ?)",
                            (patient_name, "Current Doctor Name", diagnosis, prescription, record_date))

                # Commit the transaction
                conn.commit()

                QMessageBox.information(self, "Success", "Patient record saved successfully.")

                # Clear input fields after successful save
                self.lineEdit_patientName.clear()
                self.lineEdit_diagnosis.clear()
                self.lineEdit_prescription.clear()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Failed to save patient record: {e}")

    def load_patient_names(self):
        try:
            conn = sqlite3.connect('Python\\Doctor_GUI\\db\\database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT PATIENT_NAME FROM PATIENT_RECORD")
            patient_names = [row[0] for row in cursor.fetchall()]
            conn.close()
            return patient_names
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return []

    def search_patient_records(self):
        search_name = self.lineEdit_patientName_2.text().strip()
        if not search_name:
            QMessageBox.warning(self, "Missing Information", "Please enter a patient name to search.")
            return

        try:
            conn = sqlite3.connect('Python\\Doctor_GUI\\db\\database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT RECORD_ID, PATIENT_NAME, DOCTOR_NAME, RECORD_DATE, DIAGNOSIS, PRESCRIPTION FROM PATIENT_RECORD WHERE PATIENT_NAME LIKE ?", ('%' + search_name + '%',))
            records = cursor.fetchall()

            self.list_patientRecord.setRowCount(len(records))
            headers = ["Record ID", "Patient Name", "Doctor Name", "Record Date"]
            self.list_patientRecord.setColumnCount(len(headers))
            self.list_patientRecord.setHorizontalHeaderLabels(headers)

            for row_num, row_data in enumerate(records):
                for col_num, data in enumerate(row_data[:4]):
                    item = QTableWidgetItem(str(data))
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make the item non-editable
                    self.list_patientRecord.setItem(row_num, col_num, item)

            self.patient_records = records

            if not records:
                QMessageBox.information(self, "No Results", "No records found for the entered patient name.")

            conn.close()
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            QMessageBox.critical(self, "Error", f"Database error: {e}")

    def select_row(self, row, column):
        self.list_patientRecord.selectRow(row)

    def display_record_details(self):
        selected_row = self.list_patientRecord.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a record first.")
            return

        diagnosis = self.patient_records[selected_row][4]
        prescription = self.patient_records[selected_row][5]

        self.plainTextEdit_diagnosis.setPlainText(diagnosis)
        self.plainTextEdit_prescription.setPlainText(prescription)
