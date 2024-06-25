from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from Clinicmodules.resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(828, 536)
        MainWindow.setMinimumSize(QSize(828, 536))
        MainWindow.setMaximumSize(QSize(828, 536))
        MainWindow.setStyleSheet(u"background-color: rgb(233, 253, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Icon = QWidget(self.centralwidget)
        self.Icon.setObjectName(u"Icon")
        self.Icon.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 253, 242);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:black;\n"
"	height:30px;\n"
"	border:none;\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Icon)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.Icon)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(40, 40))
        self.label.setMaximumSize(QSize(40, 40))
        self.label.setPixmap(QPixmap(u":/images/doctor.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 15, -1, -1)
        self.home_1 = QPushButton(self.Icon)
        self.home_1.setObjectName(u"home_1")
        icon = QIcon()
        icon.addFile(u":/images/cil-home (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_1.setIcon(icon)
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_1)

        self.adddoctor_1 = QPushButton(self.Icon)
        self.adddoctor_1.setObjectName(u"adddoctor_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/cil-add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adddoctor_1.setIcon(icon1)
        self.adddoctor_1.setCheckable(True)
        self.adddoctor_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.adddoctor_1)

        self.viewdoctor_1 = QPushButton(self.Icon)
        self.viewdoctor_1.setObjectName(u"viewdoctor_1")
        icon2 = QIcon()
        icon2.addFile(u":/images/cil-view.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewdoctor_1.setIcon(icon2)
        self.viewdoctor_1.setCheckable(True)
        self.viewdoctor_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.viewdoctor_1)

        self.request_1 = QPushButton(self.Icon)
        self.request_1.setObjectName(u"request_1")
        icon3 = QIcon()
        icon3.addFile(u":/images/Request.png", QSize(), QIcon.Normal, QIcon.Off)
        self.request_1.setIcon(icon3)
        self.request_1.setCheckable(True)
        self.request_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.request_1)

        self.addschedule_1 = QPushButton(self.Icon)
        self.addschedule_1.setObjectName(u"addschedule_1")
        icon4 = QIcon()
        icon4.addFile(u":/images/cil-schedule.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addschedule_1.setIcon(icon4)
        self.addschedule_1.setCheckable(True)
        self.addschedule_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.addschedule_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 244, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.Icon, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 253, 242);\n"
"	color:black\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:black;\n"
"	text-align:left;\n"
"	height:30px;\n"
"	border:none;\n"
"	padding-left:10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color:#F5FAFE;\n"
"	color:#1F95EF;\n"
"	font-weight:bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(40, 40))
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/images/doctor.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.home_2 = QPushButton(self.widget_2)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setIcon(icon)
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_2)

        self.adddoctor_2 = QPushButton(self.widget_2)
        self.adddoctor_2.setObjectName(u"adddoctor_2")
        self.adddoctor_2.setIcon(icon1)
        self.adddoctor_2.setCheckable(True)
        self.adddoctor_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.adddoctor_2)

        self.view_doctor_2 = QPushButton(self.widget_2)
        self.view_doctor_2.setObjectName(u"view_doctor_2")
        self.view_doctor_2.setIcon(icon2)
        self.view_doctor_2.setCheckable(True)
        self.view_doctor_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.view_doctor_2)

        self.request_2 = QPushButton(self.widget_2)
        self.request_2.setObjectName(u"request_2")
        self.request_2.setIcon(icon3)
        self.request_2.setCheckable(True)
        self.request_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.request_2)

        self.addschedule_2 = QPushButton(self.widget_2)
        self.addschedule_2.setObjectName(u"addschedule_2")
        self.addschedule_2.setIcon(icon4)
        self.addschedule_2.setCheckable(True)
        self.addschedule_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.addschedule_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 244, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)

        self.main_home = QWidget(self.centralwidget)
        self.main_home.setObjectName(u"main_home")
        self.verticalLayout_5 = QVBoxLayout(self.main_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.header = QWidget(self.main_home)
        self.header.setObjectName(u"header")
        self.horizontalLayout_3 = QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.menu = QPushButton(self.header)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border:none;")
        icon6 = QIcon()
        icon6.addFile(u":/images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon6)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(140, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.header)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.header)

        self.stackedWidget = QStackedWidget(self.main_home)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 253, 242);\n"
"")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.shortcut_add = QPushButton(self.home_page)
        self.shortcut_add.setObjectName(u"shortcut_add")
        self.shortcut_add.setGeometry(QRect(40, 90, 251, 151))
        self.shortcut_add.setMinimumSize(QSize(251, 151))
        self.shortcut_add.setMaximumSize(QSize(251, 151))
        self.shortcut_add.setStyleSheet(u"background-color: rgb(215, 234, 255);\n"
"border-radius: 10px;")
        self.shortcut_add.setCheckable(True)
        self.shortcut_view = QPushButton(self.home_page)
        self.shortcut_view.setObjectName(u"shortcut_view")
        self.shortcut_view.setGeometry(QRect(340, 90, 251, 151))
        self.shortcut_view.setMinimumSize(QSize(251, 151))
        self.shortcut_view.setMaximumSize(QSize(251, 151))
        self.shortcut_view.setStyleSheet(u"background-color: rgb(215, 234, 255);\n"
"border-radius: 10px;")
        self.shortcut_view.setCheckable(True)
        self.shortcut_schedule = QPushButton(self.home_page)
        self.shortcut_schedule.setObjectName(u"shortcut_schedule")
        self.shortcut_schedule.setGeometry(QRect(340, 270, 251, 151))
        self.shortcut_schedule.setMinimumSize(QSize(251, 151))
        self.shortcut_schedule.setMaximumSize(QSize(251, 151))
        self.shortcut_schedule.setStyleSheet(u"background-color: rgb(215, 234, 255);\n"
"border-radius: 10px;")
        self.shortcut_schedule.setCheckable(True)
        self.label_5 = QLabel(self.home_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 10, 121, 51))
        self.label_5.setFont(font1)
        self.shortcut_request = QPushButton(self.home_page)
        self.shortcut_request.setObjectName(u"shortcut_request")
        self.shortcut_request.setGeometry(QRect(40, 270, 251, 151))
        self.shortcut_request.setMinimumSize(QSize(251, 151))
        self.shortcut_request.setMaximumSize(QSize(251, 151))
        self.shortcut_request.setStyleSheet(u"background-color: rgb(215, 234, 255);\n"
"border-radius: 10px;")
        self.shortcut_request.setCheckable(True)
        self.stackedWidget.addWidget(self.home_page)
        self.adddoctor_page = QWidget()
        self.adddoctor_page.setObjectName(u"adddoctor_page")
        self.label_6 = QLabel(self.adddoctor_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 20, 151, 51))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:rgb(0, 85, 255);\n"
"border:none;")
        self.doc_mail_edit = QLineEdit(self.adddoctor_page)
        self.doc_mail_edit.setObjectName(u"doc_mail_edit")
        self.doc_mail_edit.setGeometry(QRect(100, 120, 441, 21))
        self.doc_mail_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.doc_add_edit = QLineEdit(self.adddoctor_page)
        self.doc_add_edit.setObjectName(u"doc_add_edit")
        self.doc_add_edit.setGeometry(QRect(100, 350, 441, 21))
        self.doc_add_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.doc_phone_edit = QLineEdit(self.adddoctor_page)
        self.doc_phone_edit.setObjectName(u"doc_phone_edit")
        self.doc_phone_edit.setGeometry(QRect(100, 270, 441, 21))
        self.doc_phone_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.doc_name_edit = QLineEdit(self.adddoctor_page)
        self.doc_name_edit.setObjectName(u"doc_name_edit")
        self.doc_name_edit.setGeometry(QRect(100, 200, 441, 21))
        self.doc_name_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.adddoctor_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 80, 91, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.adddoctor_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 170, 91, 21))
        self.label_8.setFont(font2)
        self.label_9 = QLabel(self.adddoctor_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 240, 161, 21))
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.adddoctor_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(100, 310, 111, 21))
        self.label_10.setFont(font2)
        self.confirm_button = QPushButton(self.adddoctor_page)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setGeometry(QRect(270, 400, 101, 31))
        self.confirm_button.setStyleSheet(u"background-color: rgb(231, 255, 220);\n"
"border-radius: 10px;\n"
"border:none;")
        icon7 = QIcon()
        icon7.addFile(u":/images/check-mark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confirm_button.setIcon(icon7)
        self.confirm_button.setCheckable(True)
        self.stackedWidget.addWidget(self.adddoctor_page)
        self.viewdoctor_page = QWidget()
        self.viewdoctor_page.setObjectName(u"viewdoctor_page")
        self.label_11 = QLabel(self.viewdoctor_page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(250, 10, 161, 51))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color:rgb(0, 85, 255);\n"
"border:none;")
        self.doctor_table = QTableWidget(self.viewdoctor_page)
        if (self.doctor_table.columnCount() < 4):
            self.doctor_table.setColumnCount(4)
        font3 = QFont()
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.doctor_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.doctor_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.doctor_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.doctor_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.doctor_table.setObjectName(u"doctor_table")
        self.doctor_table.setGeometry(QRect(20, 70, 591, 351))
        self.doctor_table.horizontalHeader().setDefaultSectionSize(150)
        self.delete_button = QPushButton(self.viewdoctor_page)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(520, 430, 75, 24))
        self.delete_button.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 223, 210);\n"
"border-radius:10px;")
        icon8 = QIcon()
        icon8.addFile(u":/images/bin.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon8)
        self.delete_button.setCheckable(True)
        self.stackedWidget.addWidget(self.viewdoctor_page)
        self.request_page = QWidget()
        self.request_page.setObjectName(u"request_page")
        self.label_13 = QLabel(self.request_page)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 10, 231, 51))
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"color:rgb(0, 85, 255);\n"
"border:none;")
        self.patient_request_table = QTableWidget(self.request_page)
        if (self.patient_request_table.columnCount() < 4):
            self.patient_request_table.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.patient_request_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.patient_request_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.patient_request_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.patient_request_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.patient_request_table.setObjectName(u"patient_request_table")
        self.patient_request_table.setGeometry(QRect(20, 110, 481, 321))
        self.patient_request_table.horizontalHeader().setDefaultSectionSize(120)
        self.accept_request_button = QPushButton(self.request_page)
        self.accept_request_button.setObjectName(u"accept_request_button")
        self.accept_request_button.setGeometry(QRect(530, 170, 75, 24))
        self.accept_request_button.setStyleSheet(u"background-color: rgb(231, 255, 220);\n"
"border-radius: 10px;\n"
"border:none;")
        self.accept_request_button.setIcon(icon7)
        self.accept_request_button.setCheckable(True)
        self.reject_request_button = QPushButton(self.request_page)
        self.reject_request_button.setObjectName(u"reject_request_button")
        self.reject_request_button.setGeometry(QRect(530, 310, 75, 24))
        self.reject_request_button.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 223, 210);\n"
"border-radius:10px;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/images/Reject.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reject_request_button.setIcon(icon9)
        self.reject_request_button.setCheckable(True)
        self.stackedWidget.addWidget(self.request_page)
        self.addschedule_page = QWidget()
        self.addschedule_page.setObjectName(u"addschedule_page")
        self.label_12 = QLabel(self.addschedule_page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(280, 0, 121, 51))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"color:rgb(0, 85, 255);\n"
"border:none;")
        self.schedule_table = QTableWidget(self.addschedule_page)
        if (self.schedule_table.columnCount() < 3):
            self.schedule_table.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.schedule_table.setObjectName(u"schedule_table")
        self.schedule_table.setGeometry(QRect(40, 70, 561, 371))
        self.schedule_table.horizontalHeader().setDefaultSectionSize(187)
        self.addschedule_button = QPushButton(self.addschedule_page)
        self.addschedule_button.setObjectName(u"addschedule_button")
        self.addschedule_button.setGeometry(QRect(490, 30, 111, 24))
        self.addschedule_button.setStyleSheet(u"background-color: rgb(255, 215, 93);\n"
"border-radius:10px;")
        icon10 = QIcon()
        icon10.addFile(u":/images/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addschedule_button.setIcon(icon10)
        self.addschedule_button.setCheckable(True)
        self.selectdoctor_button = QPushButton(self.addschedule_page)
        self.selectdoctor_button.setObjectName(u"selectdoctor_button")
        self.selectdoctor_button.setGeometry(QRect(40, 30, 101, 24))
        self.selectdoctor_button.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius:10px;")
        icon11 = QIcon()
        icon11.addFile(u":/images/check (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectdoctor_button.setIcon(icon11)
        self.selectdoctor_button.setCheckable(True)
        self.doctor_name_label = QLabel(self.addschedule_page)
        self.doctor_name_label.setObjectName(u"doctor_name_label")
        self.doctor_name_label.setGeometry(QRect(270, 50, 191, 16))
        self.stackedWidget.addWidget(self.addschedule_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.main_home, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.Icon.setHidden)
        self.menu.toggled.connect(self.widget_2.setVisible)
        self.addschedule_1.toggled.connect(self.addschedule_2.setChecked)
        self.viewdoctor_1.toggled.connect(self.view_doctor_2.setChecked)
        self.adddoctor_1.toggled.connect(self.adddoctor_2.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.adddoctor_2.toggled.connect(self.adddoctor_1.setChecked)
        self.view_doctor_2.toggled.connect(self.viewdoctor_1.setChecked)
        self.addschedule_2.toggled.connect(self.addschedule_1.setChecked)
        self.request_1.toggled.connect(self.request_2.setChecked)
        self.request_2.toggled.connect(self.request_1.setChecked)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.home_1.setText("")
        self.adddoctor_1.setText("")
        self.viewdoctor_1.setText("")
        self.request_1.setText("")
        self.addschedule_1.setText("")
        #self.logout_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CAD", None))
        self.home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.adddoctor_2.setText(QCoreApplication.translate("MainWindow", u"Add Doctor", None))
        self.view_doctor_2.setText(QCoreApplication.translate("MainWindow", u"View Doctor", None))
        self.request_2.setText(QCoreApplication.translate("MainWindow", u"Request", None))
        self.addschedule_2.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.menu.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Call A Doctor", None))
        self.shortcut_add.setText(QCoreApplication.translate("MainWindow", u"Add Doctor", None))
        self.shortcut_view.setText(QCoreApplication.translate("MainWindow", u"View Doctor", None))
        self.shortcut_schedule.setText(QCoreApplication.translate("MainWindow", u"Add Schedule", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Shortcuts", None))
        self.shortcut_request.setText(QCoreApplication.translate("MainWindow", u"Request Approval", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Add Doctor", None))
        self.doc_mail_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.doc_add_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.doc_phone_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.doc_name_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Doctor's Email:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Doctor's Name:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Doctor's Phone Number:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Doctor's Address:", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"View Doctor", None))
        ___qtablewidgetitem = self.doctor_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Doctor's Email", None));
        ___qtablewidgetitem1 = self.doctor_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Doctor's Name", None));
        ___qtablewidgetitem2 = self.doctor_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Doctor's Phone Number", None));
        ___qtablewidgetitem3 = self.doctor_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Doctor's Address", None));
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Request Approval", None))
        ___qtablewidgetitem4 = self.patient_request_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Patient Request", None));
        ___qtablewidgetitem5 = self.patient_request_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Patient", None));
        ___qtablewidgetitem6 = self.patient_request_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem7 = self.patient_request_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.accept_request_button.setText(QCoreApplication.translate("MainWindow", u"Accept", None))
        self.reject_request_button.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        ___qtablewidgetitem8 = self.schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Task", None));
        ___qtablewidgetitem9 = self.schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem10 = self.schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        self.addschedule_button.setText(QCoreApplication.translate("MainWindow", u"Add Schedule", None))
        self.selectdoctor_button.setText(QCoreApplication.translate("MainWindow", u"Select Doctor", None))
        self.doctor_name_label.setText(QCoreApplication.translate("MainWindow", u"Doctor:", None))
    # retranslateUi