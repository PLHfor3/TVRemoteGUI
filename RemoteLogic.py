from remoteGUI import *
from tvLogic import *


class RemoteLogic(QMainWindow, Ui_remoteWindow):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self, televisionWindow: TelevisionLogic):
        """
        Method to set default values of RemoteLogic Object
        """
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = RemoteLogic.MIN_VOLUME
        self.__channel = RemoteLogic.MIN_CHANNEL
        self.televisionWindow = televisionWindow
        self.volumeUp.clicked.connect(lambda: self.volume_up())
        self.volumeDown.clicked.connect(lambda: self.volume_down())
        self.channelUp.clicked.connect(lambda: self.channel_up())
        self.channelDown.clicked.connect(lambda: self.channel_down())
        self.powerButton.clicked.connect(lambda: self.power())
        self.Mute.clicked.connect(lambda: self.mute())
        self.updatePicture(self.__channel)
        self.televisionWindow.tvPicture.setHidden(True)

    def updateDisplay(self):
        """
        Method to update the volume and channel labels
        """
        self.televisionWindow.volumeLabel.setText(f"Volume: {self.__volume}")
        self.televisionWindow.channelLabel.setText(f"Channel: {self.__channel}")

    def updatePicture(self, channel: int):
        """
        Method to update the current channel picture being displayed on the tv
        :param channel: the current channel
        """
        match channel:
            case 0:
                self.televisionWindow.tvPicture.setPixmap(QtGui.QPixmap("cbscbb.png"))
            case 1:
                self.televisionWindow.tvPicture.setPixmap(QtGui.QPixmap("foxcbb.jpg"))
            case 2:
                self.televisionWindow.tvPicture.setPixmap(QtGui.QPixmap("espnfb.jpg"))
            case 3:
                self.televisionWindow.tvPicture.setPixmap(QtGui.QPixmap("premleague.jpg"))

    def power(self) -> None:
        """
        method to toggle whether the tv is on or off
        """
        if self.__status:
            self.__status = False
            self.televisionWindow.tvPicture.setHidden(True)
        else:
            self.__status = True
            self.televisionWindow.tvPicture.setHidden(False)

    def mute(self) -> None:
        """
        method to toggle the mute status of the TV between muted or not muted
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.updateDisplay()
            else:
                self.__muted = True
                self.televisionWindow.volumeLabel.setText("Muted")

    def channel_up(self) -> None:
        """
        method to increase channel number
        """
        if self.__status:
            if self.__channel == RemoteLogic.MAX_CHANNEL:
                self.__channel = RemoteLogic.MIN_CHANNEL
                self.updateDisplay()
            else:
                self.__channel += 1
                self.updateDisplay()
            self.updatePicture(self.__channel)

    def channel_down(self) -> None:
        """
        method to decrease Channel number
        """
        if self.__status:
            if self.__channel == RemoteLogic.MIN_CHANNEL:
                self.__channel = RemoteLogic.MAX_CHANNEL
                self.updateDisplay()
            else:
                self.__channel -= 1
                self.updateDisplay()
            self.updatePicture(self.__channel)

    def volume_up(self) -> None:
        """
        method to increase TV volume
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume == RemoteLogic.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
                self.updateDisplay()

    def volume_down(self) -> None:
        """
        method to decrease TV volume
        """
        if self.__muted:
            self.__muted = False
        if self.__status:
            if self.__volume == RemoteLogic.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
                self.updateDisplay()

    def closeEvent(self, *args, **kwargs):
        """
        Method to close all windows when the remote window is closed
        """
        super(QtGui.QMainWindow, self).closeEvent(*args, **kwargs)
        self.televisionWindow.close()
