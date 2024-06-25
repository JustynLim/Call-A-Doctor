from PyQt5 import QtCore, QtGui,QtWidgets
from UI.Login_UI import *; from UI.Register_UI import *
#from UI.Login_UI import Login_Form; from UI.Register_UI import Register_Form
from UI.Login_Resources import *; from UI.Register_Resources import *
from utilities import login, register, login_display_status, register_display_status
import sys


#  Global variables
#path_db_file    = "db/database.db"
form_type       = 1
logged_in_email = None

#  Allows window to be dragged around the screen
class DraggableWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._mousePressed = False
        self._mousePos = None
        self._startGeometry = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mousePressed = True
            self._mousePos = event.globalPos()
            self._startGeometry = self.geometry()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            delta = event.globalPos() - self._mousePos
            self.move(self._startGeometry.topLeft() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mousePressed = False


class MainController(DraggableWidget):
    login_finished = QtCore.pyqtSignal(bool) # Signal to indicate login finished
    registration_finished = QtCore.pyqtSignal(bool) # added this
    
    def __init__(self, screen):
        super().__init__()
            
        # Initialise UI widgets
        self.login_widget = Login_Form(self)
        self.register_widget = Register_Form(self)

        # Creates a central widget to hold all forms and a layout manager
        self.stacked_layout = QtWidgets.QStackedLayout(self)
        self.stacked_layout.addWidget(self.login_widget)
        self.stacked_layout.addWidget(self.register_widget)

        # Set the central widget of the main window
        self.setLayout(self.stacked_layout)

        # Connect buttons for page switching
        self.login_widget.pushButton.clicked.connect(lambda: login(self, self.login_widget.lineEdit.text(), self.login_widget.lineEdit_2.text()))
        self.login_widget.toolButton.clicked.connect(self.show_register_form)
        self.register_widget.toolButton_5.clicked.connect(self.show_login_form)
        # self.register_widget.pushButton_2.clicked.connect(lambda: register(self.register_widget, self.register_widget.lineEdit_5.text(), self.register_widget.lineEdit_6.text(), self.register_widget.lineEdit_7.text(), self.register_widget.lineEdit_8.text()))
        ###self.register_widget.pushButton_2.clicked.connect(lambda: register(self.register_widget.lineEdit_5.text(), self.register_widget.lineEdit_6.text(), self.register_widget.lineEdit_8.text()))

        self.login_finished.connect(self.display_login_status)
        self.registration_finished.connect(self.display_registration_status) # added this

        # Initialise program with login form
        self.show_login_form()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # screen = QtWidgets.QApplication.primaryScreen()
        dpi = screen.physicalDotsPerInch()
        scaling_factor = dpi / 96.0     # Standard DPI is 96
        self.resize(int(750 * scaling_factor), int(540 * scaling_factor))
        
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        


    def show_register_form(self):
        # QtCore.QTimer.singleShot(500, lambda: self.stacked_layout.setCurrentWidget(self.register_widget))
        self.stacked_layout.setCurrentWidget(self.register_widget)
        self.register_widget.lineEdit_5.setFocus()
        # self.register_widget.lineEdit_5.activateWindow()


    def show_login_form(self):
        # QtCore.QTimer.singleShot(500, lambda: self.stacked_layout.setCurrentWidget(self.login_widget))
        self.stacked_layout.setCurrentWidget(self.login_widget)

    def handle_login(self):
        email = self.login_widget.lineEdit.text().lower()
        password = self.login_widget.lineEdit_2.text()
        login_result = login(self, email, password)  # Update utilities.py accordingly
        self.login_finished.emit(login_result)  # Emit signal after login attempt

    def handle_register_XX(self):
        email = self.register_widget.lineEdit_5.text().lower()
        password = self.register_widget.lineEdit_6.text()
        confirm_password = self.register_widget.lineEdit_7.text()
        activation_code = self.register_widget.lineEdit_8.text()
        register_result = register(self, email, password, confirm_password, activation_code)
        self.registration_finished.emit(register_result)

    def display_login_status(self, success):
        if success:
            login_display_status(self, 1)
        else:
            login_display_status(self, 0)

    def display_registration_status(self, status):
        register_display_status(self, status)
        
if __name__ == '__main__':
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication(sys.argv)
    screen = app.primaryScreen()
    controller = MainController(screen)
    controller.register_widget.registration_finished.connect(controller.display_registration_status)

    controller.show()
    sys.exit(app.exec_())