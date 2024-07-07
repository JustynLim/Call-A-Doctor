# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doc.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QTimeEdit, QVBoxLayout, QWidget)
from patient_modules.resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1482, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sidebar_2 = QWidget(self.centralwidget)
        self.sidebar_2.setObjectName(u"sidebar_2")
        sizePolicy.setHeightForWidth(self.sidebar_2.sizePolicy().hasHeightForWidth())
        self.sidebar_2.setSizePolicy(sizePolicy)
        self.sidebar_2.setStyleSheet(u"* {\n"
"    background-color:rgb(245, 245, 245);\n"
"	font: 16pt \"Bell MT\";\n"
"	border-bottom-right-radius:4px;\n"
"	border-top-right-radius:4px;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	border:none;\n"
"	height: 54px;\n"
"	padding-left: 10px;\n"
"	border-radius:8px;\n"
"	cursor: pointer;\n"
"}\n"
"QLabel{\n"
"	font: 17pt \"Bell MT\";\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #8794ac;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_7 = QVBoxLayout(self.sidebar_2)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.app_logo_2 = QLabel(self.sidebar_2)
        self.app_logo_2.setObjectName(u"app_logo_2")
        self.app_logo_2.setStyleSheet(u"")
        self.app_logo_2.setPixmap(QPixmap(u":/images/images/images/doctor.png"))
        self.app_logo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.app_logo_2)

        self.hide_btn_2 = QPushButton(self.sidebar_2)
        self.hide_btn_2.setObjectName(u"hide_btn_2")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icons8-menu-bar-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_btn_2.setIcon(icon)
        self.hide_btn_2.setIconSize(QSize(22, 22))
        self.hide_btn_2.setCheckable(True)
        self.hide_btn_2.setAutoExclusive(False)

        self.verticalLayout_4.addWidget(self.hide_btn_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_2 = QPushButton(self.sidebar_2)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icons8-home-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QSize(22, 22))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_2)

        self.search_btn_2 = QPushButton(self.sidebar_2)
        self.search_btn_2.setObjectName(u"search_btn_2")
        self.search_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icons8-search-65.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn_2.setIcon(icon2)
        self.search_btn_2.setIconSize(QSize(22, 22))
        self.search_btn_2.setCheckable(True)
        self.search_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.search_btn_2)

        self.request_btn_2 = QPushButton(self.sidebar_2)
        self.request_btn_2.setObjectName(u"request_btn_2")
        self.request_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icons8-doctor-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.request_btn_2.setIcon(icon3)
        self.request_btn_2.setIconSize(QSize(22, 22))
        self.request_btn_2.setCheckable(True)
        self.request_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.request_btn_2)

        self.record_btn_2 = QPushButton(self.sidebar_2)
        self.record_btn_2.setObjectName(u"record_btn_2")
        self.record_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icons8-history-80.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.record_btn_2.setIcon(icon4)
        self.record_btn_2.setIconSize(QSize(22, 22))
        self.record_btn_2.setCheckable(True)
        self.record_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.record_btn_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.profile_btn_2 = QPushButton(self.sidebar_2)
        self.profile_btn_2.setObjectName(u"profile_btn_2")
        self.profile_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/icons8-admin-settings-male-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profile_btn_2.setIcon(icon5)
        self.profile_btn_2.setIconSize(QSize(22, 22))
        self.profile_btn_2.setCheckable(True)
        self.profile_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.profile_btn_2)

        self.quit_btn_2 = QPushButton(self.sidebar_2)
        self.quit_btn_2.setObjectName(u"quit_btn_2")
        self.quit_btn_2.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/icons8-logout-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit_btn_2.setIcon(icon6)
        self.quit_btn_2.setIconSize(QSize(22, 22))
        self.quit_btn_2.setCheckable(True)
        self.quit_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.quit_btn_2)


        self.verticalLayout_7.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.sidebar_2, 0, 0, 1, 1)

        self.sidebar = QWidget(self.centralwidget)
        self.sidebar.setObjectName(u"sidebar")
        sizePolicy.setHeightForWidth(self.sidebar.sizePolicy().hasHeightForWidth())
        self.sidebar.setSizePolicy(sizePolicy)
        self.sidebar.setStyleSheet(u"* {\n"
"    background-color:rgb(245, 245, 245);\n"
"	font: 16pt \"Bell MT\";\n"
"	border-bottom-right-radius:4px;\n"
"	border-top-right-radius:4px;\n"
"}\n"
"QPushButton{\n"
"	text-align: left;\n"
"	border:none;\n"
"	height: 54px;\n"
"	padding-left: 10px;\n"
"	border-top-left-radius:8px;\n"
"	border-bottom-left-radius:8px;\n"
"	border-top-right-radius:8px;\n"
"	border-bottom-right-radius:8px;\n"
"	cursor: pointer;\n"
"}\n"
"QLabel{\n"
"	font: 17pt \"Bell MT\";\n"
"	font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #8794ac;\n"
"	font-weight: bold;\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.sidebar)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.app_logo = QLabel(self.sidebar)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setStyleSheet(u"")
        self.app_logo.setPixmap(QPixmap(u":/images/images/images/doctor.png"))

        self.horizontalLayout.addWidget(self.app_logo)

        self.app_name = QLabel(self.sidebar)
        self.app_name.setObjectName(u"app_name")

        self.horizontalLayout.addWidget(self.app_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.hide_btn = QPushButton(self.sidebar)
        self.hide_btn.setObjectName(u"hide_btn")
        self.hide_btn.setStyleSheet(u"QPushButton:checked{\n"
"}")
        self.hide_btn.setIcon(icon)
        self.hide_btn.setIconSize(QSize(22, 22))
        self.hide_btn.setCheckable(True)
        self.hide_btn.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.hide_btn)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.home_btn = QPushButton(self.sidebar)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        self.home_btn.setIcon(icon1)
        self.home_btn.setIconSize(QSize(22, 22))
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.home_btn)

        self.search_btn = QPushButton(self.sidebar)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QSize(22, 22))
        self.search_btn.setCheckable(True)
        self.search_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.search_btn)

        self.request_btn = QPushButton(self.sidebar)
        self.request_btn.setObjectName(u"request_btn")
        self.request_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        self.request_btn.setIcon(icon3)
        self.request_btn.setIconSize(QSize(22, 22))
        self.request_btn.setCheckable(True)
        self.request_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.request_btn)

        self.record_btn = QPushButton(self.sidebar)
        self.record_btn.setObjectName(u"record_btn")
        self.record_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        self.record_btn.setIcon(icon4)
        self.record_btn.setIconSize(QSize(22, 22))
        self.record_btn.setCheckable(True)
        self.record_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.record_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.profile_btn = QPushButton(self.sidebar)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        self.profile_btn.setIcon(icon5)
        self.profile_btn.setIconSize(QSize(22, 22))
        self.profile_btn.setCheckable(True)
        self.profile_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.profile_btn)

        self.quit_btn = QPushButton(self.sidebar)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setStyleSheet(u"QPushButton:checked{\n"
"	background-color:rgb(63,97,132);\n"
"	color:rgb(255, 255, 255);\n"
"	font-weight: bold;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/icons8-logout-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.quit_btn.setIcon(icon7)
        self.quit_btn.setIconSize(QSize(22, 22))
        self.quit_btn.setCheckable(True)
        self.quit_btn.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.quit_btn)


        self.verticalLayout_6.addLayout(self.verticalLayout_3)


        self.gridLayout.addWidget(self.sidebar, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.widget_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(229, 229, 241);\n"
"")
        self.home_pg = QWidget()
        self.home_pg.setObjectName(u"home_pg")
        self.home_pg.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.477091, x2:1, y2:0.494, stop:0 rgba(47, 0, 116, 255), stop:1 rgba(255, 212, 212, 255));")
        self.gridLayout_15 = QGridLayout(self.home_pg)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.dark_bg = QWidget(self.home_pg)
        self.dark_bg.setObjectName(u"dark_bg")
        self.dark_bg.setStyleSheet(u"background-color: rgba(0, 0, 0, 128);\n"
"")
        self.gridLayout_14 = QGridLayout(self.dark_bg)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(20)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 40, -1, -1)
        self.home_header_3 = QLabel(self.dark_bg)
        self.home_header_3.setObjectName(u"home_header_3")
        self.home_header_3.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.home_header_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.home_header_3)

        self.home_header_4 = QLabel(self.dark_bg)
        self.home_header_4.setObjectName(u"home_header_4")
        self.home_header_4.setStyleSheet(u"background-color: transparent;\n"
"font: 75 20pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.home_header_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.home_header_4)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.about_2 = QWidget(self.dark_bg)
        self.about_2.setObjectName(u"about_2")
        self.about_2.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:4px;")
        self.horizontalLayout_13 = QHBoxLayout(self.about_2)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(50, 50, 100, 0)
        self.about_us_2 = QLabel(self.about_2)
        self.about_us_2.setObjectName(u"about_us_2")
        self.about_us_2.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.about_us_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.about_us_2)

        self.textEdit_2 = QTextEdit(self.about_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setStyleSheet(u"background-color: transparent;\n"
"font: 18pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.textEdit_2.setReadOnly(True)

        self.verticalLayout_19.addWidget(self.textEdit_2)


        self.horizontalLayout_12.addLayout(self.verticalLayout_19)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_12)

        self.label_3 = QLabel(self.about_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/images/images/images/doctor1.jpg"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.label_3)


        self.verticalLayout_20.addWidget(self.about_2)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 30, -1, -1)
        self.ourpartner_2 = QLabel(self.dark_bg)
        self.ourpartner_2.setObjectName(u"ourpartner_2")
        self.ourpartner_2.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.ourpartner_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.ourpartner_2)

        self.label_2 = QLabel(self.dark_bg)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/images/images/images/PyDracula.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_2)


        self.verticalLayout_20.addLayout(self.verticalLayout_10)


        self.verticalLayout_22.addLayout(self.verticalLayout_20)


        self.gridLayout_14.addLayout(self.verticalLayout_22, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.dark_bg, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.home_pg)
        self.search_pg = QWidget()
        self.search_pg.setObjectName(u"search_pg")
        self.search_pg.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.search_pg)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setVerticalSpacing(20)
        self.gridLayout_12.setContentsMargins(-1, 25, -1, -1)
        self.widget_3 = QWidget(self.search_pg)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"background-color: rgb(2, 0, 122);\n"
"	border-radius: 8px;")
        self.gridLayout_9 = QGridLayout(self.widget_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(50, 30, 50, 40)
        self.search_table = QTableWidget(self.widget_3)
        if (self.search_table.columnCount() < 2):
            self.search_table.setColumnCount(2)
        font = QFont()
        font.setFamilies([u"Bell MT"])
        font.setPointSize(14)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.search_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        self.search_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.search_table.setObjectName(u"search_table")
        self.search_table.setStyleSheet(u"QHeaderView:section{\n"
"		\n"
"	background-color: rgb(229, 229, 241);\n"
"}\n"
"QTableWidget{\n"
"background:transparent;\n"
"	background-color: rgb(255, 255, 255);\n"
"	alternate-background-color: rgb(229, 229, 241);\n"
"	border-radius: 8px;\n"
"}\n"
"")
        self.search_table.setAlternatingRowColors(True)
        self.search_table.setRowCount(0)
        self.search_table.horizontalHeader().setCascadingSectionResizes(False)
        self.search_table.horizontalHeader().setMinimumSectionSize(40)
        self.search_table.horizontalHeader().setDefaultSectionSize(40)
        self.search_table.horizontalHeader().setStretchLastSection(True)
        self.search_table.verticalHeader().setVisible(False)
        self.search_table.verticalHeader().setCascadingSectionResizes(False)
        self.search_table.verticalHeader().setHighlightSections(True)

        self.gridLayout_9.addWidget(self.search_table, 1, 0, 1, 1)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(50)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(100, -1, 100, 20)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(50)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.search_lineedit_6 = QLineEdit(self.widget_3)
        self.search_lineedit_6.setObjectName(u"search_lineedit_6")
        self.search_lineedit_6.setStyleSheet(u"\n"
"	font:  16pt \"Bell MT\";\n"
"	color: black;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid #ccc;\n"
"	border-radius: 4px;")

        self.horizontalLayout_9.addWidget(self.search_lineedit_6)

        self.searchlinic_btn_6 = QPushButton(self.widget_3)
        self.searchlinic_btn_6.setObjectName(u"searchlinic_btn_6")
        self.searchlinic_btn_6.setStyleSheet(u"background-color: transparent;")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/icons8-search-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchlinic_btn_6.setIcon(icon8)
        self.searchlinic_btn_6.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.searchlinic_btn_6)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.location_combobox = QComboBox(self.widget_3)
        self.location_combobox.setObjectName(u"location_combobox")
        self.location_combobox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  16pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:4px;")

        self.horizontalLayout_10.addWidget(self.location_combobox)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.gridLayout_9.addLayout(self.verticalLayout_9, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.widget_3, 1, 0, 1, 1)

        self.request_header_2 = QLabel(self.search_pg)
        self.request_header_2.setObjectName(u"request_header_2")
        self.request_header_2.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"font-weight:bold;")
        self.request_header_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_12.addWidget(self.request_header_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.search_pg)
        self.request_pg = QWidget()
        self.request_pg.setObjectName(u"request_pg")
        self.gridLayout_7 = QGridLayout(self.request_pg)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.request_header = QLabel(self.request_pg)
        self.request_header.setObjectName(u"request_header")
        self.request_header.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"font-weight:bold;")
        self.request_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.request_header)

        self.request_box = QWidget(self.request_pg)
        self.request_box.setObjectName(u"request_box")
        self.request_box.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:4px;")
        self.gridLayout_6 = QGridLayout(self.request_box)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(30)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(50, 30, 50, 50)
        self.request_boxheader = QLabel(self.request_box)
        self.request_boxheader.setObjectName(u"request_boxheader")
        self.request_boxheader.setStyleSheet(u"background-color: transparent;\n"
"font: 75 20pt \"Bell MT\";\n"
"color: white;\n"
"font-weight:bold;")
        self.request_boxheader.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.request_boxheader)

        self.clinic_combobox = QComboBox(self.request_box)
        self.clinic_combobox.setObjectName(u"clinic_combobox")
        self.clinic_combobox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  16pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(0, 0, 0);\n"
"border-radius:4px;")
        self.clinic_combobox.setEditable(False)

        self.verticalLayout_8.addWidget(self.clinic_combobox)

        self.request_widget = QWidget(self.request_box)
        self.request_widget.setObjectName(u"request_widget")
        self.request_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_5 = QGridLayout(self.request_widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(80)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.date_label = QLabel(self.request_widget)
        self.date_label.setObjectName(u"date_label")
        self.date_label.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.date_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.date_label)

        self.dateEdit = QDateEdit(self.request_widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dateEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.time_label = QLabel(self.request_widget)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.time_label)

        self.timeEdit = QTimeEdit(self.request_widget)
        self.timeEdit.setObjectName(u"timeEdit")
        self.timeEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);")

        self.horizontalLayout_3.addWidget(self.timeEdit)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.requestdoctor_btn = QPushButton(self.request_widget)
        self.requestdoctor_btn.setObjectName(u"requestdoctor_btn")
        self.requestdoctor_btn.setStyleSheet(u"\n"
"	border-radius:8px;\n"
"	font: bold 20pt \"Bell MT\";\n"
"	border:1px solid grey;\n"
"	background-color:#02007a;\n"
"	color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_4.addWidget(self.requestdoctor_btn)


        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.request_widget)


        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.request_box)


        self.gridLayout_7.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(100)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(100, 0, 100, -1)
        self.day = QWidget(self.request_pg)
        self.day.setObjectName(u"day")
        self.day.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_8 = QGridLayout(self.day)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(50, -1, 0, -1)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_13.setContentsMargins(0, -1, -1, -1)
        self.label_6 = QLabel(self.day)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u":/images/images/images/sun.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout_13.addWidget(self.label_6)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.day)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.verticalLayout_11.addWidget(self.label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.dayprice_label = QLabel(self.day)
        self.dayprice_label.setObjectName(u"dayprice_label")
        self.dayprice_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_8.addWidget(self.dayprice_label)

        self.day_price = QLabel(self.day)
        self.day_price.setObjectName(u"day_price")
        self.day_price.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_8.addWidget(self.day_price)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.daystarttime_box = QHBoxLayout()
        self.daystarttime_box.setSpacing(0)
        self.daystarttime_box.setObjectName(u"daystarttime_box")
        self.daystarttime_label = QLabel(self.day)
        self.daystarttime_label.setObjectName(u"daystarttime_label")
        self.daystarttime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.daystarttime_box.addWidget(self.daystarttime_label)

        self.daystarttime = QLabel(self.day)
        self.daystarttime.setObjectName(u"daystarttime")
        self.daystarttime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.daystarttime_box.addWidget(self.daystarttime)


        self.verticalLayout_11.addLayout(self.daystarttime_box)

        self.dayendtime_box = QHBoxLayout()
        self.dayendtime_box.setSpacing(0)
        self.dayendtime_box.setObjectName(u"dayendtime_box")
        self.dayendtime_label = QLabel(self.day)
        self.dayendtime_label.setObjectName(u"dayendtime_label")
        self.dayendtime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.dayendtime_box.addWidget(self.dayendtime_label)

        self.dayendtime = QLabel(self.day)
        self.dayendtime.setObjectName(u"dayendtime")
        self.dayendtime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.dayendtime_box.addWidget(self.dayendtime)


        self.verticalLayout_11.addLayout(self.dayendtime_box)


        self.verticalLayout_13.addLayout(self.verticalLayout_11)


        self.gridLayout_8.addLayout(self.verticalLayout_13, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.day)

        self.night = QWidget(self.request_pg)
        self.night.setObjectName(u"night")
        self.night.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_10 = QGridLayout(self.night)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_5 = QLabel(self.night)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setPixmap(QPixmap(u":/images/images/images/moon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_5)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_8 = QLabel(self.night)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.verticalLayout_14.addWidget(self.label_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.nightprice_label = QLabel(self.night)
        self.nightprice_label.setObjectName(u"nightprice_label")
        self.nightprice_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_7.addWidget(self.nightprice_label)

        self.nightprice = QLabel(self.night)
        self.nightprice.setObjectName(u"nightprice")
        self.nightprice.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_7.addWidget(self.nightprice)


        self.verticalLayout_14.addLayout(self.horizontalLayout_7)

        self.nightstarttime_box = QHBoxLayout()
        self.nightstarttime_box.setSpacing(0)
        self.nightstarttime_box.setObjectName(u"nightstarttime_box")
        self.nightstarttime_label = QLabel(self.night)
        self.nightstarttime_label.setObjectName(u"nightstarttime_label")
        self.nightstarttime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.nightstarttime_box.addWidget(self.nightstarttime_label)

        self.nightstarttime = QLabel(self.night)
        self.nightstarttime.setObjectName(u"nightstarttime")
        self.nightstarttime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.nightstarttime_box.addWidget(self.nightstarttime)


        self.verticalLayout_14.addLayout(self.nightstarttime_box)

        self.nightendtime_box = QHBoxLayout()
        self.nightendtime_box.setSpacing(0)
        self.nightendtime_box.setObjectName(u"nightendtime_box")
        self.nightendtime_label = QLabel(self.night)
        self.nightendtime_label.setObjectName(u"nightendtime_label")
        self.nightendtime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.nightendtime_box.addWidget(self.nightendtime_label)

        self.nightendtime = QLabel(self.night)
        self.nightendtime.setObjectName(u"nightendtime")
        self.nightendtime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.nightendtime_box.addWidget(self.nightendtime)


        self.verticalLayout_14.addLayout(self.nightendtime_box)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.gridLayout_10.addLayout(self.verticalLayout_15, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.night)

        self.holiday = QWidget(self.request_pg)
        self.holiday.setObjectName(u"holiday")
        self.holiday.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_11 = QGridLayout(self.holiday)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(50, -1, -1, -1)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_4 = QLabel(self.holiday)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/images/images/images/publicholiday.png"))
        self.label_4.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_4)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_15 = QLabel(self.holiday)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.verticalLayout_16.addWidget(self.label_15)

        self.holidayprice_box = QHBoxLayout()
        self.holidayprice_box.setSpacing(0)
        self.holidayprice_box.setObjectName(u"holidayprice_box")
        self.holidayprice_label = QLabel(self.holiday)
        self.holidayprice_label.setObjectName(u"holidayprice_label")
        self.holidayprice_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.holidayprice_box.addWidget(self.holidayprice_label)

        self.holidayprice = QLabel(self.holiday)
        self.holidayprice.setObjectName(u"holidayprice")
        self.holidayprice.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.holidayprice_box.addWidget(self.holidayprice)


        self.verticalLayout_16.addLayout(self.holidayprice_box)

        self.holidaystarttime_box = QHBoxLayout()
        self.holidaystarttime_box.setSpacing(0)
        self.holidaystarttime_box.setObjectName(u"holidaystarttime_box")
        self.holidaystarttime_label = QLabel(self.holiday)
        self.holidaystarttime_label.setObjectName(u"holidaystarttime_label")
        self.holidaystarttime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.holidaystarttime_box.addWidget(self.holidaystarttime_label)

        self.holidaystarttime = QLabel(self.holiday)
        self.holidaystarttime.setObjectName(u"holidaystarttime")
        self.holidaystarttime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.holidaystarttime_box.addWidget(self.holidaystarttime)


        self.verticalLayout_16.addLayout(self.holidaystarttime_box)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.holidayendtime_label = QLabel(self.holiday)
        self.holidayendtime_label.setObjectName(u"holidayendtime_label")
        self.holidayendtime_label.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_6.addWidget(self.holidayendtime_label)

        self.holidayendtime = QLabel(self.holiday)
        self.holidayendtime.setObjectName(u"holidayendtime")
        self.holidayendtime.setStyleSheet(u"background-color: transparent;\n"
"font:  14pt \"Bell MT\";\n"
"color:#FFFFFF;\n"
"font-weight:bold;\n"
"border:transparent;")

        self.horizontalLayout_6.addWidget(self.holidayendtime)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)


        self.verticalLayout_17.addLayout(self.verticalLayout_16)


        self.gridLayout_11.addLayout(self.verticalLayout_17, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.holiday)


        self.gridLayout_7.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.request_pg)
        self.record_pg = QWidget()
        self.record_pg.setObjectName(u"record_pg")
        self.record_pg.setStyleSheet(u"background-color:#e5e5f1;")
        self.gridLayout_4 = QGridLayout(self.record_pg)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.record_header = QLabel(self.record_pg)
        self.record_header.setObjectName(u"record_header")
        self.record_header.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"font-weight:bold;")
        self.record_header.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.record_header)

        self.record_box = QWidget(self.record_pg)
        self.record_box.setObjectName(u"record_box")
        self.record_box.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:4px;")
        self.gridLayout_3 = QGridLayout(self.record_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setContentsMargins(50, 50, 50, 50)
        self.record_table = QTableWidget(self.record_box)
        self.record_table.setObjectName(u"record_table")
        self.record_table.setStyleSheet(u"QHeaderView:section{\n"
"		\n"
"	background-color: rgb(229, 229, 241);\n"
"}\n"
"QTableWidget{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	alternate-background-color: rgb(229, 229, 241);\n"
"}\n"
"")
        self.record_table.setAlternatingRowColors(True)
        self.record_table.setRowCount(0)
        self.record_table.horizontalHeader().setMinimumSectionSize(39)
        self.record_table.horizontalHeader().setDefaultSectionSize(150)
        self.record_table.horizontalHeader().setStretchLastSection(True)
        self.record_table.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.record_table, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.record_box)


        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.record_pg)
        self.profile_pg = QWidget()
        self.profile_pg.setObjectName(u"profile_pg")
        self.profile_pg.setStyleSheet(u"background-color:#e5e5f1;")
        self.gridLayout_13 = QGridLayout(self.profile_pg)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(15, 15, 15, 15)
        self.widget = QWidget(self.profile_pg)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.gridLayout_16 = QGridLayout(self.widget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.record_box_3 = QWidget(self.widget)
        self.record_box_3.setObjectName(u"record_box_3")
        self.record_box_3.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.477091, x2:1, y2:0.494, stop:0 rgba(47, 0, 116, 255), stop:1 rgba(255, 212, 212, 255));\n"
"	border-bottom-left-radius:2px;\n"
"	border-bottom-right-radius:2px;\n"
"	border-top-left-radius:30px;\n"
"	border-top-right-radius:30px;")
        self.gridLayout_17 = QGridLayout(self.record_box_3)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(150)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, -1, 50, -1)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(50)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.record_box_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background-color: transparent;")
        self.label_9.setPixmap(QPixmap(u":/images/images/images/user.png"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_9)

        self.profile_header_2 = QLabel(self.record_box_3)
        self.profile_header_2.setObjectName(u"profile_header_2")
        self.profile_header_2.setStyleSheet(u"background-color: transparent;\n"
"font:  40pt \"Bell MT\";\n"
"color: rgb(249, 206, 209);\n"
"font-weight:bold;")
        self.profile_header_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.profile_header_2)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_16)

        self.editprofile_btn_2 = QPushButton(self.record_box_3)
        self.editprofile_btn_2.setObjectName(u"editprofile_btn_2")
        self.editprofile_btn_2.setLayoutDirection(Qt.RightToLeft)
        self.editprofile_btn_2.setStyleSheet(u"\n"
"	border-radius:8px;\n"
"	font: bold 20pt \"Bell MT\";\n"
"	border:1px solid grey;\n"
"	background-color:#02007a;\n"
"	color: rgb(255, 255, 255);\n"
"")

        self.horizontalLayout_21.addWidget(self.editprofile_btn_2)


        self.gridLayout_17.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.record_box_3, 0, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.userEmail_label_2 = QLabel(self.widget)
        self.userEmail_label_2.setObjectName(u"userEmail_label_2")
        self.userEmail_label_2.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.userEmail_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.userEmail_label_2)

        self.userEmail_edit_2 = QTextEdit(self.widget)
        self.userEmail_edit_2.setObjectName(u"userEmail_edit_2")
        self.userEmail_edit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);\n"
"border-radius:4px;")

        self.verticalLayout_18.addWidget(self.userEmail_edit_2)


        self.verticalLayout_25.addLayout(self.verticalLayout_18)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(6)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.username_label_2 = QLabel(self.widget)
        self.username_label_2.setObjectName(u"username_label_2")
        self.username_label_2.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.username_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_38.addWidget(self.username_label_2)

        self.username_edit_2 = QTextEdit(self.widget)
        self.username_edit_2.setObjectName(u"username_edit_2")
        self.username_edit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);\n"
"border-radius:4px;")

        self.verticalLayout_38.addWidget(self.username_edit_2)


        self.verticalLayout_25.addLayout(self.verticalLayout_38)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setSpacing(6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.phone_label_2 = QLabel(self.widget)
        self.phone_label_2.setObjectName(u"phone_label_2")
        self.phone_label_2.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.phone_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_24.addWidget(self.phone_label_2)

        self.phone_edit_2 = QTextEdit(self.widget)
        self.phone_edit_2.setObjectName(u"phone_edit_2")
        self.phone_edit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);\n"
"border-radius:4px;")

        self.verticalLayout_24.addWidget(self.phone_edit_2)


        self.verticalLayout_39.addLayout(self.verticalLayout_24)


        self.verticalLayout_25.addLayout(self.verticalLayout_39)


        self.horizontalLayout_15.addLayout(self.verticalLayout_25)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(50, 50, 50, 50)
        self.address_label_2 = QLabel(self.widget)
        self.address_label_2.setObjectName(u"address_label_2")
        self.address_label_2.setStyleSheet(u"background-color: transparent;\n"
"font: 20pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.address_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_26.addWidget(self.address_label_2)

        self.address_edit_2 = QTextEdit(self.widget)
        self.address_edit_2.setObjectName(u"address_edit_2")
        self.address_edit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font:  20pt \"Bell MT\";\n"
"border:1px solid #c8c8c8;\n"
"color: rgb(40, 40, 40);\n"
"border-radius:4px;")

        self.verticalLayout_26.addWidget(self.address_edit_2)


        self.horizontalLayout_15.addLayout(self.verticalLayout_26)


        self.gridLayout_16.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.widget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.profile_pg)
        self.search_pg2 = QWidget()
        self.search_pg2.setObjectName(u"search_pg2")
        self.gridLayout_24 = QGridLayout(self.search_pg2)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.widget_5 = QWidget(self.search_pg2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setStyleSheet(u"background-color: rgb(2, 0, 122);\n"
"	border-radius: 8px;")
        self.gridLayout_20 = QGridLayout(self.widget_5)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.back_btn = QPushButton(self.widget_5)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setStyleSheet(u"background-color: transparent;")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/icons8-back-64.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.back_btn.setIcon(icon9)
        self.back_btn.setIconSize(QSize(50, 50))

        self.horizontalLayout_17.addWidget(self.back_btn)

        self.clinicname_label = QLabel(self.widget_5)
        self.clinicname_label.setObjectName(u"clinicname_label")
        self.clinicname_label.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.clinicname_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.clinicname_label)

        self.horizontalLayout_17.setStretch(1, 1)

        self.gridLayout_20.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_4 = QWidget(self.search_pg2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(2, 0, 122);\n"
"	border-radius: 8px;")
        self.gridLayout_19 = QGridLayout(self.widget_4)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.clinicimage = QLabel(self.widget_4)
        self.clinicimage.setObjectName(u"clinicimage")

        self.horizontalLayout_11.addWidget(self.clinicimage)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.about_us_3 = QLabel(self.widget_4)
        self.about_us_3.setObjectName(u"about_us_3")
        self.about_us_3.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.about_us_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_27.addWidget(self.about_us_3)

        self.clinicdetail_label = QTextEdit(self.widget_4)
        self.clinicdetail_label.setObjectName(u"clinicdetail_label")
        self.clinicdetail_label.setStyleSheet(u"background-color: transparent;\n"
"font: 18pt \"Bell MT\";\n"
"color: rgb(255, 255, 255);\n"
"font-weight:bold;")
        self.clinicdetail_label.setReadOnly(True)

        self.verticalLayout_27.addWidget(self.clinicdetail_label)

        self.viewmap = QPushButton(self.widget_4)
        self.viewmap.setObjectName(u"viewmap")
        self.viewmap.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 14pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"font-weight:bold;")

        self.verticalLayout_27.addWidget(self.viewmap)


        self.horizontalLayout_11.addLayout(self.verticalLayout_27)


        self.gridLayout_19.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)


        self.gridLayout_24.addWidget(self.widget_4, 1, 0, 1, 1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.ourdoctor = QLabel(self.search_pg2)
        self.ourdoctor.setObjectName(u"ourdoctor")
        self.ourdoctor.setStyleSheet(u"background-color: transparent;\n"
"font: 75 24pt \"Bell MT\";\n"
"color: rgb(0, 0, 0);\n"
"font-weight:bold;")
        self.ourdoctor.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.ourdoctor)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.doctor1 = QWidget(self.search_pg2)
        self.doctor1.setObjectName(u"doctor1")
        self.doctor1.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_22 = QGridLayout(self.doctor1)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.doctorimg1 = QLabel(self.doctor1)
        self.doctorimg1.setObjectName(u"doctorimg1")

        self.gridLayout_22.addWidget(self.doctorimg1, 0, 0, 1, 1)

        self.doctordetail_label1 = QLabel(self.doctor1)
        self.doctordetail_label1.setObjectName(u"doctordetail_label1")
        self.doctordetail_label1.setStyleSheet("color: rgb(255, 255, 255);\n"
         "font:  14pt \"Bell MT\";\n"
         "font-weight:bold;")
        self.gridLayout_22.addWidget(self.doctordetail_label1, 0, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.doctor1)

        self.doctor3 = QWidget(self.search_pg2)
        self.doctor3.setObjectName(u"doctor3")
        self.doctor3.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_21 = QGridLayout(self.doctor3)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.doctorimg3 = QLabel(self.doctor3)
        self.doctorimg3.setObjectName(u"doctorimg3")

        self.gridLayout_21.addWidget(self.doctorimg3, 1, 0, 1, 1)

        self.doctordetail_label3 = QLabel(self.doctor3)
        self.doctordetail_label3.setObjectName(u"doctordetail_label3")
        self.doctordetail_label3.setStyleSheet("color: rgb(255, 255, 255);\n"
         "font:  14pt \"Bell MT\";\n"
         "font-weight:bold;")
        self.gridLayout_21.addWidget(self.doctordetail_label3, 1, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.doctor3)

        self.doctor2 = QWidget(self.search_pg2)
        self.doctor2.setObjectName(u"doctor2")
        self.doctor2.setStyleSheet(u"background-color:#02007a;\n"
"border-radius:30px;\n"
"")
        self.gridLayout_23 = QGridLayout(self.doctor2)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.doctorimg2 = QLabel(self.doctor2)
        self.doctorimg2.setObjectName(u"doctorimg2")

        self.gridLayout_23.addWidget(self.doctorimg2, 0, 0, 1, 1)

        self.doctordetail_label2 = QLabel(self.doctor2)
        self.doctordetail_label2.setObjectName(u"doctordetail_label2")
        self.doctordetail_label2.setStyleSheet("color: rgb(255, 255, 255);\n"
         "font:  14pt \"Bell MT\";\n"
         "font-weight:bold;")
        self.gridLayout_23.addWidget(self.doctordetail_label2, 0, 1, 1, 1)


        self.horizontalLayout_14.addWidget(self.doctor2)


        self.verticalLayout_28.addLayout(self.horizontalLayout_14)


        self.gridLayout_24.addLayout(self.verticalLayout_28, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.search_pg2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_6, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.hide_btn_2.clicked["bool"].connect(self.sidebar.setVisible)
        self.hide_btn.clicked["bool"].connect(self.sidebar_2.setVisible)
        self.hide_btn_2.clicked["bool"].connect(self.sidebar_2.setHidden)
        self.hide_btn.clicked["bool"].connect(self.sidebar.setHidden)
        self.home_btn.toggled.connect(self.home_btn_2.setChecked)
        self.search_btn.toggled.connect(self.search_btn_2.setChecked)
        self.request_btn.toggled.connect(self.request_btn_2.setChecked)
        self.record_btn.toggled.connect(self.record_btn_2.setChecked)
        self.record_btn_2.toggled.connect(self.record_btn.setChecked)
        self.request_btn_2.toggled.connect(self.request_btn.setChecked)
        self.search_btn_2.toggled.connect(self.search_btn.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn.setChecked)
        self.quit_btn.clicked.connect(MainWindow.close)
        self.quit_btn_2.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_logo_2.setText("")
        self.hide_btn_2.setText("")
        self.home_btn_2.setText("")
        self.search_btn_2.setText("")
        self.request_btn_2.setText("")
        self.record_btn_2.setText("")
        self.profile_btn_2.setText("")
        self.quit_btn_2.setText("")
        self.app_logo.setText("")
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"Call A Doctor", None))
        self.hide_btn.setText(QCoreApplication.translate("MainWindow", u"   Hide", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"   Home", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"   Search", None))
        self.request_btn.setText(QCoreApplication.translate("MainWindow", u"   Appoinment", None))
        self.record_btn.setText(QCoreApplication.translate("MainWindow", u"   Record", None))
        self.profile_btn.setText(QCoreApplication.translate("MainWindow", u"   Profile", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"   Quit", None))
        self.home_header_3.setText(QCoreApplication.translate("MainWindow", u"Welcome to Call A Doctor", None))
        self.home_header_4.setText(QCoreApplication.translate("MainWindow", u"We Provide 24 hours Professional Medical Care to Your Doorstep", None))
        self.about_us_2.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.textEdit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bell MT'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Our experience has shown us that treating those who need medical  services  in  their  home  setting  improves  health outcomes,  reduces  patient  stress,  and  provides  comfort. The health of our patients is always  our  priority. Our doctors work  around  the clock to provide the very best at home to patients. Our doctors treat children, adults, and the elderly with care and compassion. Whether you are at home, in a hotel or in an aged care facility, wherever you are, we can treat you.</span></p></body></html>", None))
        self.label_3.setText("")
        self.ourpartner_2.setText(QCoreApplication.translate("MainWindow", u"Our Partners", None))
        self.label_2.setText("")
        ___qtablewidgetitem = self.search_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Clinic's Name", None));
        ___qtablewidgetitem1 = self.search_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.search_lineedit_6.setText("")
        self.search_lineedit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Clinic's Name, Address...", None))
        self.searchlinic_btn_6.setText("")
        self.request_header_2.setText(QCoreApplication.translate("MainWindow", u"Search Clinic", None))
        self.request_header.setText(QCoreApplication.translate("MainWindow", u"Appointment for a doctor?", None))
        self.request_boxheader.setText(QCoreApplication.translate("MainWindow", u"Call A Doctor offers a variety of packages, \n"
"tailored to fit your needs at affordable prices.", None))
        self.date_label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.time_label.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.requestdoctor_btn.setText(QCoreApplication.translate("MainWindow", u"Appoinment", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Day Package", None))
        self.dayprice_label.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.day_price.setText(QCoreApplication.translate("MainWindow", u"RM200", None))
        self.daystarttime_label.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.daystarttime.setText(QCoreApplication.translate("MainWindow", u"08:00", None))
        self.dayendtime_label.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.dayendtime.setText(QCoreApplication.translate("MainWindow", u"20:00", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Night Package", None))
        self.nightprice_label.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.nightprice.setText(QCoreApplication.translate("MainWindow", u"RM300", None))
        self.nightstarttime_label.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.nightstarttime.setText(QCoreApplication.translate("MainWindow", u"20:00", None))
        self.nightendtime_label.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.nightendtime.setText(QCoreApplication.translate("MainWindow", u"08:00", None))
        self.label_4.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Public Holiday Package", None))
        self.holidayprice_label.setText(QCoreApplication.translate("MainWindow", u"Price:", None))
        self.holidayprice.setText(QCoreApplication.translate("MainWindow", u"RM500", None))
        self.holidaystarttime_label.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.holidaystarttime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.holidayendtime_label.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.holidayendtime.setText(QCoreApplication.translate("MainWindow", u"24:00", None))
        self.record_header.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.label_9.setText("")
        self.profile_header_2.setText(QCoreApplication.translate("MainWindow", u"Welcome to Profile Page", None))
        self.editprofile_btn_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.userEmail_label_2.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.username_label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.phone_label_2.setText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.phone_edit_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bell MT'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.phone_edit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Please fill in", None))
        self.address_label_2.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.back_btn.setText("")
        self.clinicname_label.setText(QCoreApplication.translate("MainWindow", u"Clinic Name", None))
        self.clinicimage.setText("")
        self.about_us_3.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.clinicdetail_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Bell MT'; font-size:18pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Our experience has shown us that treating those who need medical  services  in  their  home  setting  improves  health outcomes,  reduces  patient  stress,  and  provides  comfort. The health of our patients is always  our  priority. Our doctors work  around  the clock to provide the very best at home to patients. Our doctors treat children, adults, and the elderly with care and compassion. Whether you are at home, in a hotel or in an aged care facility, wherever you are, we can treat you.</span></p></body></html>", None))
        self.viewmap.setText(QCoreApplication.translate("MainWindow", u"View In Google Map", None))
        self.ourdoctor.setText(QCoreApplication.translate("MainWindow", u"Our Doctors", None))
        self.doctorimg1.setText("")
        self.doctordetail_label1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.doctorimg3.setText("")
        self.doctordetail_label3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.doctorimg2.setText("")
        self.doctordetail_label2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

