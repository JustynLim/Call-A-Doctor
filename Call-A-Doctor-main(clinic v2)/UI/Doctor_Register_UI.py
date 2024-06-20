from PySide6 import QtCore, QtGui, QtWidgets
#from PyQt5 import QtCore, QtGui, QtWidgets
from utilities import register#, register_display_status
import webbrowser


# #  Allows window to be dragged around the screen
# class DraggableWidget(QtWidgets.QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._mousePressed = False
#         self._mousePos = None
#         self._startGeometry = None

#     def mousePressEvent(self, event):
#         if event.button() == QtCore.Qt.LeftButton:
#             self._mousePressed = True
#             self._mousePos = event.globalPos()
#             self._startGeometry = self.geometry()

#     def mouseMoveEvent(self, event):
#         if self._mousePressed:
#             delta = event.globalPos() - self._mousePos
#             self.move(self._startGeometry.topLeft() + delta)

#     def mouseReleaseEvent(self, event):
#         if event.button() == QtCore.Qt.LeftButton:
#             self._mousePressed = False

            
class Register_Form(QtWidgets.QWidget):
    registration_finished = QtCore.Signal(int)  # Signal for registration status

    def __init__(self,parent = None):
        #super().__init__(parent)
        super().__init__()
        self.setupUi(self)

        # Add search path for resources
        QtCore.QDir.addSearchPath("resources","../resources/")

        self.pushButton_2.clicked.connect(self.signup)
        #global email_input2, password_input2, confirm_password_input, activation_code_input
        #email_input2 = None; password_input2 = None; confirm_password_input = None; activation_code_input = None


    def setupUi(self, Form):
        Form.setObjectName("Form")

        # Dynamically adjust window size based on the screen's DPI
        screen = QtWidgets.QApplication.primaryScreen()
        dpi = screen.physicalDotsPerInch()
        scaling_factor = dpi / 96.0  # Standard DPI is 96
        Form.resize(int(750 * scaling_factor), int(540 * scaling_factor))
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setGeometry(QtCore.QRect(int(20 * scaling_factor), int(0 * scaling_factor), int(671 * scaling_factor), int(491 * scaling_factor)))
        self.widget_2.setObjectName("widget_2")
        
        self.label_13 = QtWidgets.QLabel(self.widget_2)
        self.label_13.setGeometry(QtCore.QRect(int(0 * scaling_factor), int(0 * scaling_factor), int(310 * scaling_factor), int(491 * scaling_factor)))
        self.label_13.setStyleSheet("border-image: url(:/newPrefix/resources/register-background.jpg);\n"
                                    "border-top-left-radius: {}px;\n"
                                    "border-bottom-left-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.widget_2)
        self.label_14.setGeometry(QtCore.QRect(int(0 * scaling_factor), int(0 * scaling_factor), int(310 * scaling_factor), int(491 * scaling_factor)))
        self.label_14.setStyleSheet("background-color: rgba(0,0,0,80);\n"
                                    "border-top-left-radius: {}px;\n"
                                    "border-bottom-left-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.widget_2)
        self.label_15.setGeometry(QtCore.QRect(int(310 * scaling_factor), int(0 * scaling_factor), int(351 * scaling_factor), int(490 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(9 * scaling_factor))
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                    "border-top-right-radius: {}px;\n"
                                    "border-bottom-right-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.widget_2)
        self.label_16.setGeometry(QtCore.QRect(int(450 * scaling_factor), int(20 * scaling_factor), int(100 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(15 * scaling_factor))
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        #font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgba(87,161,248,200);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(100 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(160 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n""color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(360 * scaling_factor), int(190 * scaling_factor), int(30 * scaling_factor)))
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgba(87,161,248,200);\n"
                                        "color:rgba(255,255,255,200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signup)

        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(int(410 * scaling_factor), int(410 * scaling_factor), int(140 * scaling_factor), int(16 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(7 * scaling_factor))
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_5.setGeometry(QtCore.QRect(int(530 * scaling_factor), int(410 * scaling_factor), int(42 * scaling_factor), int(17 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(7 * scaling_factor))
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "color:rgba(87,161,248,200);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.show_login_page)

        # Not a member yet?
        self.toolButton_6 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_6.setGeometry(QtCore.QRect(int(500 * scaling_factor), int(325 * scaling_factor), int(100 * scaling_factor), int(21 * scaling_factor)))
        font.setPointSize(int(6 * scaling_factor))
        self.toolButton_6.setFont(font)
        self.toolButton_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "color:rgba(87,161,248,200);")
        self.toolButton_6.setObjectName("toolButton")
        self.toolButton_6.clicked.connect(lambda: webbrowser.open("https://forms.gle/XjGP3GMHqQjtgTjG6"))

        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(int(410 * scaling_factor), int(450 * scaling_factor), int(170 * scaling_factor), int(16 * scaling_factor)))
        font.setPointSize(int(6 * scaling_factor))
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(220 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)

        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(280 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setGeometry(QtCore.QRect(int(600 * scaling_factor), int(165 * scaling_factor), int(24 * scaling_factor), int(24 * scaling_factor)))
        self.checkBox_2.setStyleSheet("QCheckBox::indicator:checked{image: url(:/newPrefix/resources/hide_password.png);}\n"
                                      "QCheckBox::indicator:unchecked{image: url(:/newPrefix/resources/show_password.png);}")
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.stateChanged.connect(lambda state: self.toggle_password_visibility(state, self.lineEdit_6))

        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_3.setGeometry(QtCore.QRect(int(600 * scaling_factor), int(225 * scaling_factor), int(24 * scaling_factor), int(24 * scaling_factor)))
        self.checkBox_3.setStyleSheet("QCheckBox::indicator:checked{image: url(:/newPrefix/resources/hide_password.png);}\n"
                                      "QCheckBox::indicator:unchecked{image: url(:/newPrefix/resources/show_password.png);}")
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_3.stateChanged.connect(lambda state: self.toggle_password_visibility(state, self.lineEdit_7))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        Form.setTabOrder(self.lineEdit_6, self.checkBox_2)
        Form.setTabOrder(self.checkBox_2, self.lineEdit_7)
        Form.setTabOrder(self.lineEdit_7, self.checkBox_3)
        Form.setTabOrder(self.checkBox_3, self.lineEdit_8)
        Form.setTabOrder(self.lineEdit_8, self.toolButton_5)
        Form.setTabOrder(self.toolButton_5, self.pushButton_2)
        Form.setTabOrder(self.pushButton_2, self.toolButton_6)

        self.lineEdit_5.returnPressed.connect(self.pushButton_2.click)
        self.lineEdit_6.returnPressed.connect(self.pushButton_2.click)
        self.lineEdit_7.returnPressed.connect(self.pushButton_2.click)
        self.lineEdit_8.returnPressed.connect(self.pushButton_2.click)


        # # Set tab order for lineEdits
        # QtWidgets.QWidget.setTabOrder(self.lineEdit_5, self.lineEdit_6)  # Email -> Password
        # QtWidgets.QWidget.setTabOrder(self.lineEdit_6, self.lineEdit_7)  # Password -> Confirm Password
        # QtWidgets.QWidget.setTabOrder(self.lineEdit_7, self.lineEdit_8)  # Confirm Password -> Activation Code
        # QtWidgets.QWidget.setTabOrder(self.lineEdit_8, self.lineEdit_5)  # Activation Code -> Email (cycle back)

        # self.lineEdit_5.setFocus()

    def show_login_page(self):
        self.parent().parent().show_login_form()

    def toggle_password_visibility(self, state, lineEdit):
        if state == QtCore.Qt.Checked:
            lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)  # Display password in plaintext format
        else:
            lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)  # Display password using '*'

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "SIGN UP"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Email"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "Activation Code"))
        self.pushButton_2.setText(_translate("Form", "Sign Up"))
        self.toolButton_6.setText(_translate("Form", "Not a member yet?"))
        self.label_17.setText(_translate("Form", "Already have an account?"))
        self.toolButton_5.setText(_translate("Form", "Sign In"))

    def signup(self):
        email = self.lineEdit_5.text().lower(); password = self.lineEdit_6.text(); confirm_password = self.lineEdit_7.text(); activation_code = self.lineEdit_8.text()
        # email_input2 = self.lineEdit_5.text().lower(); password_input2 = self.lineEdit_6.text(); confirm_password_input = self.lineEdit_7.text(); activation_code_input = self.lineEdit_8.text()
        
        status = -1

        if not email:
            status = 0

        elif not password or not confirm_password:
            status = 1
            
        elif password != confirm_password:
            status = 2

        elif not activation_code:
            status = 4

        if status != -1:
            self.registration_finished.emit(status)
            #register_display_status(self, status)
            return
        
        #print(f"Registering email: {email_input2}")
        status = register(email, password, activation_code)
        self.registration_finished.emit(status)
        #register_display_status(self, status)

        
    def show_login_page(self):
        self.parent().show_login_form()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()