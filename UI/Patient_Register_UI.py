from PySide6 import QtCore, QtGui, QtWidgets
from doctor_utilities import register
from draggable_widget import DraggableWidget
import webbrowser

            
class Register_Form(QtWidgets.QWidget):
    registration_finished = QtCore.Signal(int)  # Signal for registration status

    def __init__(self,parent = None):
        super().__init__(parent)
        # super().__init__()
        self.setupUi(self)
        self.draggable_widget = DraggableWidget(self)


        # Add search path for resources
        QtCore.QDir.addSearchPath("resources","../resources/")



    def setupUi(self, Form):
        print("setupUi Register UI")
        print(self.layout())
        if not Form.objectName():
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
        self.label_13.setStyleSheet("border-image: url(:/resources/register-background.jpg);\n"
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
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:rgba(87,161,248,200);")
        self.label_16.setObjectName("label_16")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(100 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(140 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_4.setObjectName("lineEdit_4")


        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(180 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
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
        self.lineEdit_6.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(220 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
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
        self.pushButton_2.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(350 * scaling_factor), int(190 * scaling_factor), int(30 * scaling_factor)))
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:rgba(87,161,248,200);\n"
                                        "color:rgba(255,255,255,200);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.signup)

        self.label_17 = QtWidgets.QLabel(self.widget_2)
        self.label_17.setGeometry(QtCore.QRect(int(410 * scaling_factor), int(400 * scaling_factor), int(140 * scaling_factor), int(16 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(7 * scaling_factor))
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_5.setGeometry(QtCore.QRect(int(530 * scaling_factor), int(400 * scaling_factor), int(42 * scaling_factor), int(17 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(7 * scaling_factor))
        self.toolButton_5.setFont(font)
        self.toolButton_5.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                        "color:rgba(87,161,248,200);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_5.clicked.connect(self.show_login_page)

        self.label_18 = QtWidgets.QLabel(self.widget_2)
        self.label_18.setGeometry(QtCore.QRect(int(410 * scaling_factor), int(450 * scaling_factor), int(170 * scaling_factor), int(16 * scaling_factor)))
        font.setPointSize(int(6 * scaling_factor))
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(260 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
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

        # self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_2)
        # self.lineEdit_8.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(280 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        # font = QtGui.QFont()
        # font.setPointSize(int(10 * scaling_factor))
        # self.lineEdit_8.setFont(font)
        # self.lineEdit_8.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        #                               "border:none;\n"
        #                               "border-bottom:2px solid rgba(46,82,101,200);\n"
        #                               "color:rgba(0,0,0,240);\n"
        #                               "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        # self.lineEdit_8.setObjectName("lineEdit_8")

        icon_size = QtCore.QSize(24,24)

        self.toggle_button_2 = QtWidgets.QPushButton(self.widget_2)
        self.toggle_button_2.setGeometry(QtCore.QRect(int(600 * scaling_factor), int(165 * scaling_factor), int(30 * scaling_factor), int(30 * scaling_factor)))
        self.toggle_button_2.setStyleSheet("border: 1px solid transparent;")
        self.toggle_button_2.setIcon(QtGui.QIcon(":/resources/show_password.png"))  # Set initial icon
        self.toggle_button_2.setIconSize(icon_size)
        self.toggle_button_2.setCheckable(True)
        self.toggle_button_2.setChecked(False)
        self.toggle_button_2.clicked.connect(self.toggle_password_visibility)


        self.toggle_button_3 = QtWidgets.QPushButton(self.widget_2)
        self.toggle_button_3.setGeometry(QtCore.QRect(int(600 * scaling_factor), int(225 * scaling_factor), int(30 * scaling_factor), int(30 * scaling_factor)))
        self.toggle_button_3.setStyleSheet("border: 1px solid transparent;")
        self.toggle_button_3.setIcon(QtGui.QIcon(":/resources/show_password.png"))  # Set initial icon
        self.toggle_button_3.setIconSize(icon_size)
        self.toggle_button_3.setCheckable(True)
        self.toggle_button_3.setChecked(False)
        self.toggle_button_3.clicked.connect(self.toggle_password_visibility)
        self.retranslateUi(Form)
        
        # Set tab order (come back ltr)
        # QtCore.QMetaObject.connectSlotsByName(Form)
        # Form.setTabOrder(self.lineEdit_4, self.lineEdit_6)
        # Form.setTabOrder(self.lineEdit_6, self.toggle_button_2)
        # Form.setTabOrder(self.toggle_button_2, self.lineEdit_7)
        # Form.setTabOrder(self.lineEdit_7, self.toggle_button_3)
        # Form.setTabOrder(self.toggle_button_3, self.lineEdit_8)
        # Form.setTabOrder(self.lineEdit_8, self.pushButton_2)
        # Form.setTabOrder(self.pushButton_2, self.toolButton_5)


        self.lineEdit_4.returnPressed.connect(self.pushButton_2.click)
        self.lineEdit_6.returnPressed.connect(self.pushButton_2.click)
        self.lineEdit_7.returnPressed.connect(self.pushButton_2.click)
        #self.lineEdit_8.returnPressed.connect(self.pushButton_2.click)


    def show_login_page(self):
        # Get the top-level LoginController instance
        controller = self.parent().parent()  
        controller.show_login_form()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_16.setText(_translate("Form", "SIGN UP"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Email"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Address"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "Confirm Password"))
        #self.lineEdit_8.setPlaceholderText(_translate("Form", "Address"))
        self.pushButton_2.setText(_translate("Form", "Sign Up"))
        #self.toolButton_6.setText(_translate("Form", "Not a member yet?"))
        self.label_17.setText(_translate("Form", "Already have an account?"))
        self.toolButton_5.setText(_translate("Form", "Sign In"))

    def signup(self):
        email = self.lineEdit_4.text().lower(); password = self.lineEdit_6.text(); confirm_password = self.lineEdit_7.text(); activation_code = self.lineEdit_8.text()
        
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
            return
        
        #print(f"Registering email: {email_input2}")
        print("Called from Register_UI")
        status = register(email, password, activation_code)
        self.registration_finished.emit(status)

        
    def show_login_page(self):
        controller = self.parent().parent()
        controller.show_login_form()
        self.lineEdit_4.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()

    def toggle_password_visibility(self):
        sender = self.sender()
        if sender == self.toggle_button_2:
            line_edit = self.lineEdit_6
        
        elif sender == self.toggle_button_3:
            line_edit = self.lineEdit_7
        
        else:
            return

        if self.toggle_button_2.isChecked():
            line_edit.setEchoMode(QtWidgets.QLineEdit.Normal)                               # Display password in plaintext
            self.toggle_button_2.setIcon(QtGui.QIcon(":/resources/hide_password.png"))
        else:
            line_edit.setEchoMode(QtWidgets.QLineEdit.Password)                             # Display password using '*'
            self.toggle_button_2.setIcon(QtGui.QIcon(":/resources/show_password.png"))