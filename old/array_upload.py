# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\array_upload.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

#import sys
#import os
#import csv

# import sys
# import os
# import csv
import xlrd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from dataComboBox import DataCombo


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_dropzone = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_dropzone.setMinimumSize(QtCore.QSize(602, 295))
        self.tableWidget_dropzone.setMaximumSize(QtCore.QSize(602, 295))
        self.tableWidget_dropzone.setObjectName("tableWidget_dropzone")
        self.tableWidget_dropzone.setColumnCount(3)
        self.tableWidget_dropzone.setRowCount(9)
        self.tableWidget_dropzone.setAcceptDrops(True)
        self.tableWidget_dropzone.setColumnWidth(0, 192)
        self.tableWidget_dropzone.setColumnWidth(1, 192)
        self.tableWidget_dropzone.setColumnWidth(2, 192)
        self.tableWidget_dropzone.setHorizontalHeaderLabels(['A1', 'A2', 'A3'])
        self.tableWidget_dropzone.setVerticalHeaderLabels(['', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8'])

        dpath = 'C:/'

        comboBox1 = DataCombo(dpath)
        comboBox2 = QtWidgets.QComboBox()
        comboBox3 = QtWidgets.QComboBox()

        self.tableWidget_dropzone.setCellWidget(0, 0, comboBox1)
        self.tableWidget_dropzone.setCellWidget(0, 1, comboBox2)
        self.tableWidget_dropzone.setCellWidget(0, 2, comboBox3)


        self.verticalLayout_2.addWidget(self.tableWidget_dropzone)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit_comment = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_comment.setMinimumSize(QtCore.QSize(602, 0))
        self.textEdit_comment.setMaximumSize(QtCore.QSize(602, 16777215))
        self.textEdit_comment.setObjectName("textEdit_comment")
        self.verticalLayout_2.addWidget(self.textEdit_comment)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(400, 0))
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.tableWidget_XLS = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_XLS.setObjectName("tableWidget_XLS")
        self.tableWidget_XLS.setColumnCount(30)
        self.tableWidget_XLS.setRowCount(100)

        self.check_change = False
        book = xlrd.open_workbook("C:/Users/parla/Documents/test.xls", 'r')
        sheet = book.sheet_by_index(0)
        self.tableWidget_XLS.setColumnCount(sheet.ncols + 10)

        for row_index in range(0, sheet.nrows):
#            print(row_index)
            #row = self.rowCount()
            #self.insertRow(row)
            for col_index in range(0, sheet.ncols):
#                print(col_index)
                content = sheet.cell(row_index, col_index).value
                item = QTableWidgetItem(content)
#                print(content)
                self.tableWidget_XLS.setItem(row_index, col_index, item)
                self.tableWidget_XLS.setDragEnabled(True)
                #self.setAcceptDrops(True)
        self.check_change = True


        self.verticalLayout_3.addWidget(self.tableWidget_XLS)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.tableWidget_dropzone.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        self.textEdit_comment.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuFile.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Array upload"))
        self.label_2.setText(_translate("MainWindow", "Comment:"))
        self.label.setText(_translate("MainWindow", "Samples excel sheet"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Variant Studio Manifest"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Bluefuse Multi  Manifest"))
        self.pushButton_4.setText(_translate("MainWindow", "Upload to Variant Studio"))
        self.pushButton.setText(_translate("MainWindow", "Upload to Variant Studio"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

