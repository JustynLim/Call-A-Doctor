from PySide6 import QtCore, QtGui, QtWidgets
from doctor_utilities import login, register#, login_display_status, register_display_status
from UI.Doctor_Login_UI import Login_Form; from UI.Doctor_Register_UI import Register_Form
#import webbrowser
from draggable_widget import DraggableWidget

class LoginController(QtWidgets.QMainWindow):

    registration_finished = QtCore.Signal(int)
    show_main_app_signal = QtCore.Signal(bool)

    def __init__(self):
        super().__init__()
        self._mousePressed = False
        self._mousePos = None
        self._startGeometry = None
        
        self.login_finished = QtCore.Signal(bool)
        self.registration_finished = QtCore.Signal(int)


    def setupUI(self, screen):
        print("setupUI Login Controller")
        print(self.layout())
        
        # 1) Create layout
        self.stacked_layout = QtWidgets.QStackedLayout(self)

        # 2) Set layout for draggable widget
        self.draggable_widget = DraggableWidget(self, main_window=self)
        self.draggable_widget.setLayout(self.stacked_layout)

        # 3) Create forms after setting up layout and pass self.draggable_widget as parent
        self.login_form = Login_Form(self.draggable_widget)
        self.register_form = Register_Form(self.draggable_widget)

        # 4) Add forms to stacked layout
        self.stacked_layout.addWidget(self.login_form)
        self.stacked_layout.addWidget(self.register_form)

        # 5) Set central widget of main window to draggable widget
        self.setCentralWidget(self.draggable_widget)


        # self.setLayout(self.stacked_layout)   # Almost there!
        print("Creating widgets in LoginController")

                    
        dpi = screen.physicalDotsPerInch()
        scaling_factor = dpi / 96.0     # Standard DPI is 96
        self.resize(int(700 * scaling_factor), int(500 * scaling_factor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        print("Widgets created")

        # Initialise program with login form
        self.show_login_form()


        # Connect buttons for page switching
        self.login_form.pushButton.clicked.connect(self.handle_login)
        self.login_form.login_successful.connect(self.login_finished)
        self.register_form.toolButton_5.clicked.connect(self.show_login_form)
        self.register_form.pushButton_2.clicked.connect(self.handle_registration)
        self.login_form.toolButton.clicked.connect(self.show_register_form)

        # Connect signals for status display and main app launch
        self.login_form.login_successful.connect(self.display_login_status)
        self.register_form.registration_finished.connect(self.display_register_status)
        

        # Initialize the layout of self.draggable_widget
        self.draggable_widget.setLayout(self.stacked_layout)
             

    def show_register_form(self):
        self.stacked_layout.setCurrentWidget(self.register_form)
        self.register_form.lineEdit_5.setFocus()  # Set focus directly



    def show_login_form(self):
        # QtCore.QTimer.singleShot(500, lambda: self.stacked_layout.setCurrentWidget(self.login_widget))
        self.stacked_layout.setCurrentWidget(self.login_form)

    def handle_login(self):
        print("Entering handle_login()")
        email = self.login_form.lineEdit.text().lower()
        password = self.login_form.lineEdit_2.text()
        success = login(self, email, password)  # Update utilities.py accordingly
        self.show_main_app_signal.emit(success)
        #self.login_finished.emit(success)

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

    
    def display_register_status(self, status):

        if status == 0:
            self.register_form.label_18.setText("Email field cannot be blank")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 1:
            self.register_form.label_18.setText("Password field(s) cannot be blank")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 2:
            self.register_form.label_18.setText("Passwords do not match")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 3:
            self.register_form.label_18.setText("Email does not exist")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 4:
            self.register_form.label_18.setText("Activation Code cannot be blank")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 5:
            self.register_form.label_18.setText("Invalid code/Code has already been used")
            self.register_form.label_18.setStyleSheet("color:red")
        
        elif status == 6:   
            self.register_form.label_18.setText("Successful Registration")
            self.register_form.label_18.setStyleSheet("color:green")
        
        elif status == 7:
            self.register_form.label_18.setText("Database error occurred. Please try again")
            self.register_form.label_18.setStyleSheet("color:red")        