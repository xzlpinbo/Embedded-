#!/usr/bin/python3

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import uic
from math import sqrt


class Form(QtWidgets.QWidget):
    def __init__(self, parrent=None):
        super(self.__class__, self).__init__(parrent)
        self = uic.loadUi("/root/untitled.ui", self)
        self.setupUi()
        self.setupFunc()

    def setupUi(self):
        self.setWindowTitle("example 1")
        self.setMouseTracking(False)
        self.target.setMouseTracking(False)
        self.target.setAutoFillBackground(True)

        self.px = 0
        self.py = 0
        self.rgb = ''

        self.propertyList= ("width", "height", "x", "y")
        msg = self.getProperty(self.propertyList)
        self.target.setText(msg)

        self.toggle.setCheckable(True)
        self.toggle.setStyleSheet("background-color:red")

    def setupFunc(self):
        self.toggle.toggled.connect(self.slot_btn_toggle)
        self.R.valueChanged.connect(self.slot_spinBox_changed)
        self.G.valueChanged.connect(self.slot_spinBox_changed)
        self.B.valueChanged.connect(self.slot_spinBox_changed)

    def slot_spinBox_changed(self):

        r = int(self.R.value())
        g = int(self.G.value())
        b = int(self.B.value())
        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(r,g,b))
        self.target.setPalette(pal)


    def slot_btn_toggle(self, flag):
        self.toggle.setStyleSheet("background-color:%s" % ({True : "green", False : "red"}[flag]))
        self.toggle.setText({True: "ON", False:"OFF"}[flag])

        self.setMouseTracking(flag)
        self.target.setMouseTracking(flag)

        self.R.setEnabled(not flag)
        self.G.setEnabled(not flag)
        self.B.setEnabled(not flag)

    def getProperty(self, list):
        msg = []
        for p in list:
            if not hasattr(self.target, p):
                continue
            value = getattr(self.target, p)()
            msg.append("{} : {}".format(p, str(value)))
        msg.append("{} : {}".format("mouse_x", str(self.px)))
        msg.append("{} : {}".format("mouse_y", str(self.py)))
        msg.append("{} : {}".format("rgb", self.rgb))
        msg = "\n".join(msg)
        return msg

    def mouseMoveEvent(self, QMouseEvent):
        self.px = QMouseEvent.x()
        self.py = QMouseEvent.y()
        self.setWidgetBackground(self.target, self.px, self.py)
        self.update()

    def setWidgetBackground(self, widget, x, y):
        if not isinstance(widget, QtWidgets.QWidget):
            return False
        lw = widget.width()
        lh = widget.height()

        if ((lw < x) or (lh < y)):
            return False

        v = int(sqrt(x**2 + y**2))
        r = int(sqrt(lw**2 + lh**2))
        r = int(v/r * 255)
        g = int(x/lw * 255)
        b = int(y/lh * 255)

        pal = QtGui.QPalette()
        pal.setColor(QtGui.QPalette.Background, QtGui.QColor(r,g,b))
        widget.setPalette(pal)
        self.rgb = "r{}, g{}, b{}".format(r,g,b)

    def paintEvent(self, QPaintEvent):
        msg = self.getProperty(self.propertyList)
        self.target.setText(msg)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())