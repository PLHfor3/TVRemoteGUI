from PyQt6.QtWidgets import *

from tvGUI import *


class TelevisionLogic(QMainWindow, Ui_tvWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setContentsMargins(0, 0, 0, 0)

    def mousePressEvent(self, event):
        """
        Method to help move frameless window when interacted with from the mouse
        """
        self.dragPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """
        Method to help move frameless window when interacted with from the mouse
        """
        self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
        self.dragPos = event.globalPosition().toPoint()
        event.accept()
