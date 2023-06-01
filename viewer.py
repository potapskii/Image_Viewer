# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import os
import sys
import gvar
# https://www.youtube.com/watch?v=6zkOrq9YVik&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=30
# Thuesday 30


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        # load the ui file
        uic.loadUi("viewer.ui", self)
        # define our widgets
        self.open_btn = self.findChild(QPushButton, "btn1")
        self.lbl    = self.findChild(QLabel, "label")
        # Click The Dropdown Box
        self.open_btn.clicked.connect(self.clicker)
        self.show()
     # button handdler
    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "c:\\User\\PC\\Pictures\\screnn", "All Files (*);;PNG Files (*.png)")
        # open the image
        self.pixmap = QPixmap(fname[0])
        self.lbl.setPixmap(self.pixmap)