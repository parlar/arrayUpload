import sys
import os
import csv
import xlrd

from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import qApp, QAction, QDialog
from pref import PrefsDialog
from PyQt5.QtCore import QSettings

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.check_change = True
        self.init_ui()

    def init_ui(self):
        self.cellChanged.connect(self.c_current)
        self.show()

    def c_current(self):
        if self.check_change:
            row = self.currentRow()
            col = self.currentColumn()
            value = self.item(row, col)
            value = value.text()
            print("The current cell is ", row, ", ", col)
            print("In this cell we have: ", value)

    def open_sheet(self):
        self.check_change = False

        path = QFileDialog.getOpenFileName(self, 'Open XLS', "C:/Users/parlar/Documents", 'XLS(*.xls)')
        if path[0] != '':
            print(path[0])
            book = xlrd.open_workbook(path[0], 'r')
            sheet = book.sheet_by_index(0)

            self.setColumnCount(sheet.ncols)

            for row_index in range(0, sheet.nrows):
                 print(row_index)
                 row = self.rowCount()
                 self.insertRow(row)
                 for col_index in range(0, sheet.ncols):
                     print(col_index)
                     content = sheet.cell(row_index,col_index).value
                     item = QTableWidgetItem(content)
                     print(content)
                     self.setItem(row_index, col_index, item)
                     self.setDragEnabled(True)
                     self.setAcceptDrops(True)
        self.check_change = True

    def save_sheet(self):
        path = QFileDialog.getSaveFileName(self, 'Save CSV', os.getenv('HOME'), 'CSV(*.csv)')
        if path[0] != '':
            with open(path[0], 'w') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                for row in range(self.rowCount()):
                    row_data = []
                    for column in range(self.columnCount()):
                        item = self.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append('')
                    writer.writerow(row_data)
    def open_pref(self):
        dialog = QDialog()
        dialog.ui = PrefsDialog()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

class Sheet(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = MyTable(10, 10)
        self.setCentralWidget(self.form_widget)
        col_headers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.form_widget.setHorizontalHeaderLabels(col_headers)

        # Set up menu
        bar = self.menuBar()
        file = bar.addMenu('File')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)

        pref_action = QAction('&Pref', self)
        pref_action.setShortcut('Ctrl+P')

        quit_action = QAction('&Quit', self)

        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(pref_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_app)
        save_action.triggered.connect(self.form_widget.save_sheet)
        pref_action.triggered.connect(self.form_widget.open_pref)
        open_action.triggered.connect(self.form_widget.open_sheet)

        prefhook = QSettings('vll', 'spread')
#        prefhook.setValue('dict_value', {'datapath': "C:/Users/parla"})
        dict_value = prefhook.value('dict_value', type=str)

        print("dict_value: %s" % repr(dict_value))
        self.show()

    def quit_app(self):
        qApp.quit()




app = QApplication(sys.argv)
sheet = Sheet()

sys.exit(app.exec_())