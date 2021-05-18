from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys
import os
from centerit import *

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    centerqt(win, 500, 400)
    win.setWindowTitle("Hello")

    lbl = QtWidgets.QLabel(win)
    lbl.setText("Hello There!!")

    win.show()
    sys.exit(app.exec())

window()
