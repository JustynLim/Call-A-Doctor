from PySide6 import QtCore, QtGui, QtWidgets
from LoginController import LoginController
from UI.Login_Resources import *; from UI.Register_Resources import *
from modules.sidebar import MySideBar
from modules.ui_doctor import Ui_MainWindow
import sys


logged_in_email = None


def open_main_app(success, login_controller):
    if success:
        # Fetch the logged-in email from the LoginController
        email = login_controller.login_form.lineEdit.text().lower()
        
        # Create and show the main app
        if not hasattr(login_controller, 'main_app'):
            main_app = MySideBar(doctor_email=email)
            login_controller.main_app = main_app  # Store reference to prevent re-creation
            main_app.show()
            main_app.activateWindow()

        # Close the login window
        login_controller.close()




if __name__ == '__main__':
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

    app = QtWidgets.QApplication(sys.argv)  # Ensure QApplication is created first
    print("QApplication initialised")
    screen = app.primaryScreen()

    login_controller = LoginController()
    login_controller.setupUI(screen)
    
    login_controller.show_main_app_signal.connect(lambda success : open_main_app (success, login_controller))
    login_controller.show()

    sys.exit(app.exec())