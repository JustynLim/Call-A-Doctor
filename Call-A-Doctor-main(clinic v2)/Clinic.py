from PySide6 import QtCore, QtGui, QtWidgets
from LoginController import LoginController
from Modules.function import MySideBar
import sys

logged_in_email = None

def open_main_app(success, login_controller):
    if success:
        email = login_controller.login_form.lineEdit.text().lower()
        main_app = MySideBar(doctor_email=email)
        main_app.ui.setupUi(main_app)
        main_app.doctor_email = email
        main_app.show()
        main_app.activateWindow()
        login_controller.close()

if __name__ == '__main__':
    import ctypes
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    # Remove the deprecated attribute setting:
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QtWidgets.QApplication(sys.argv)
    print("QApplication initialised")
    screen = app.primaryScreen()

    login_controller = LoginController()
    login_controller.setupUI(screen)
    
    login_controller.show_main_app_signal.connect(lambda success: open_main_app(success, login_controller))
    login_controller.show()
    login_controller.login_form.login_successful.connect(open_main_app)
    
    sys.exit(app.exec_())
