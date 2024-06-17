from PySide6.QtWidgets import *
import sys
from clinic import MySideBar

app = QApplication(sys.argv)

window = MySideBar()

window.show()
app.exec()