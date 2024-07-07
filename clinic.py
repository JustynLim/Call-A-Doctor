from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QTimer
from ClinicLoginController import LoginController
from UI.Login_Resources import *; from UI.Register_Resources import *
from Clinicmodules.clinic_main_app import MySideBar        
from Clinicmodules.clinicUI import Ui_MainWindow    
import sys



logged_in_email = None

def open_main_app(success, login_controller):
    if success:
        # Fetch the logged-in email from the LoginController
        email = login_controller.login_form.lineEdit.text().lower()

        def create_main_app():    
            # Create and show the main app
            if not hasattr(login_controller, 'main_app'):
                main_app = MySideBar(clinic_email=email)  # Create the main app
                main_app.show()
                main_app.activateWindow()
            else:
                login_controller.main_app.show()
                login_controller.main_app.activateWindow()

            # Close the login window
            login_controller.close()

        # Set a single-shot timer to delay the showing of the main app
        QTimer.singleShot(500, create_main_app)



        
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