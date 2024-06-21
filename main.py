import sys
import webbrowser
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QFont
from ui import Ui_MainWindow
from datetime import datetime, time, timedelta
from PyQt5.QtCore import QDate

def create_connection():
    """Create a connection to the SQLite database."""
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('database.db')  # Replace with your actual database file name

    if not db.open():
        QMessageBox.critical(None, 'Database Error', 'Could not open database.')
        sys.exit(1)

    return db

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initial_load = True  # Flag to track initial population
        self.ui.dateEdit.setMinimumDate(QDate.currentDate())
        self.ui.dateEdit.setMaximumDate(QDate.currentDate().addYears(1))
        self.holiday_dates = ["2024-12-25", "2024-01-01", "2024-07-04"]

        # Connect buttons to functions
        self.ui.sidebar.setHidden(True)
        self.ui.home_btn.clicked.connect(self.switch_to_homePage)
        self.ui.home_btn_2.clicked.connect(self.switch_to_homePage)
        self.ui.profile_btn.clicked.connect(self.switch_to_profilePage)
        self.ui.profile_btn_2.clicked.connect(self.switch_to_profilePage)
        self.ui.record_btn.clicked.connect(self.switch_to_recordPage)
        self.ui.record_btn_2.clicked.connect(self.switch_to_recordPage)
        self.ui.search_btn.clicked.connect(self.switch_to_searchPage)
        self.ui.search_btn_2.clicked.connect(self.switch_to_searchPage)
        self.ui.back_btn.clicked.connect(self.switch_to_searchPage)
        self.ui.request_btn.clicked.connect(self.switch_to_requestPage)
        self.ui.request_btn_2.clicked.connect(self.switch_to_requestPage)

        self.ui.searchlinic_btn_6.clicked.connect(self.search_clinics)
        self.ui.location_combobox.currentIndexChanged.connect(self.search_clinics)
        self.populate_location_combobox()
        self.populate_clinic_combobox()
        self.ui.editprofile_btn_2.clicked.connect(self.toggle_edit_profile)
        self.ui.requestdoctor_btn.clicked.connect(self.submit_doctor_request)

        # Create database connection and tables
        self.db = create_connection()
        print("Database connection established and tables created.")

        # Initialize search page
        self.populate_search_table(show_message=False)
    def determine_package(self, date_str, time_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        time_obj = datetime.strptime(time_str, "%H:%M:%S").time()

        # Check if the selected date is a holiday
        if date_str in self.holiday_dates:
            return "Holiday"

        # Check the time for Day or Night package
        if time(8, 0) <= time_obj < time(20, 0):
            return "Day"
        else:
            return "Night"

    def submit_doctor_request(self):
        clinic_name = self.ui.clinic_combobox.currentText()
        date = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        time = self.ui.timeEdit.time().toString("HH:mm:ss")

        # Validate the date is not today
        current_date = QtCore.QDate.currentDate()
        selected_date = self.ui.dateEdit.date()
        current_time = QtCore.QTime.currentTime()
        selected_time = self.ui.timeEdit.time()

        if selected_date < current_date:
            QMessageBox.warning(self, 'Validation Error', 'The date cannot be in the past.')
            return

        if selected_date == current_date and selected_time < current_time:
            QMessageBox.warning(self, 'Validation Error', 'The time cannot be in the past or today.')
            return

        # Validate the clinic selection
        if clinic_name == "Choose Clinic":
            QMessageBox.warning(self, 'Validation Error', 'Please select a valid clinic.')
            return

        # Determine the package
        package = self.determine_package(date, time)

        # Insert the request into the database
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO PATIENT_REQUEST (DATE, TIME, PACKAGE, CLINIC_NAME, PATIENT_EMAIL)
            VALUES (?, ?, ?, ?, ?)
        """)

        query.addBindValue(date)
        query.addBindValue(time)
        query.addBindValue(package)
        query.addBindValue(clinic_name)
        query.addBindValue("stevenblindmonk@hotmail.com")  # Use the actual patient email

        print(
            f"Submitting request: date={date}, time={time}, package={package}, clinic_name={clinic_name}, patient_email='stevenblindmonk@hotmail.com'")

        if not query.exec_():
            error = query.lastError().text()
            QMessageBox.critical(self, 'Database Error', f'Failed to submit the doctor request. Error: {error}')
            print(f'Database Error: {error}')
            return

        success_message = f'''
            Your doctor request has been successfully submitted with the following details:
            - Clinic: {clinic_name}
            - Date: {date}
            - Time: {time}
            - Package: {package}
        '''
        QMessageBox.information(self, 'Success', success_message)
        print(f'Success: {success_message}')

    def populate_record_table(self):
        # Clear the existing rows and columns
        self.ui.record_table.clear()
        self.ui.record_table.setRowCount(0)
        self.ui.record_table.setColumnCount(4)  # Set the number of columns (excluding RECORD_ID and PATIENT_EMAIL)
        self.ui.record_table.setHorizontalHeaderLabels(['Doctor Name', 'Diagnosis', 'Prescription', 'Record Date'])
        self.ui.record_table.setStyleSheet("""
                QTableWidget {
                    background-color: rgb(255, 255, 255);
                    alternate-background-color: rgb(229, 229, 241);
                    gridline-color: rgb(200, 200, 200);
                    font: 12pt "Bell MT";
                }
                QHeaderView::section {
                    background-color: rgb(229, 229, 241);
                    border: 1px solid rgb(200, 200, 200);
                    font: bold 14pt "Bell MT";
                }
                QTableWidget::item {
                    padding: 5px;
                }
                QTableWidget::item:selected {
                    background-color: rgb(85, 170, 255);
                    color: white;
                }
                QTableWidget::item:hover {
                    background-color: rgb(85, 170, 255);
                    color: white;
                }
            """)

        # Query to fetch data from the PATIENT_RECORD table for the given email
        query = QSqlQuery()
        query.prepare("""
            SELECT DOCTOR_NAME, DIAGNOSIS, PRESCRIPTION, RECORD_DATE 
            FROM PATIENT_RECORD 
            WHERE PATIENT_EMAIL = ?
        """)
        query.addBindValue("stevenblindmonk@hotmail.com")
        query.exec_()

        # Populate the table with the query results
        row = 0
        while query.next():
            self.ui.record_table.insertRow(row)
            for col in range(4):  # Loop through the 4 columns (excluding RECORD_ID and PATIENT_EMAIL)
                item = QTableWidgetItem(query.value(col))
                self.ui.record_table.setItem(row, col, item)
            row += 1

    def populate_clinic_combobox(self):
        self.ui.clinic_combobox.clear()  # Clear existing items
        self.ui.clinic_combobox.addItem("Choose Clinic")  # Add the prompt item

        query = QSqlQuery()
        query.exec_("SELECT CLINIC_NAME FROM CLINICS")

        while query.next():
            clinic_name = query.value(0)
            self.ui.clinic_combobox.addItem(clinic_name)

    def switch_to_homePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_profilePage(self):
        user_email = "stevenblindmonk@hotmail.com"  # Replace with the actual email or retrieve it dynamically
        user_info = self.retrieve_user_info(user_email)

        if user_info:
            self.ui.username_edit_2.setPlainText(user_info["name"])
            self.ui.userEmail_edit_2.setPlainText(user_info["email"])
            self.ui.nric_edit_2.setPlainText(user_info["ic"])
            self.ui.phone_edit_2.setPlainText(user_info["phone"])
            self.ui.address_edit_2.setPlainText(user_info["address"])
        else:
            QMessageBox.warning(self, 'User Not Found', 'The user information could not be found.')
        self.enable_profile_editing(False)
        self.ui.editprofile_btn_2.setText("Edit")
        self.ui.stackedWidget.setCurrentIndex(4)

    def enable_profile_editing(self, enable):
        self.ui.username_edit_2.setReadOnly(not enable)
        self.ui.userEmail_edit_2.setReadOnly(not enable)
        self.ui.nric_edit_2.setReadOnly(not enable)
        self.ui.phone_edit_2.setReadOnly(not enable)
        self.ui.address_edit_2.setReadOnly(not enable)

    def toggle_edit_profile(self):
        if self.ui.editprofile_btn_2.text() == "Edit":
            self.enable_profile_editing(True)
            self.ui.editprofile_btn_2.setText("Save")
            QMessageBox.information(self, 'Edit Mode',
                                    'You can now edit your profile information. Click Save when you are done.')
        else:
            if self.save_profile_changes():
                self.enable_profile_editing(False)
                self.ui.editprofile_btn_2.setText("Edit")
                QMessageBox.information(self, 'Success', 'Your profile information has been successfully updated.')

    def save_profile_changes(self):
        name = self.ui.username_edit_2.toPlainText()
        email = self.ui.userEmail_edit_2.toPlainText()
        nric = self.ui.nric_edit_2.toPlainText()
        phone = self.ui.phone_edit_2.toPlainText()
        address = self.ui.address_edit_2.toPlainText()

        if not self.is_valid_email(email):
            QMessageBox.warning(self, 'Validation Error', 'Invalid email format.')
            return False

        if not self.is_valid_phone(phone):
            QMessageBox.warning(self, 'Validation Error', 'Invalid phone number format.')
            return False

        if self.check_duplicate("PATIENT_EMAIL", email) or self.check_duplicate("PATIENT_IC", nric) or self.check_duplicate("PATIENT_PHONENO", phone):
            QMessageBox.warning(self, 'Validation Error', 'Duplicate NRIC, phone number, or email found in the database.')
            return False

        query = QSqlQuery()
        query.prepare("""
            UPDATE PATIENT
            SET PATIENT_NAME = ?, PATIENT_EMAIL = ?, PATIENT_IC = ?, PATIENT_PHONENO = ?, PATIENT_ADDRESS = ?
            WHERE PATIENT_EMAIL = ?
        """)
        query.addBindValue(name)
        query.addBindValue(email)
        query.addBindValue(nric)
        query.addBindValue(phone)
        query.addBindValue(address)
        query.addBindValue("stevenblindmonk@hotmail.com")  # Current user's email

        if not query.exec_():
            QMessageBox.critical(self, 'Database Error', 'Failed to update the user information.')
            return False

        return True

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def is_valid_phone(self, phone):
        phone_regex = r'^\d{10,15}$'
        return re.match(phone_regex, phone) is not None
    def check_duplicate(self, column, value):
        query = QSqlQuery()
        query.prepare(f"SELECT COUNT(*) FROM PATIENT WHERE {column} = ? AND PATIENT_EMAIL != ?")
        query.addBindValue(value)
        query.addBindValue("stevenblindmonk@hotmail.com")  # Current user's email
        query.exec_()

        if query.next() and query.value(0) > 0:
            return True

    def switch_to_recordPage(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.populate_record_table()

    def switch_to_requestPage(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_searchPage(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.reset_search_fields()  # Reset the search fields when switching to the search page
        self.populate_search_table(show_message=False)  # Populate the table without showing a message

    def reset_search_fields(self):
        self.ui.search_lineedit_6.setText("")
        self.ui.location_combobox.setCurrentIndex(0)

    def populate_location_combobox(self):
        # Add locations to the combobox
        locations = ["All Locations", "Bayan Lepas", "Jelutong"]  # Add your locations here
        self.ui.location_combobox.addItems(locations)

    def search_clinics(self):
        search_text = self.ui.search_lineedit_6.text()
        selected_location = self.ui.location_combobox.currentText()
        self.populate_search_table(search_text, selected_location, show_message=True)

    def populate_search_table(self, search_text="", selected_location="All Locations", show_message=True):
        query = QSqlQuery()

        base_query = "SELECT CLINIC_NAME, CLINIC_ADDRESS FROM CLINICS"
        conditions = []

        if search_text:
            conditions.append("CLINIC_NAME LIKE ?")
        if selected_location != "All Locations":
            conditions.append("CLINIC_ADDRESS LIKE ?")

        if conditions:
            query_string = f"{base_query} WHERE {' AND '.join(conditions)}"
        else:
            query_string = base_query

        query.prepare(query_string)

        if search_text:
            query.addBindValue(f"%{search_text}%")
        if selected_location != "All Locations":
            query.addBindValue(f"%{selected_location}%")

        query.exec_()

        self.ui.search_table.setRowCount(0)  # Clear existing rows
        self.ui.search_table.setColumnCount(3)  # Set column count to 3 (Clinic Name, Clinic Address, View Detail)
        self.ui.search_table.setHorizontalHeaderLabels(['Clinic Name', 'Clinic Address', 'View Detail'])
        self.ui.search_table.setStyleSheet("""
        QTableWidget {
            background-color: rgb(255, 255, 255);
            alternate-background-color: rgb(229, 229, 241);
            gridline-color: rgb(200, 200, 200);
            font: 12pt "Bell MT";
        }
        QHeaderView::section {
            background-color: rgb(229, 229, 241);
            border: 1px solid rgb(200, 200, 200);
            font: bold 14pt "Bell MT";
        }
        QTableWidget::item {
            padding: 5px;
        }
        QTableWidget::item:selected {
            background-color: rgb(85, 170, 255);
            color: white;
        }
        QTableWidget::item:hover {
            background-color: rgb(85, 170, 255);
            color: white;
        }
    """)

        header_font = QFont("Bell MT ", 14, QFont.Bold)
        self.ui.search_table.horizontalHeaderItem(2).setFont(header_font)
        self.ui.search_table.setColumnWidth(0, 400)
        self.ui.search_table.setColumnWidth(1, 750)

        row = 0
        while query.next():
            clinic_name = query.value(0)
            clinic_address = query.value(1)

            self.ui.search_table.insertRow(row)

            # Set clinic name item with the specified font
            item_clinic_name = QTableWidgetItem(clinic_name)
            self.ui.search_table.setItem(row, 0, item_clinic_name)

            # Set clinic address item with the specified font
            item_clinic_address = QTableWidgetItem(clinic_address)
            self.ui.search_table.setItem(row, 1, item_clinic_address)

            # Add view detail button
            view_button = QPushButton('View Detail')
            view_button.setStyleSheet("\n"
"    border-radius:8px;\n"
"    font: bold 12pt \"Bell MT\";\n"
"    border:1px solid grey;\n"
"    background-color:#02007a;\n"
"    color: rgb(255, 255, 255);\n"
"")
            view_button.clicked.connect(self.view_detail)
            self.ui.search_table.setCellWidget(row, 2, view_button)

            row += 1

        if row == 0 and show_message and not self.initial_load:
            QMessageBox.information(self, "No Results",
                                    "No clinics found for the selected location and search criteria.")

        if self.initial_load:
            self.initial_load = False

    def view_detail(self):
        button = self.sender()
        if button:
            row = self.ui.search_table.indexAt(button.pos()).row()
            clinic_name = self.ui.search_table.item(row, 0).text()

            # Fetch clinic details from the database
            query = QSqlQuery()
            query.prepare("SELECT CLINIC_IMG, CLINIC_DETAIL, CLINIC_ADDRESS FROM CLINICS WHERE CLINIC_NAME = ?")
            query.addBindValue(clinic_name)
            query.exec_()

            if query.next():
                clinic_img_path = query.value(0)
                clinic_detail = query.value(1)
                clinic_address = query.value(2)

                # Display clinic details in the UI
                self.ui.clinicname_label.setText(clinic_name)
                self.ui.clinicdetail_label.setPlainText(clinic_detail)

                # Clear previous clinic image
                self.ui.clinicimage.clear()
                self.current_clinic_address = clinic_address
                # Load clinic image if path is valid
                if clinic_img_path:
                    pixmap = QtGui.QPixmap(clinic_img_path)
                    if not pixmap.isNull():
                        self.ui.clinicimage.setPixmap(pixmap.scaledToWidth(300))

                # Display doctors associated with this clinic
                self.display_doctors(clinic_name)
                self.ui.viewmap.clicked.connect(self.view_map)
                self.ui.stackedWidget.setCurrentIndex(5)

    def view_map(self):
        address = getattr(self, 'current_clinic_address', None)  # Retrieve the stored address
        if address:
            url = f"https://www.google.com/maps/search/?api=1&query={address}"
            webbrowser.open(url)
        else:
            QMessageBox.warning(self, 'Address Not Found', 'The address for this clinic is not available.')

    def display_doctors(self, clinic_name):
        query = QSqlQuery()
        query.prepare("SELECT DOCTOR_NAME, DOCTOR_IMG FROM DOCTORS WHERE CLINIC_NAME = ?")
        query.addBindValue(clinic_name)
        query.exec_()

        doctor_widgets = [self.ui.doctorimg1, self.ui.doctorimg2, self.ui.doctorimg3]
        doctor_detail_labels = [self.ui.doctordetail_label1, self.ui.doctordetail_label2, self.ui.doctordetail_label3]
        index = 0

        while query.next() and index < len(doctor_widgets):
            doctor_name = query.value(0)
            doctor_img_path = query.value(1)

            # Load doctor image if path is valid
            if doctor_img_path:
                pixmap = QtGui.QPixmap(doctor_img_path)
                if not pixmap.isNull():
                    doctor_widgets[index].setPixmap(pixmap.scaledToWidth(150))

            # Display doctor detail
            doctor_detail_labels[index].setText(doctor_name)

            index += 1

        # Hide remaining doctor image widgets if less than 3 doctors
        for i in range(index, len(doctor_widgets)):
            doctor_widgets[i].hide()
            doctor_detail_labels[i].hide()

        self.ui.ourdoctor.setText(f"Our Doctors at {clinic_name}")

    def retrieve_user_info(self, email):
        query = QSqlQuery()
        query.prepare("""
            SELECT PATIENT_NAME, PATIENT_EMAIL, PATIENT_IC, PATIENT_PHONENO, PATIENT_ADDRESS
            FROM PATIENT
            WHERE PATIENT_EMAIL = ?
        """)
        query.addBindValue(email)
        query.exec_()

        if query.next():
            user_info = {
                "name": query.value(0),
                "email": query.value(1),
                "ic": query.value(2),
                "phone": query.value(3),
                "address": query.value(4),
            }
            return user_info
        else:
            return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = create_connection()
    mainWindow = MyMainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
