from PySide6 import QtCore, QtGui, QtWidgets
from doctor_utilities import login
from draggable_widget import DraggableWidget


#   Creates window       
class Login_Form(QtWidgets.QWidget): # Change to QWidget, not QMainWindow
    login_successful = QtCore.Signal(bool, QtWidgets.QMainWindow)

    def __init__(self, parent = None):
        super(Login_Form, self).__init__(parent)
        self.setupUi(self)
        
        # Add search path for resources
        QtCore.QDir.addSearchPath("resources","../resources/")


    def setupUi(self, Login_Form):
        Form = Login_Form
        print("setupUi Login UI")
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
        
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(int(20 * scaling_factor), int(0 * scaling_factor), int(671 * scaling_factor), int(491 * scaling_factor)))
        self.widget.setObjectName("widget")

        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(int(0 * scaling_factor), int(0 * scaling_factor), int(310 * scaling_factor), int(491 * scaling_factor)))
        self.label.setStyleSheet("border-image: url(:/resources/login-background.jpg);\n"
                                 "border-top-left-radius: {}px;\n"
                                 "border-bottom-left-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(int(0 * scaling_factor), int(0 * scaling_factor), int(310 * scaling_factor), int(491 * scaling_factor)))
        self.label_2.setStyleSheet("background-color: rgba(0,0,0,80);\n"
                                   "border-top-left-radius: {}px;\n"
                                   "border-bottom-left-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(int(310 * scaling_factor), int(0 * scaling_factor), int(351 * scaling_factor), int(490 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(9 * scaling_factor))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:rgba(255,255,255,255);\n"
                                   "border-top-right-radius: {}px;\n"
                                   "border-bottom-right-radius: {}px;".format(int(50 * scaling_factor), int(50 * scaling_factor)))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(int(450 * scaling_factor), int(20 * scaling_factor), int(100 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(15 * scaling_factor))
        font.setBold(True)
        font.setWeight(QtGui.QFont.Weight.Bold)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(87,161,248,200);")
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(140 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border:none;\n"
                                    "border-bottom:2px solid rgba(46,82,101,200);\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit.setObjectName("lineEdit")
        

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(200 * scaling_factor), int(190 * scaling_factor), int(40 * scaling_factor)))
        font = QtGui.QFont()
        font.setPointSize(int(10 * scaling_factor))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border:none;\n"
                                      "border-bottom:2px solid rgba(46,82,101,200);\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "padding-bottom:{}px;\n""".format(int(7 * scaling_factor)))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password) # Set echo mode to Password


        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(int(400 * scaling_factor), int(338 * scaling_factor), int(190 * scaling_factor), int(30 * scaling_factor)))
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:rgba(87,161,248,200);\n"
                                      "color:rgba(255,255,255,200);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.signin)
        
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(int(410 * scaling_factor), int(410 * scaling_factor), int(140 * scaling_factor), int(16 * scaling_factor)))
        font.setPointSize(int(7 * scaling_factor))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(int(425 * scaling_factor), int(450 * scaling_factor), int(125 * scaling_factor), int(16 * scaling_factor)))
        font.setPointSize(int(6 * scaling_factor))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.toolButton = QtWidgets.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(int(520 * scaling_factor), int(410 * scaling_factor), int(43 * scaling_factor), int(17 * scaling_factor)))
        font.setPointSize(int(7 * scaling_factor))
        self.toolButton.setFont(font)
        self.toolButton.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "color:rgba(87,161,248,200);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton.clicked.connect(self.show_register_page)

        # self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        # self.toolButton_2.setGeometry(QtCore.QRect(int(506 * scaling_factor), int(250 * scaling_factor), int(97 * scaling_factor), int(21 * scaling_factor)))
        # font.setPointSize(int(6 * scaling_factor))
        # self.toolButton_2.setFont(font)
        # self.toolButton_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        #                                 "color:rgba(87,161,248,200);")
        # self.toolButton_2.setObjectName("toolButton_2")

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(int(430 * scaling_factor), int(450 * scaling_factor), int(125 * scaling_factor), int(16 * scaling_factor)))
        font.setPointSize(int(8 * scaling_factor))
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        
        icon_size = QtCore.QSize(24,24)
        self.toggle_button = QtWidgets.QPushButton(self.widget)
        self.toggle_button.setGeometry(QtCore.QRect(int(600 * scaling_factor), int(206 * scaling_factor), int(30 * scaling_factor), int(30 * scaling_factor)))
        self.toggle_button.setStyleSheet("border: 1px solid transparent;")
        self.toggle_button.setIcon(QtGui.QIcon(":/resources/show_password.png"))  # Set initial icon
        self.toggle_button.setIconSize(icon_size)
        self.toggle_button.setCheckable(True)
        self.toggle_button.setChecked(False)
        self.toggle_button.clicked.connect(self.toggle_password_visibility)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit, self.lineEdit_2)
        Form.setTabOrder(self.lineEdit_2, self.toggle_button)
        Form.setTabOrder(self.toggle_button, self.toolButton)
        Form.setTabOrder(self.toolButton, self.pushButton)
        Form.setTabOrder(self.pushButton, self.toolButton)

        self.lineEdit.returnPressed.connect(self.pushButton.click)
        self.lineEdit_2.returnPressed.connect(self.pushButton.click)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login"))
        self.label_4.setText(_translate("Form", "SIGN IN"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Email"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Sign In"))
        self.label_5.setText(_translate("Form", "Don\'t have an account?"))
        self.toolButton.setText(_translate("Form", "Sign Up"))
        #self.toolButton_2.setText(_translate("Form", "Forgot Password?"))


    def signin(self):
        email = self.lineEdit.text().lower(); password = self.lineEdit_2.text()

        success = login(self.parent(), email, password)
        self.login_successful.emit(success, self.parent()) # Emit tuple (success, login_controller)


    def show_register_page(self):
        # Get the top-level LoginController instance
        controller = self.parent().parent()  
        controller.show_register_form()
        self.lineEdit.clear()
        self.lineEdit_2.clear()


    def toggle_password_visibility(self):
        if self.toggle_button.isChecked():
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)                     # Display password in plaintext
            self.toggle_button.setIcon(QtGui.QIcon(":/resources/hide_password.png"))
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)                   # Display password using '*'
            self.toggle_button.setIcon(QtGui.QIcon(":/resources/show_password.png"))