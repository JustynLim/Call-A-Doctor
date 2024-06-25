from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


from modules.resources_rc import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1087, 535)
        MainWindow.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.Menu = QWidget(self.centralwidget)
        self.Menu.setObjectName(u"Menu")
        self.Menu.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.verticalLayout_6 = QVBoxLayout(self.Menu)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.Menu)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/images/images/images/doctor.png"))

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.menu_btn_1 = QPushButton(self.Menu)
        self.menu_btn_1.setObjectName(u"menu_btn_1")
        self.menu_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-menu.png);")
        self.menu_btn_1.setCheckable(True)
        self.menu_btn_1.setChecked(False)
        self.menu_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.menu_btn_1)

        self.home_btn_1 = QPushButton(self.Menu)
        self.home_btn_1.setObjectName(u"home_btn_1")
        self.home_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-home.png);")
        self.home_btn_1.setCheckable(True)

        self.verticalLayout.addWidget(self.home_btn_1)

        self.schedule_btn_1 = QPushButton(self.Menu)
        self.schedule_btn_1.setObjectName(u"schedule_btn_1")
        self.schedule_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-calendar-check.png);")
        self.schedule_btn_1.setCheckable(True)

        self.verticalLayout.addWidget(self.schedule_btn_1)

        self.patientPrescription_btn_1 = QPushButton(self.Menu)
        self.patientPrescription_btn_1.setObjectName(u"patientPrescription_btn_1")
        self.patientPrescription_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.patientPrescription_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-clipboard.png);")
        self.patientPrescription_btn_1.setCheckable(True)

        self.verticalLayout.addWidget(self.patientPrescription_btn_1)

        self.patientRecord_btn_1 = QPushButton(self.Menu)
        self.patientRecord_btn_1.setObjectName(u"patientRecord_btn_1")
        self.patientRecord_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.patientRecord_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-magnifying-glass.png);")
        self.patientRecord_btn_1.setCheckable(True)

        self.verticalLayout.addWidget(self.patientRecord_btn_1)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 249, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.profile_btn_1 = QPushButton(self.Menu)
        self.profile_btn_1.setObjectName(u"profile_btn_1")
        self.profile_btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_btn_1.setStyleSheet(u"image: url(:/icons/images/icons/cil-user.png);")
        self.profile_btn_1.setCheckable(True)

        self.verticalLayout_4.addWidget(self.profile_btn_1)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.Menu, 0, 0, 1, 1)

        self.Menu_extend = QWidget(self.centralwidget)
        self.Menu_extend.setObjectName(u"Menu_extend")
        self.Menu_extend.setEnabled(True)
        self.Menu_extend.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.verticalLayout_7 = QVBoxLayout(self.Menu_extend)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.Menu_extend)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/images/images/images/doctor.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.Menu_extend)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Menu_btn_2 = QPushButton(self.Menu_extend)
        self.Menu_btn_2.setObjectName(u"Menu_btn_2")
        self.Menu_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.Menu_btn_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"text-align: left;")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_btn_2.setIcon(icon)
        self.Menu_btn_2.setCheckable(True)
        self.Menu_btn_2.setChecked(True)
        self.Menu_btn_2.setAutoRepeat(False)
        self.Menu_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.Menu_btn_2)

        self.home_btn_2 = QPushButton(self.Menu_extend)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_2.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.home_btn_2)

        self.schedule_btn_2 = QPushButton(self.Menu_extend)
        self.schedule_btn_2.setObjectName(u"schedule_btn_2")
        self.schedule_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_btn_2.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/cil-calendar-check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.schedule_btn_2.setIcon(icon2)
        self.schedule_btn_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.schedule_btn_2)

        self.patientPrescription_btn_2 = QPushButton(self.Menu_extend)
        self.patientPrescription_btn_2.setObjectName(u"patientPrescription_btn_2")
        self.patientPrescription_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.patientPrescription_btn_2.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/cil-clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientPrescription_btn_2.setIcon(icon3)
        self.patientPrescription_btn_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.patientPrescription_btn_2)

        self.patientRecord_btn_2 = QPushButton(self.Menu_extend)
        self.patientRecord_btn_2.setObjectName(u"patientRecord_btn_2")
        self.patientRecord_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.patientRecord_btn_2.setStyleSheet(u"text-align: left;\n"
"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-magnifying-glass.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientRecord_btn_2.setIcon(icon4)
        self.patientRecord_btn_2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.patientRecord_btn_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 249, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.profile_btn_2 = QPushButton(self.Menu_extend)
        self.profile_btn_2.setObjectName(u"profile_btn_2")
        self.profile_btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_btn_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_btn_2.setIcon(icon5)
        self.profile_btn_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.profile_btn_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_5)


        self.gridLayout.addWidget(self.Menu_extend, 0, 1, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget = QStackedWidget(self.widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.label_username = QLabel(self.home_page)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setGeometry(QRect(0, 9, 751, 31))
        self.label_username.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_clinicName = QLabel(self.home_page)
        self.label_clinicName.setObjectName(u"label_clinicName")
        self.label_clinicName.setGeometry(QRect(0, 50, 751, 51))
        self.label_clinicName.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_todaySchedule = QLabel(self.home_page)
        self.label_todaySchedule.setObjectName(u"label_todaySchedule")
        self.label_todaySchedule.setGeometry(QRect(0, 120, 381, 41))
        self.label_todaySchedule.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.table_todaySchedule = QTableWidget(self.home_page)
        self.table_todaySchedule.setObjectName(u"table_todaySchedule")
        self.table_todaySchedule.setGeometry(QRect(0, 170, 381, 321))
        self.table_todaySchedule.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);")
        self.label_requestApproval = QLabel(self.home_page)
        self.label_requestApproval.setObjectName(u"label_requestApproval")
        self.label_requestApproval.setGeometry(QRect(400, 120, 341, 41))
        self.label_requestApproval.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.list_approval = QTableWidget(self.home_page)
        self.list_approval.setObjectName(u"list_approval")
        self.list_approval.setGeometry(QRect(400, 170, 341, 321))
        self.list_approval.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);")
        self.approve_btn = QPushButton(self.home_page)
        self.approve_btn.setObjectName(u"approve_btn")
        self.approve_btn.setGeometry(QRect(750, 460, 91, 31))
        self.approve_btn.setStyleSheet(u"background-color:rgb(0, 105, 143);\n"
"color:rgb(248, 255, 255);\n"
"font: Bold;")
        self.reject_btn = QPushButton(self.home_page)
        self.reject_btn.setObjectName(u"reject_btn")
        self.reject_btn.setGeometry(QRect(750, 420, 91, 31))
        self.reject_btn.setStyleSheet(u"background-color:rgb(234, 9, 9);\n"
"color:rgb(248, 255, 255);\n"
"font: Bold;")
        self.label_username_fill_2 = QLabel(self.home_page)
        self.label_username_fill_2.setObjectName(u"label_username_fill_2")
        self.label_username_fill_2.setGeometry(QRect(100, 9, 651, 31))
        self.label_username_fill_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_clinicName_fill_2 = QLabel(self.home_page)
        self.label_clinicName_fill_2.setObjectName(u"label_clinicName_fill_2")
        self.label_clinicName_fill_2.setGeometry(QRect(100, 60, 651, 31))
        self.label_clinicName_fill_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.home_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_profile = QLabel(self.profile_page)
        self.label_profile.setObjectName(u"label_profile")
        self.label_profile.setGeometry(QRect(0, 10, 751, 31))
        self.label_profile.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_username_2 = QLabel(self.profile_page)
        self.label_username_2.setObjectName(u"label_username_2")
        self.label_username_2.setGeometry(QRect(0, 50, 750, 50))
        self.label_username_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_clinicName_2 = QLabel(self.profile_page)
        self.label_clinicName_2.setObjectName(u"label_clinicName_2")
        self.label_clinicName_2.setGeometry(QRect(0, 110, 750, 50))
        self.label_clinicName_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_address = QLabel(self.profile_page)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setGeometry(QRect(0, 180, 750, 50))
        self.label_address.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_email = QLabel(self.profile_page)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setGeometry(QRect(0, 340, 750, 50))
        self.label_email.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_email_2 = QLabel(self.profile_page)
        self.label_email_2.setObjectName(u"label_email_2")
        self.label_email_2.setGeometry(QRect(0, 260, 750, 50))
        self.label_email_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_email_fill = QLabel(self.profile_page)
        self.label_email_fill.setObjectName(u"label_email_fill")
        self.label_email_fill.setGeometry(QRect(190, 340, 571, 44))
        self.label_email_fill.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_phoneNumber_fill = QLabel(self.profile_page)
        self.label_phoneNumber_fill.setObjectName(u"label_phoneNumber_fill")
        self.label_phoneNumber_fill.setGeometry(QRect(190, 260, 571, 44))
        self.label_phoneNumber_fill.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_address_fill = QLabel(self.profile_page)
        self.label_address_fill.setObjectName(u"label_address_fill")
        self.label_address_fill.setGeometry(QRect(190, 180, 571, 44))
        self.label_address_fill.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_clinicName_fill = QLabel(self.profile_page)
        self.label_clinicName_fill.setObjectName(u"label_clinicName_fill")
        self.label_clinicName_fill.setGeometry(QRect(190, 120, 571, 44))
        self.label_clinicName_fill.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_username_fill = QLabel(self.profile_page)
        self.label_username_fill.setObjectName(u"label_username_fill")
        self.label_username_fill.setGeometry(QRect(190, 50, 571, 44))
        self.label_username_fill.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.profile_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.label_schedule = QLabel(self.schedule_page)
        self.label_schedule.setObjectName(u"label_schedule")
        self.label_schedule.setGeometry(QRect(0, 10, 751, 31))
        self.label_schedule.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_schedule = QTableWidget(self.schedule_page)
        self.tableWidget_schedule.setObjectName(u"tableWidget_schedule")
        self.tableWidget_schedule.setGeometry(QRect(460, 50, 371, 449))
        self.tableWidget_schedule.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255)")
        self.calendar_schedule = QCalendarWidget(self.schedule_page)
        self.calendar_schedule.setObjectName(u"calendar_schedule")
        self.calendar_schedule.setGeometry(QRect(0, 50, 451, 441))
        self.calendar_schedule.setStyleSheet(u"#calendar_schedule QWidget {\n"
"    alternate-background-color: rgb(0, 105, 143);\n"
"	font: rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#calendar_schedule_body{\n"
"	font:rgb(255, 255, 255);\n"
"}\n"
"\n"
"#qt_calendar_button {\n"
"    qproperty-icon: none;\n"
"    border: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    margin-left: 5px;\n"
"    qproperty-icon: url(:/images/images/images/7etpgol5vni7a29jfbecupgimi.png);\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"    margin-right: 5px;\n"
"    qproperty-icon: url(:/images/images/images/a99rnbdjdo7qbirto4a5ivqhr3.png);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed,\n"
"#qt_calendar_nextmonth:pressed{\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"#qt_calendar_yearbutton {\n"
"margin: 5px;\n"
"padding:0 10px;\n"
"}")
        self.stackedWidget.addWidget(self.schedule_page)
        self.patientRecord_page = QWidget()
        self.patientRecord_page.setObjectName(u"patientRecord_page")
        self.label_patientRecord = QLabel(self.patientRecord_page)
        self.label_patientRecord.setObjectName(u"label_patientRecord")
        self.label_patientRecord.setGeometry(QRect(0, 10, 751, 41))
        self.label_patientRecord.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.list_patientRecord = QTableWidget(self.patientRecord_page)
        self.list_patientRecord.setObjectName(u"list_patientRecord")
        self.list_patientRecord.setGeometry(QRect(0, 130, 411, 331))
        self.list_patientRecord.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_patientName_2 = QLineEdit(self.patientRecord_page)
        self.lineEdit_patientName_2.setObjectName(u"lineEdit_patientName_2")
        self.lineEdit_patientName_2.setGeometry(QRect(0, 60, 831, 31))
        self.lineEdit_patientName_2.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_diagnosis = QPlainTextEdit(self.patientRecord_page)
        self.plainTextEdit_diagnosis.setObjectName(u"plainTextEdit_diagnosis")
        self.plainTextEdit_diagnosis.setGeometry(QRect(420, 130, 411, 141))
        self.plainTextEdit_diagnosis.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit_prescription = QPlainTextEdit(self.patientRecord_page)
        self.plainTextEdit_prescription.setObjectName(u"plainTextEdit_prescription")
        self.plainTextEdit_prescription.setGeometry(QRect(420, 310, 411, 188))
        self.plainTextEdit_prescription.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_diagnosis = QLabel(self.patientRecord_page)
        self.label_diagnosis.setObjectName(u"label_diagnosis")
        self.label_diagnosis.setGeometry(QRect(420, 100, 331, 21))
        self.label_diagnosis.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_prescription = QLabel(self.patientRecord_page)
        self.label_prescription.setObjectName(u"label_prescription")
        self.label_prescription.setGeometry(QRect(420, 280, 331, 21))
        self.label_prescription.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.search_btn = QPushButton(self.patientRecord_page)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(755, 64, 71, 24))
        self.search_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_btn.setStyleSheet(u"background-color:rgb(0, 105, 143);\n"
"color:rgb(248, 255, 255);")
        self.select_btn = QPushButton(self.patientRecord_page)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setGeometry(QRect(310, 470, 101, 31))
        self.select_btn.setStyleSheet(u"background-color:rgb(0, 105, 143);\n"
"color:rgb(248, 255, 255);")
        self.stackedWidget.addWidget(self.patientRecord_page)
        self.patientPrescription_page = QWidget()
        self.patientPrescription_page.setObjectName(u"patientPrescription_page")
        self.label_patientPrescription = QLabel(self.patientPrescription_page)
        self.label_patientPrescription.setObjectName(u"label_patientPrescription")
        self.label_patientPrescription.setGeometry(QRect(0, 10, 751, 41))
        self.label_patientPrescription.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_patientName = QLineEdit(self.patientPrescription_page)
        self.lineEdit_patientName.setObjectName(u"lineEdit_patientName")
        self.lineEdit_patientName.setGeometry(QRect(0, 60, 751, 51))
        self.lineEdit_patientName.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_diagnosis = QLineEdit(self.patientPrescription_page)
        self.lineEdit_diagnosis.setObjectName(u"lineEdit_diagnosis")
        self.lineEdit_diagnosis.setGeometry(QRect(0, 130, 751, 131))
        self.lineEdit_diagnosis.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_prescription = QLineEdit(self.patientPrescription_page)
        self.lineEdit_prescription.setObjectName(u"lineEdit_prescription")
        self.lineEdit_prescription.setGeometry(QRect(0, 280, 751, 181))
        self.lineEdit_prescription.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.btn_save = QPushButton(self.patientPrescription_page)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(630, 470, 121, 31))
        self.btn_save.setStyleSheet(u"background-color:rgb(0, 105, 143);\n"
"color:rgb(248, 255, 255);")
        self.stackedWidget.addWidget(self.patientPrescription_page)

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.schedule_btn_2.toggled.connect(self.schedule_btn_1.setChecked)
        self.schedule_btn_1.toggled.connect(self.schedule_btn_2.setChecked)
        self.patientPrescription_btn_2.toggled.connect(self.patientPrescription_btn_1.setChecked)
        self.patientPrescription_btn_1.toggled.connect(self.patientPrescription_btn_2.setChecked)
        self.patientRecord_btn_1.toggled.connect(self.patientRecord_btn_2.setChecked)
        self.patientRecord_btn_2.toggled.connect(self.patientRecord_btn_1.setChecked)
        self.profile_btn_1.toggled.connect(self.profile_btn_2.setChecked)
        self.profile_btn_2.toggled.connect(self.profile_btn_1.setChecked)
        self.Menu_btn_2.toggled.connect(self.Menu.setVisible)
        self.Menu_btn_2.toggled.connect(self.Menu_extend.setHidden)
        self.Menu_btn_2.toggled.connect(self.menu_btn_1.setChecked)
        self.menu_btn_1.toggled.connect(self.Menu_extend.setVisible)
        self.menu_btn_1.toggled.connect(self.Menu.setHidden)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.menu_btn_1.setText("")
        self.home_btn_1.setText("")
        self.schedule_btn_1.setText("")
        self.patientPrescription_btn_1.setText("")
        self.patientRecord_btn_1.setText("")
        self.profile_btn_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Call a Doctor", None))
        self.Menu_btn_2.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.schedule_btn_2.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.patientPrescription_btn_2.setText(QCoreApplication.translate("MainWindow", u"Patient Prescription", None))
        self.patientRecord_btn_2.setText(QCoreApplication.translate("MainWindow", u"Patient Record", None))
        self.profile_btn_2.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_clinicName.setText(QCoreApplication.translate("MainWindow", u"Clinic name:", None))
        self.label_todaySchedule.setText(QCoreApplication.translate("MainWindow", u"Today Schedule", None))
        self.label_requestApproval.setText(QCoreApplication.translate("MainWindow", u"Request approval", None))
        self.approve_btn.setText(QCoreApplication.translate("MainWindow", u"Approve", None))
        self.reject_btn.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.label_username_fill_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_clinicName_fill_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_profile.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_username_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_clinicName_2.setText(QCoreApplication.translate("MainWindow", u"Clinic name:", None))
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_email_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.label_email_fill.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_phoneNumber_fill.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_address_fill.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_clinicName_fill.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_username_fill.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_schedule.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_patientRecord.setText(QCoreApplication.translate("MainWindow", u"Patient Record", None))
        self.lineEdit_patientName_2.setInputMask("")
        self.lineEdit_patientName_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.label_diagnosis.setText(QCoreApplication.translate("MainWindow", u"Diagnosis", None))
        self.label_prescription.setText(QCoreApplication.translate("MainWindow", u"Prescription", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.select_btn.setText(QCoreApplication.translate("MainWindow", u"SELECT", None))
        self.label_patientPrescription.setText(QCoreApplication.translate("MainWindow", u"Patient Prescription", None))
        self.lineEdit_patientName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Patient Name", None))
        self.lineEdit_diagnosis.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Diagnosis", None))
        self.lineEdit_prescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Prescription", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

