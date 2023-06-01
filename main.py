# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication
#from PyQt5 import uic
import sys
import viewer as vwr
#import gvar
# https://www.youtube.com/watch?v=6zkOrq9YVik&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=30
# Thuesday 30


def main():
    app = QApplication(sys.argv)
    UIWindow = vwr.UI()
    UIWindow.setWindowTitle('Susel Image Viewer')
    UIWindow.setFixedSize(591, 581)
    app.exec_()

if __name__ == "__main__":
    main()