import sys
import os
from natsort import natsorted, ns
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QComboBox
#from PyQt5.QtCore import QSettings

class DataCombo(QtWidgets.QComboBox):
    def __init__(self, dpath):
        super().__init__()
        self.populate(dpath)

    def populate(self, dpath):
        print(dpath)

        dirs = os.listdir(path=dpath)
        sdirs = natsorted(dirs)

        sdirs.insert(0, " -- none selected -- ")

        for d in sdirs:
            if d[0] != '$':
                p = os.path.join(dpath, d)
                if os.path.isdir(p) or d == " -- none selected -- ":
                    self.addItem(d)