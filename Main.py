from RemoteLogic import *
from Television import *
from tvLogic import *


def main():
    television = Television()
    application = QApplication([])
    televisonWindow = TelevisionLogic()
    televisonWindow.show()
    remoteWindow = RemoteLogic(televisonWindow)
    remoteWindow.show()
    application.exec()


if __name__ == '__main__':
    main()
