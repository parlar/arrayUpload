import sys
import os
from natsort import natsorted, ns
import xlrd

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QComboBox
#from PyQt5.QtCore import QSettings

class ExcelCombo(QtWidgets.QComboBox):
    def __init__(self, path):
        super().__init__()
        self.populate(path)

    def populate(self, path):
        print(path)

        files = os.listdir(path=path)
        files_xls = []
        for f in files:
            if f.endswith(".xls"):
                files_xls.append(f)

        sfiles_xls = natsorted(files_xls)

        sfiles.insert(0, " -- none selected -- ")

        for f in sfiles_xls:
            if f[0] != '$':
                self.addItem(f)

