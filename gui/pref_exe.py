# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pref.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(422, 112)
        self.toolButton_1 = QtWidgets.QToolButton(Form)
        self.toolButton_1.setGeometry(QtCore.QRect(370, 30, 25, 19))
        self.toolButton_1.setObjectName("toolButton_1")
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setGeometry(QtCore.QRect(49, 30, 311, 20))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(240, 70, 75, 23))
        self.btn_ok.setObjectName("btn_ok")
        self.btn_cancel = QtWidgets.QPushButton(Form)
        self.btn_cancel.setGeometry(QtCore.QRect(320, 70, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        self.lbl_1 = QtWidgets.QLabel(Form)
        self.lbl_1.setGeometry(QtCore.QRect(11, 30, 32, 16))
        self.lbl_1.setObjectName("lbl_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton_1.setText(_translate("Form", "..."))
        self.btn_ok.setText(_translate("Form", "OK"))
        self.btn_cancel.setText(_translate("Form", "Cancel"))
        self.lbl_1.setText(_translate("Form", "Input1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

