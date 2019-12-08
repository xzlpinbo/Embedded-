import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi('./sample.ui', self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()