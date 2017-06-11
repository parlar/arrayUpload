#! python

import sys
import xlrd
import os
from natsort import natsorted

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QComboBox,QDialog
from PyQt5.QtCore import QSettings

from dataComboBox import DataCombo
from preferences import Preferences
from gui.mainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.tableWidget_dropzone.setColumnCount(3)
        self.tableWidget_dropzone.setRowCount(9)
        self.tableWidget_dropzone.setAcceptDrops(True)
        self.tableWidget_dropzone.setColumnWidth(0, 192)
        self.tableWidget_dropzone.setColumnWidth(1, 192)
        self.tableWidget_dropzone.setColumnWidth(2, 192)
        self.tableWidget_dropzone.setHorizontalHeaderLabels(['A1', 'A2', 'A3'])
        self.tableWidget_dropzone.setVerticalHeaderLabels(['', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'])


        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        path1 = arrayUpload_settings.value('path1', type=str)

        self.label_d1_data.setText(path1)

        dpath = 'C:/'

        comboBox1 = DataCombo(dpath)
        comboBox2 = QComboBox()
        comboBox3 = QComboBox()

        self.tableWidget_dropzone.setCellWidget(0, 0, comboBox1)
        self.tableWidget_dropzone.setCellWidget(0, 1, comboBox2)
        self.tableWidget_dropzone.setCellWidget(0, 2, comboBox3)

        self.loadExcel()
        self.load_samples()

        self.actionPreferences.triggered.connect(self.show_preferences)




    def loadExcel(self):

        book = xlrd.open_workbook("C:/Users/parla/Documents/test.xls", 'r')
        sheet = book.sheet_by_index(0)

        self.tableWidget_XLS.setColumnCount(sheet.ncols + 10)
        self.tableWidget_XLS.setRowCount(sheet.nrows + 10)

        self.check_change = False

        for row_index in range(0, sheet.nrows):

            for col_index in range(0, sheet.ncols):

                content = sheet.cell(row_index, col_index).value
                item = QTableWidgetItem(content)
                self.tableWidget_XLS.setItem(row_index, col_index, item)
                self.tableWidget_XLS.setDragEnabled(True)

        self.check_change = True

    def load_samples(self):

        files = os.listdir("C:/Users/parla/Documents/")
        sfiles = natsorted(files)
        sfiles.insert(0, " -- none selected -- ")

        for f in sfiles:
            # print(f)
            if f.endswith('.xls') or f.endswith(' -- none selected -- '):
                self.load_samples_comboBox.addItem(f)

    def show_preferences(self):
        self.p = Preferences(self)
        self.p.show()

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

