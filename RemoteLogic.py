from PyQt6.QtWidgets import *

from Television import Television
from remoteGUI import *


class RemoteLogic(QMainWindow, Ui_MainWindow, Television):

    def __init__(self, televisionWindow):
        super().__init__()
        self.setupUi(self)
        self.televisionWindow = televisionWindow
        # self.button_submit.clicked.connect(lambda: self.print_output())
        # self.button_10.clicked.connect(lambda: self.update_tip_percent("10"))
        # self.button_15.clicked.connect(lambda: self.update_tip_percent("15"))
        # self.button_20.clicked.connect(lambda: self.update_tip_percent("20"))
        # self.button_clear.clicked.connect(lambda: self.clear_all())
