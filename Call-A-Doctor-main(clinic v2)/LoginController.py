from PySide6 import QtCore, QtGui, QtWidgets
from utilities import login, register
from UI.Login_UI import Login_Form
from UI.Register_UI import Register_Form
import webbrowser
from draggable_widget import DraggableWidget

class LoginController(QtWidgets.QMainWindow):
    registration_finished = QtCore.Signal(int)
    show_main_app_signal = QtCore.Signal(bool)

    def __init__(self):
        super().__init__()
        self.login_finished = QtCore.Signal(bool)
        self.registration_finished = QtCore.Signal(int)

    def setupUI(self, screen):
        print("Creating widgets in LoginController")

        dpi = screen.logicalDotsPerInch()
        scaling_factor = dpi / 96.0  # Standard DPI is 96
        self.resize(int(750 * scaling_factor), int(540 * scaling_factor))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.draggable_widget = DraggableWidget(self)

        self.central_widget = QtWidgets.QWidget(self)
        print("Widgets created")

        self.login_form = Login_Form(self.central_widget)
        self.register_form = Register_Form(self.central_widget)

        self.stacked_layout = QtWidgets.QStackedLayout(self.central_widget)
        self.stacked_layout.addWidget(self.login_form)
        self.stacked_layout.addWidget(self.register_form)

        self.setCentralWidget(self.draggable_widget)

        self.register_form.registration_finished.connect(self.display_registration_status)

        self.show_login_form()

        self.login_form.pushButton.clicked.connect(self.handle_login)
        self.login_form.login_successful.connect(self.login_finished)
        self.register_form.toolButton_5.clicked.connect(self.show_login_form)
        self.register_form.pushButton_2.clicked.connect(self.handle_registration)
        self.login_form.toolButton.clicked.connect(self.show_register_form)

        self.login_form.login_successful.connect(self.display_login_status)
        self.register_form.registration_finished.connect(self.display_registration_status)

        self.draggable_widget.setLayout(self.stacked_layout)

    def show_register_form(self):
        self.stacked_layout.setCurrentWidget(self.register_form)
        self.register_form.lineEdit_5.setFocus()

    def show_login_form(self):
        self.stacked_layout.setCurrentWidget(self.login_form)

    def handle_login(self):
        print("Entering handle_login()")
        email = self.login_form.lineEdit.text().lower()
        password = self.login_form.lineEdit_2.text()
        success = login(self, email, password)
        self.show_main_app_signal.emit(success)

    def handle_registration(self):
        email = self.register_form.lineEdit_5.text().lower()
        password = self.register_form.lineEdit_6.text()
        confirm_password = self.register_form.lineEdit_7.text()
        activation_code = self.register_form.lineEdit_8.text()

    def display_login_status(self, success):
        if success:
            self.login_form.label_6.setText("Login successful")
            self.login_form.label_6.setStyleSheet("color:green")
            self.show_main_app_signal.emit(success)
        else:
            self.login_form.label_6.setText("Invalid email/password")
            self.login_form.label_6.setStyleSheet("color:red")

    def display_registration_status(self, status):
        register_display_status(self.register_form, status)

def register_display_status(register_form, status):
    label = register_form.label_18

    if status == 0:
        label.setText("Email field cannot be blank")
        label.setStyleSheet("color:red")
    elif status == 1:
        label.setText("Password field(s) cannot be blank")
        label.setStyleSheet("color:red")
    elif status == 2:
        label.setText("Passwords do not match")
        label.setStyleSheet("color:red")
    elif status == 3:
        label.setText("Email already exists")
        label.setStyleSheet("color:red")
    elif status == 4:
        label.setText("Activation Code cannot be blank")
        label.setStyleSheet("color:red")
    elif status == 5:
        label.setText("Invalid code/Code has already been used")
        label.setStyleSheet("color:red")
    elif status == 6:
        label.setText("Successful Registration")
        label.setStyleSheet("color:green")
    elif status == 7:
        label.setText("Database error occurred. Please try again")
        label.setStyleSheet("color:red")