from PySide6 import QtCore, QtGui, QtWidgets
from LoginController import LoginController
#from modules.sidebar import MySideBar
#from PySide6.QtWidgets import QApplication
#from PyQt5.QtWidgets import QApplication
# from PyQt5 import QtCore, QtGui,QtWidgets
#from UI.Doctor_Login_UI import *; from UI.Doctor_Register_UI import *



#from UI.Login_UI import Login_Form; from UI.Register_UI import Register_Form
#from UI.Login_Resources import *; from UI.Register_Resources import *
#from doctor_utilities import login, register, login_display_status, register_display_status
from modules.sidebar import MySideBar
from modules.ui_doctor import Ui_MainWindow
#from draggable_widget import DraggableWidget
import sys#, webbrowser


#  Global variables
#path_db_file    = "db/database.db"
#form_type       = 1
logged_in_email = None

        
# if __name__ == '__main__':
#     import ctypes
#     ctypes.windll.shcore.SetProcessDpiAwareness(2)
#     QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

#     app = QtWidgets.QApplication(sys.argv)
#     screen = app.primaryScreen()
#     controller = MainController(screen)
#     controller.register_widget.registration_finished.connect(controller.display_registration_status)

#     controller.show()
#     sys.exit(app.exec_())



def open_main_app(success, login_controller):
    if success:
        # Fetch the logged-in email from the LoginController
        email = login_controller.login_form.lineEdit.text().lower()

        # Check if main_app already exists and is visible
        if hasattr(login_controller, 'main_app') and login_controller.main_app.isVisible():
            # If main_app exists and is visible, activate it and return
            login_controller.main_app.activateWindow()
            return

        # Create and show the main app (MySideBar)
        main_app = MySideBar(doctor_email=email)
        main_app.show()
        main_app.activateWindow()

        # Close the login window
        login_controller.close()

        # Store main_app in login_controller for future reference
        login_controller.main_app = main_app

    else:
        # Handle login failure if needed
        pass





if __name__ == '__main__':
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # app = QApplication(sys.argv)
    app = QtWidgets.QApplication(sys.argv)  # Ensure QApplication is created first
    print("QApplication initialised")
    screen = app.primaryScreen()

    # login_controller = LoginController(screen)
    login_controller = LoginController()
    login_controller.setupUI(screen)
    
    login_controller.show_main_app_signal.connect(lambda success : open_main_app (success, login_controller))
    login_controller.show()
    #controller.register_widget.registration_finished.connect(controller.display_registration_status)

    login_controller.login_form.login_successful.connect(open_main_app)
    # Connect the login_finished signal to show the main app
    
    
    #login_controller.login_finished.connect(lambda success: open_main_app(success, login_controller))
    
    #controller.show()

    # # Start the QApplication event loop explicitly
    # result = app.exec_()  

    # # Check if main app was created successfully
    # if hasattr(controller, 'main_app') and controller.main_app.isVisible():
    #     # If the main app is running, execute its event loop
    #     sys.exit(controller.main_app.exec_()) 
    # else:
    #     # If the main app failed to start, exit with the original result code
    #     sys.exit(result) 

    sys.exit(app.exec_())

