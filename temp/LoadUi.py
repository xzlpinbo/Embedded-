#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from time import strftime
import kma
import res
import os

class Dialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        uiPath = os.path.dirname(os.path.abspath(__file__))
        uiPath += "/DigitalClock.ui"
        self.ui = uic.loadUi(uiPath, self)
        self.setupUi()
        self.setupFunc()

    def setupUi(self):
        self.ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.timeUpdate()
        self.timeUpdate2()

    def setupFunc(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timeUpdate)
        self.timer.start(1000)

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.timeUpdate2)
        self.timer2.start(1000 * 3600)

    def timeUpdate(self):
        self.ui.lcdNumber_time.display(strftime("%I"+":"+"%M"+":"+"%S"))
        self.ui.label_date.setText(strftime("%Y년  %m월 %d일"))
        self.label_AMPM.setText(strftime("%p"))

    def timeUpdate2(self):
        wdata = kma.getWeather("1121571000")
        self.ui.label_local.setText(wdata[8])
        self.ui.label_icon.setPixmap(QtGui.QPixmap(":/newPrefix/weatherIcon/"+kma.wDict[wdata[0]]+".png"))
        self.ui.label_wdata.setText("현재 온도(℃ )- "+wdata[1]+"("+wdata[2]+"/"+wdata[3]+") "+ "\n" \
                                    "습도 - "+wdata[7]+"%"  \
                                    )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = Dialog()
    Form.show()
    sys.exit(app.exec_())
