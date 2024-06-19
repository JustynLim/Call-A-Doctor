from PySide6.QtWidgets import *
import sys
from function import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()