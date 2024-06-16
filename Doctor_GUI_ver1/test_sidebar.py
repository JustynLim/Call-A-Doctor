import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from modules.sidebar import MySideBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sidebar = MySideBar()
        self.setCentralWidget(self.sidebar)
        self.setWindowTitle("Doctor GUI")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
