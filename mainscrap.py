from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os
from scrapy12 import *
from scarap12 import *
from scrapping2 import *
class birthday(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.dis)
        self.ui.pushButton_2.clicked.connect(self.exit)
    def dis(self):
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setupUi(self.MainWindow)
            self.MainWindow.show()
            self.ui.pushButton.clicked.connect(self.ui.scrap)
            self.ui.pushButton_2.clicked.connect(self.ui.ope1)
            self.ui.pushButton_3.clicked.connect(self.ui.exs)

    def exit(self):
            self.MainWindow = QtWidgets.QMainWindow()
            self.ui1 = Ui_MainWindow21()
            self.ui1.setupUi(self.MainWindow)
            self.MainWindow.show()
            self.ui1.pushButton.clicked.connect(self.ui1.scrap1)
            self.ui1.pushButton_2.clicked.connect(self.ui1.ope11)
            self.ui1.pushButton_3.clicked.connect(self.ui1.exs1)

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = birthday()
    w.show()
    sys.exit(app.exec_())
