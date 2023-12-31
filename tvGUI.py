# Form implementation generated from reading ui file '.\tv.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_tvWindow(object):
    def setupUi(self, tvWindow):
        tvWindow.setObjectName("tvWindow")
        tvWindow.resize(540, 413)
        self.centralwidget = QtWidgets.QWidget(parent=tvWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tvFrame = QtWidgets.QLabel(parent=self.centralwidget)
        self.tvFrame.setGeometry(QtCore.QRect(0, -50, 541, 511))
        self.tvFrame.setMinimumSize(QtCore.QSize(541, 511))
        self.tvFrame.setMaximumSize(QtCore.QSize(541, 511))
        self.tvFrame.setText("")
        self.tvFrame.setPixmap(QtGui.QPixmap(".\\istockphoto-952473194-612x612.jpg"))
        self.tvFrame.setScaledContents(True)
        self.tvFrame.setObjectName("tvFrame")
        self.tvPicture = QtWidgets.QLabel(parent=self.centralwidget)
        self.tvPicture.setGeometry(QtCore.QRect(36, 32, 471, 301))
        self.tvPicture.setText("")
        self.tvPicture.setPixmap(QtGui.QPixmap(".\\premleague.jpg"))
        self.tvPicture.setScaledContents(True)
        self.tvPicture.setObjectName("tvPicture")
        self.volumeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.volumeLabel.setGeometry(QtCore.QRect(0, 360, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.volumeLabel.setFont(font)
        self.volumeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.volumeLabel.setObjectName("volumeLabel")
        self.channelLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.channelLabel.setGeometry(QtCore.QRect(420, 360, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.channelLabel.setFont(font)
        self.channelLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.channelLabel.setObjectName("channelLabel")
        self.tvFrame.raise_()
        self.volumeLabel.raise_()
        self.channelLabel.raise_()
        self.tvPicture.raise_()
        tvWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(tvWindow)
        QtCore.QMetaObject.connectSlotsByName(tvWindow)

    def retranslateUi(self, tvWindow):
        _translate = QtCore.QCoreApplication.translate
        tvWindow.setWindowTitle(_translate("tvWindow", "TV Window"))
        self.volumeLabel.setText(_translate("tvWindow", "Volume: 0"))
        self.channelLabel.setText(_translate("tvWindow", "Channel: 0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tvWindow = QtWidgets.QMainWindow()
    ui = Ui_tvWindow()
    ui.setupUi(tvWindow)
    tvWindow.show()
    sys.exit(app.exec())
