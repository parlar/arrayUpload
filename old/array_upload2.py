# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\array_upload2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1232, 858)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget_dropzone = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_dropzone.setMinimumSize(QtCore.QSize(602, 300))
        self.tableWidget_dropzone.setMaximumSize(QtCore.QSize(602, 522))
        self.tableWidget_dropzone.setObjectName("tableWidget_dropzone")
        self.tableWidget_dropzone.setColumnCount(0)
        self.tableWidget_dropzone.setRowCount(0)
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
        self.tableWidget_XLS.setColumnCount(0)
        self.tableWidget_XLS.setRowCount(0)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1232, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

