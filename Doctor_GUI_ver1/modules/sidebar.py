import sqlite3
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from .ui_doctor import Ui_MainWindow

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.Menu_extend.setHidden(True)  # Initially hide the extended menu

        # Load data into table
        self.load_appointments()

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

    def switch_to_homePage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_schedulePage(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_patientPrescriptionPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_patientRecordPage(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_profilePage(self):
        self.stackedWidget.setCurrentIndex(4)

    def logout(self):
        QApplication.instance().quit()

    def load_appointments(self):
        try:
            conn = sqlite3.connect('Python\\Doctor_GUI\\db\\database.db')  # Replace with your actual database path
            cursor = conn.cursor()

            # Execute query to fetch appointments
            cursor.execute("SELECT APPOINTMENT_ID, APPOINTMENT_DATE, DOCTOR_NAME, PATIENT_NAME FROM APPOINTMENT")
            appointments = cursor.fetchall()

            # Print fetched data for debugging
            print("Fetched Appointments:", appointments)

            # Set table widget headers
            headers = ["Appointment ID", "Appointment Date", "Doctor Name", "Patient Name"]
            self.table_todaySchedule.setColumnCount(len(headers))
            self.table_todaySchedule.setHorizontalHeaderLabels(headers)

            # Insert data into table widget
            self.table_todaySchedule.setRowCount(len(appointments))
            for row_num, row_data in enumerate(appointments):
                for col_num, data in enumerate(row_data):
                    print(f"Setting item at {row_num}, {col_num}: {data}")  # Debug print
                    item = QTableWidgetItem(str(data))
                    self.table_todaySchedule.setItem(row_num, col_num, item)

            conn.close()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
