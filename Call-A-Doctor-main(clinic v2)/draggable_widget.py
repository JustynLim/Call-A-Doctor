from PySide6 import QtCore, QtWidgets

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
            self._startSiGeometry = self.geometry()

    def mouseMoveEvent(self, event):
        if self._mousePressed:
            delta = event.globalPos() - self._mousePos
            self.move(self._startGeometry.topLeft() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self._mousePressed = False