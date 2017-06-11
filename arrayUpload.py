#! python

import sys
import xlrd
import os
from natsort import natsorted

from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QComboBox,QDialog

from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import QSettings

from dataComboBox import DataCombo
#from excelComboBox import ExcelCombo

from preferences import Preferences
from gui.mainWindow_ui import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.tableWidget_dropzone.setColumnCount(6)
        self.tableWidget_dropzone.setRowCount(9)
        self.tableWidget_dropzone.setAcceptDrops(True)
        self.tableWidget_dropzone.setColumnWidth(0, 128)
        self.tableWidget_dropzone.setColumnWidth(1, 64)
        self.tableWidget_dropzone.setColumnWidth(2, 128)
        self.tableWidget_dropzone.setColumnWidth(3, 64)
        self.tableWidget_dropzone.setColumnWidth(4, 128)
        self.tableWidget_dropzone.setColumnWidth(5, 64)
        self.tableWidget_dropzone.setHorizontalHeaderLabels(['A1 Sample IDs', 'Gender', 'A2 Sample IDs', 'Gender',
                                                             'A3 Sample IDs', 'Gender'])
        self.tableWidget_dropzone.setVerticalHeaderLabels(['', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'])
        self.tableWidget_dropzone.setSpan(0, 0, 1, 2)
        self.tableWidget_dropzone.setSpan(0, 2, 1, 2)
        self.tableWidget_dropzone.setSpan(0, 4, 1, 2)

        # populate stuff
        # arrayUpload_settings = QSettings('vll', 'arrayUpload')
        # path_array_data_folder = arrayUpload_settings.value('path_array_data_folder', type=str)
        # dataComboBox1 = DataCombo(path_array_data_folder)
        # dataComboBox2 = DataCombo(path_array_data_folder)
        # dataComboBox3 = DataCombo(path_array_data_folder)
        #
        # self.tableWidget_dropzone.setCellWidget(0, 0, dataComboBox1)
        # self.tableWidget_dropzone.setCellWidget(0, 2, dataComboBox2)
        # self.tableWidget_dropzone.setCellWidget(0, 4, dataComboBox3)

        self.populateExcelComboBox()
        self.populateDataComboBoxes()
        self.populateInvestigators()

        # other settings

        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        # actions

        self.actionPreferences.triggered.connect(self.show_preferences)
        self.load_samples_comboBox.activated.connect(self.loadExcel)

    def repopulate(self):
        self.populateExcelComboBox()
        self.populateDataComboBoxes()
        self.populateInvestigators()

    def populateInvestigators(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        investigators_list = arrayUpload_settings.value('investigators', type=list)

        investigators_list.insert(0, " -- none selected -- ")

        self.comboBox_investigator.clear()
        for i in investigators_list:
            self.comboBox_investigator.addItem(i)

    def populateDataComboBoxes(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        path_array_data_folder = arrayUpload_settings.value('path_array_data_folder', type=str)
        dataComboBox1 = DataCombo(path_array_data_folder)
        dataComboBox2 = DataCombo(path_array_data_folder)
        dataComboBox3 = DataCombo(path_array_data_folder)

        self.tableWidget_dropzone.setCellWidget(0, 0, dataComboBox1)
        self.tableWidget_dropzone.setCellWidget(0, 2, dataComboBox2)
        self.tableWidget_dropzone.setCellWidget(0, 4, dataComboBox3)

    def populateExcelComboBox(self):
        self.load_samples_comboBox.clear()
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        path_sample_excel_files_folder = arrayUpload_settings.value('path_sample_excel_files_folder', type=str)
        files = os.listdir(path=path_sample_excel_files_folder)
        files_xls = []
        for f in files:
            if f.endswith(".xls"):
                files_xls.append(f)

        sfiles_xls = natsorted(files_xls)

        sfiles_xls.insert(0, " -- none selected -- ")

        for f in sfiles_xls:
            if f[0] != '$':
                self.load_samples_comboBox.addItem(f)


    def loadExcel(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        path_sample_excel_files_folder = arrayUpload_settings.value('path_sample_excel_files_folder', type=str)

        self.tableWidget_XLS.clear()

        cexcel = self.load_samples_comboBox.currentText()
        cexcel_path = path_sample_excel_files_folder + "/" + cexcel

        if cexcel != " -- none selected -- ":

            book = xlrd.open_workbook(cexcel_path, 'r')
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

