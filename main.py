import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from modules.ui_doctor import Ui_MainWindow 
from modules.sidebar import MySideBar
from modules import *

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySideBar()
    window.show()
    sys.exit(app.exec())