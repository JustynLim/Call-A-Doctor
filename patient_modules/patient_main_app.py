import sys, webbrowser, re, os,sqlite3
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QPushButton
from PySide6.QtSql import QSqlDatabase, QSqlQuery
#from PySide6.QtCore import pyqtSlot
from PySide6.QtGui import QFont
from .ui import Ui_MainWindow
from datetime import datetime, time, timedelta
from PySide6.QtCore import QDate

# Global variable(s)
global_path = os.path.dirname(__file__)   # Directory of the current file
parent_dir = os.path.dirname(global_path)  # Parent directory
db_path = os.path.join(parent_dir, "db")
path_db_file = os.path.join(db_path, "database.db")


class PatientApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, patient_email, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initial_load = True  # Flag to track initial population
        self.ui.dateEdit.setMinimumDate(QDate.currentDate())
        self.ui.dateEdit.setMaximumDate(QDate.currentDate().addYears(1))
        self.holiday_dates = ["2024-12-25", "2024-01-01", "2024-07-04"]

        self.patient_email = patient_email


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
        try:

            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

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

            if selected_date == current_date:
                QMessageBox.warning(self, 'Validation Error', 'The time cannot be today.')
                return

            # Validate the clinic selection
            if clinic_name == "Choose Clinic":
                QMessageBox.warning(self, 'Validation Error', 'Please select a valid clinic.')
                return

            # Determine the package
            package = self.determine_package(date, time)

            # Insert the request into the database
            cursor.execute("""
                INSERT INTO PATIENT_REQUEST (APPOINTMENT_DATE, APPOINTMENT_TIME, PACKAGE, CLINIC_NAME, PATIENT_EMAIL)
                VALUES (?, ?, ?, ?, ?)
            """, (date, time, package, clinic_name, self.patient_email))

            conn.commit()
            print(
                f"Submitting request: date={date}, time={time}, package={package}, clinic_name={clinic_name}, patient_email={self.patient_email}")

            success_message = f'''
                Your doctor request has been successfully submitted with the following details:
                - Clinic: {clinic_name}
                - Date: {date}
                - Time: {time}
                - Package: {package}
            '''
            QMessageBox.information(self, 'Success', success_message)
            print(f'Success: {success_message}')

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Database Error', f'Failed to submit the doctor request. Error: {str(e)}')
            print(f'Database Error: {str(e)}')
        finally:
            if conn:
                conn.close()

    def populate_record_table(self):
        try:
            # Open the database connection

            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Clear the existing rows and columns
            self.ui.record_table.clear()
            self.ui.record_table.setRowCount(0)
            self.ui.record_table.setColumnCount(4)  # Set the number of columns
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
            self.ui.record_table.setColumnWidth(0, 200)
            self.ui.record_table.setColumnWidth(1, 300)
            self.ui.record_table.setColumnWidth(2, 400)
            self.ui.record_table.setColumnWidth(3, 170)

            # Execute the SQL query
            cursor.execute(
                """
                SELECT D.DOCTOR_NAME, PR.DIAGNOSIS, PR.PRESCRIPTION, PR.RECORD_DATE 
                FROM PATIENT_RECORD PR
                JOIN DOCTORS D ON PR.DOCTOR_EMAIL = D.DOCTOR_EMAIL
                WHERE PR.PATIENT_EMAIL = ?
                """,
                (self.patient_email,)
            )
            records = cursor.fetchall()

            # Populate the table with the query results
            for row_idx, record in enumerate(records):
                self.ui.record_table.insertRow(row_idx)
                for col_idx, data in enumerate(record):
                    item = QTableWidgetItem(str(data))
                    self.ui.record_table.setItem(row_idx, col_idx, item)

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if conn:
                conn.close()

    def populate_clinic_combobox(self):
        try:

            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            self.ui.clinic_combobox.clear()  # Clear existing items
            self.ui.clinic_combobox.addItem("Choose Clinic")  # Add the prompt item

            cursor.execute("SELECT CLINIC_NAME FROM CLINICS")

            clinics = cursor.fetchall()  # Fetch all results from the executed query

            for clinic in clinics:
                clinic_name = clinic[0]
                self.ui.clinic_combobox.addItem(clinic_name)

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Database Error', f'Failed to populate clinic combobox. Error: {str(e)}')
            print(f'Database Error: {str(e)}')
        finally:
            if conn:
                conn.close()

    def switch_to_homePage(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_profilePage(self):
        user_info = self.retrieve_user_info(self.patient_email)

        if user_info:
            self.ui.username_edit_2.setPlainText(user_info["name"])
            self.ui.userEmail_edit_2.setPlainText(user_info["email"])
            self.ui.phone_edit_2.setPlainText(user_info["phone"])
            self.ui.address_edit_2.setPlainText(user_info["address"])
        else:
            QMessageBox.warning(self, 'User Not Found', 'The user information could not be found.')
        self.enable_profile_editing(False)
        self.ui.editprofile_btn_2.setText("Edit")
        self.ui.stackedWidget.setCurrentIndex(4)

    def enable_profile_editing(self, enable):
        self.ui.username_edit_2.setReadOnly(not enable)
        self.ui.phone_edit_2.setReadOnly(not enable)
        self.ui.address_edit_2.setReadOnly(not enable)
        # Email field should always be read-only
        self.ui.userEmail_edit_2.setReadOnly(True)

    def toggle_edit_profile(self):
        if self.ui.editprofile_btn_2.text() == "Edit":
            self.enable_profile_editing(True)
            self.ui.editprofile_btn_2.setText("Save")
            QMessageBox.information(self, 'Edit Mode',
                                    'You can now edit your profile information except the email. Click Save when you are done.')
        else:
            if self.save_profile_changes():
                self.enable_profile_editing(False)
                self.ui.editprofile_btn_2.setText("Edit")
                QMessageBox.information(self, 'Success', 'Your profile information has been successfully updated.')

    def save_profile_changes(self):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            name = self.ui.username_edit_2.toPlainText()
            phone = self.ui.phone_edit_2.toPlainText()
            address = self.ui.address_edit_2.toPlainText()

            # Validate phone number
            if not self.is_valid_phone(phone):
                QMessageBox.warning(self, 'Validation Error', 'Invalid phone number format.')
                return False

            # Check for duplicate phone number
            if self.check_duplicate("PATIENT_PHONENO", phone):
                QMessageBox.warning(self, 'Validation Error', 'Duplicate Phone Number found in the database.')
                return False

            # Update the patient's profile information
            cursor.execute("""
                UPDATE PATIENT
                SET PATIENT_NAME = ?, PATIENT_PHONENO = ?, PATIENT_ADDRESS = ?
                WHERE PATIENT_EMAIL = ?
            """, (name, phone, address, self.patient_email))

            conn.commit()  # Commit the transaction

            print(f"Profile updated: name={name}, phone={phone}, address={address}, email={self.patient_email}")
            return True

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Database Error', f'Failed to update the user information. Error: {str(e)}')
            print(f'Database Error: {str(e)}')
            return False

        finally:
            if conn:
                conn.close()

    def is_valid_phone(self, phone):
        phone_regex = r'^\d{10,15}$'
        return re.match(phone_regex, phone) is not None

    def check_duplicate(self, column, value):
        try:

            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()


            query = f"SELECT COUNT(*) FROM PATIENT WHERE {column} = ? AND PATIENT_EMAIL != ?"
            cursor.execute(query, (value, self.patient_email))

            result = cursor.fetchone()

            if result and result[0] > 0:
                return True
            return False

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Database Error', f'Error checking for duplicate entry. Error: {str(e)}')
            print(f'Database Error: {str(e)}')
            return False

        finally:
            if conn:
                conn.close()

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
        locations = ["All Location", "Bayan Lepas", "Jelutong","Ayer Itam","Simpang Ampat","George Town","Bukit Mertajam"]  # Add your locations here
        self.ui.location_combobox.addItems(locations)

    def search_clinics(self):
        search_text = self.ui.search_lineedit_6.text()
        selected_location = self.ui.location_combobox.currentText()
        self.populate_search_table(search_text, selected_location, show_message=True)

    def populate_search_table(self, search_text="", selected_location="All Location", show_message=True):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()
            base_query = "SELECT CLINIC_NAME, CLINIC_ADDRESS FROM CLINICS"
            conditions = []
            params = []

            if search_text:
                conditions.append("CLINIC_NAME LIKE ?")
                params.append(f"%{search_text}%")
            if selected_location != "All Location":
                conditions.append("CLINIC_ADDRESS LIKE ?")
                params.append(f"%{selected_location}%")

            if conditions:
                query_string = f"{base_query} WHERE {' AND '.join(conditions)}"
            else:
                query_string = base_query

            cursor.execute(query_string, params)
            results = cursor.fetchall()

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
            self.ui.search_table.setColumnWidth(0, 300)
            self.ui.search_table.setColumnWidth(1, 700)

            for row, (clinic_name, clinic_address) in enumerate(results):
                self.ui.search_table.insertRow(row)

                # Set clinic name item with the specified font
                item_clinic_name = QTableWidgetItem(clinic_name)
                self.ui.search_table.setItem(row, 0, item_clinic_name)

                # Set clinic address item with the specified font
                item_clinic_address = QTableWidgetItem(clinic_address)
                self.ui.search_table.setItem(row, 1, item_clinic_address)

                # Add view detail button
                view_button = QPushButton('View Detail')
                view_button.setStyleSheet("""
                    border-radius: 8px;
                    font: bold 12pt "Bell MT";
                    border: 1px solid grey;
                    background-color: #02007a;
                    color: rgb(255, 255, 255);
                """)
                view_button.clicked.connect(self.view_detail)
                self.ui.search_table.setCellWidget(row, 2, view_button)

            if not results and show_message and not self.initial_load:
                QMessageBox.information(self, "No Results",
                                        "No clinics found for the selected location and search criteria.")

            if self.initial_load:
                self.initial_load = False

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Database Error', f'Failed to retrieve data from the database. Error: {str(e)}')
            print(f'Database Error: {str(e)}')

        finally:
            if conn:
                conn.close()

    def view_detail(self):
        button = self.sender()
        if button:
            row = self.ui.search_table.indexAt(button.pos()).row()
            clinic_name = self.ui.search_table.item(row, 0).text()
            print(f"View detail for: {clinic_name}")  # Debug output
            try:
                conn = sqlite3.connect(path_db_file)
                cursor = conn.cursor()

                # Fetch clinic details from the database
                cursor.execute("SELECT CLINIC_IMG, CLINIC_DETAIL, CLINIC_ADDRESS FROM CLINICS WHERE CLINIC_NAME = ?",
                               (clinic_name,))
                result = cursor.fetchone()

                if result:
                    clinic_img_path, clinic_detail, clinic_address = result

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
                            self.ui.clinicimage.setPixmap(pixmap.scaledToWidth(600))
                            self.ui.clinicimage.setScaledContents(True)

                    # Display doctors associated with this clinic
                    self.display_doctors(clinic_name)

                    # Ensure the view map button is properly connected
                    try:
                        self.ui.viewmap.clicked.disconnect(self.view_map)
                    except TypeError:
                        pass  # No connection to disconnect

                    self.ui.viewmap.clicked.connect(self.view_map)

                    # Navigate to the clinic details page
                    self.ui.stackedWidget.setCurrentIndex(5)
                else:
                    print(f"No details found for clinic: {clinic_name}")

            except sqlite3.Error as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                if conn:
                    conn.close()

    def view_map(self):
        address = getattr(self, 'current_clinic_address', None)  # Retrieve the stored address
        if address:
            url = f"https://www.google.com/maps/search/?api=1&query={address}"
            webbrowser.open(url)
        else:
            QMessageBox.warning(self, 'Address Not Found', 'The address for this clinic is not available.')

    def display_doctors(self, clinic_name):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            cursor.execute("SELECT DOCTOR_NAME, DOCTOR_IMG FROM DOCTORS WHERE CLINIC_NAME = ?", (clinic_name,))

            doctor_widgets = [self.ui.doctorimg1, self.ui.doctorimg2, self.ui.doctorimg3]
            doctor_detail_labels = [self.ui.doctordetail_label1, self.ui.doctordetail_label2,
                                    self.ui.doctordetail_label3]
            index = 0

            # Fetch all results at once
            results = cursor.fetchall()

            for row in results:
                doctor_name = row[0]
                doctor_img_path = row[1]

                # Load doctor image if path is valid
                if doctor_img_path:
                    pixmap = QtGui.QPixmap(doctor_img_path)
                    if not pixmap.isNull():
                        doctor_widgets[index].setPixmap(pixmap.scaledToWidth(150))

                # Add "Dr." prefix to doctor name
                full_doctor_name = f"Dr. {doctor_name}" if doctor_name else "Dr."

                # Display doctor detail
                doctor_detail_labels[index].setText(full_doctor_name)

                index += 1

            # Hide remaining doctor image widgets if less than 3 doctors
            for i in range(index, len(doctor_widgets)):
                doctor_widgets[i].hide()
                doctor_detail_labels[i].hide()

            self.ui.ourdoctor.setText(f"Our Doctors at {clinic_name}")

        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if conn:
                conn.close()

    def retrieve_user_info(self, email):
        try:
            conn = sqlite3.connect(path_db_file)
            cursor = conn.cursor()

            # Corrected the query execution and parameter passing
            cursor.execute("""
                SELECT PATIENT_NAME, PATIENT_EMAIL, PATIENT_PHONENO, PATIENT_ADDRESS
                FROM PATIENT
                WHERE PATIENT_EMAIL = ?
            """, (email,))

            # Fetch the first result
            result = cursor.fetchone()

            if result:
                user_info = {
                    "name": result[0],
                    "email": result[1],
                    "phone": result[2],
                    "address": result[3],
                }
                return user_info
            else:
                return None

        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None  # Return None on error
        except Exception as e:
            print(f"Error: {e}")
            return None  # Return None on any other exception
        finally:
            if conn:
                conn.close()