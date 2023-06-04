# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
#from PyQt5 import uic
import sys
import viewer as vwr
import gvar


def main():
    app = QApplication(sys.argv)
    UIWindow = vwr.UI()
    UIWindow.setWindowTitle('Susel Image Viewer')
    UIWindow.setFixedSize(gvar.width, gvar.height)
    app.exec_()

if __name__ == "__main__":
    main()