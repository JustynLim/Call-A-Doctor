from PySide6 import QtCore, QtWidgets

class DraggableWidget(QtWidgets.QWidget):
    def __init__(self, parent = None, main_window = None):
        super().__init__(parent)
        self.main_window = main_window
        self._mousePressed = False
        self._mousePos = None
        self._startGeometry = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mousePressed = True
            self._mousePos = event.globalPos()
            self._startGeometry = self.main_window.geometry()

    def mouseMoveEvent(self, event):
        if self._mousePressed and self._startGeometry:  # Check if _startGeometry is not None
            delta = event.globalPos() - self._mousePos
            self.main_window.move(self._startGeometry.topLeft() + delta)


    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mousePressed = False