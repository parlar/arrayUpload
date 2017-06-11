import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QTableWidget, QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QComboBox, QDialog, QWidget, QListWidgetItem
from PyQt5.QtCore import QSettings

from gui.pref_ui import Ui_Form

class Preferences(QWidget, Ui_Form):
    def __init__(self, parent):
#    def __init__(self):
        super(Preferences, self).__init__()

        self.setupUi(self)
        self.setWindowTitle('Preferences')

        self.btn_ok.clicked.connect(lambda: self.ok(parent))
#        self.btn_ok.clicked.connect(self.ok)
        self.btn_cancel.clicked.connect(self.cancel)

        self.toolButton_manifest_file.clicked.connect(self.open_manifest_file_dialog)
        self.toolButton_array_data_folder.clicked.connect(self.open_array_data_folder_dialog)
        self.toolButton_sample_excel_files_folder.clicked.connect(self.open_sample_excel_files_folder_dialog)
        self.toolButton_sample_sheet_folder.clicked.connect(self.open_sample_sheet_folder_dialog)
        self.pushButton_add_investigator.clicked.connect(self.add_investigator)
        self.pushButton_remove_investigators.clicked.connect(self.remove_investigator)

        arrayUpload_settings = QSettings('vll', 'arrayUpload')

        institute = arrayUpload_settings.value('institute', type=str)
        path_manifest_file = arrayUpload_settings.value('path_manifest_file', type=str)
        path_array_data_folder = arrayUpload_settings.value('path_array_data_folder', type=str)
        path_sample_excel_files_folder = arrayUpload_settings.value('path_sample_excel_files_folder', type=str)
        path_sample_sheet_folder = arrayUpload_settings.value('path_sample_sheet_folder', type=str)
        investigators_list = arrayUpload_settings.value('investigators', type=list)

        self.lineEdit_institute.setText(institute)
        self.lineEdit_manifest_file.setText(path_manifest_file)
        self.lineEdit_array_data_folder.setText(path_array_data_folder)
        self.lineEdit_sample_excel_files_folder.setText(path_sample_excel_files_folder)
        self.lineEdit_sample_sheet_folder.setText(path_sample_sheet_folder)

        for i in investigators_list:
            item = QListWidgetItem(i)
            self.listWidget_investigators.addItem(item)


    def ok(self, parent):
#    def ok(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')

        institute = self.lineEdit_institute.text()
        path_manifest_file = self.lineEdit_manifest_file.text()
        path_array_data_folder = self.lineEdit_array_data_folder.text()
        path_sample_excel_files_folder = self.lineEdit_sample_excel_files_folder.text()
        path_sample_sheet_folder = self.lineEdit_sample_sheet_folder.text()

        arrayUpload_settings.setValue('institute', institute)
        arrayUpload_settings.setValue('path_manifest_file', path_manifest_file)
        arrayUpload_settings.setValue('path_array_data_folder', path_array_data_folder)
        arrayUpload_settings.setValue('path_sample_excel_files_folder', path_sample_excel_files_folder)
        arrayUpload_settings.setValue('path_sample_sheet_folder', path_sample_sheet_folder)
        parent.repopulate()

        self.close()

    def cancel(self):
        self.close()

    def open_manifest_file_dialog(self):
        path = QFileDialog.getOpenFileName(self, "Select Manifest File", "Manifest Files (*.bpm)")[0]
        self.lineEdit_manifest_file.setText(path)

    def open_array_data_folder_dialog(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_array_data_folder.setText(path)

    def open_sample_excel_files_folder_dialog(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_sample_excel_files_folder.setText(path)

    def open_sample_sheet_folder_dialog(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit_sample_sheet_folder.setText(path)

    def add_investigator(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        investigator = self.lineEdit_add_investigator.text()

        if investigator:
            investigators_list = arrayUpload_settings.value('investigators', type=list)
            investigators_list.append(investigator)
            investigators_list = list(set(investigators_list))
            arrayUpload_settings.setValue('investigators', investigators_list)

            self.listWidget_investigators.clear()
            investigators_list = arrayUpload_settings.value('investigators', type=list)
            for i in investigators_list:
                item = QListWidgetItem(i)
                self.listWidget_investigators.addItem(item)

            self.lineEdit_add_investigator.setText("")

    def remove_investigator(self):
        arrayUpload_settings = QSettings('vll', 'arrayUpload')
        investigator = ""
        try:
            investigator = self.listWidget_investigators.currentItem().text()

        except:
            pass

        if investigator:
            print(investigator)
            investigators_list = arrayUpload_settings.value('investigators', type=list)
            print(investigators_list)
            investigators_list.remove(investigator)
            print(investigators_list)
            investigators_list = list(set(investigators_list))
            arrayUpload_settings.setValue('investigators', investigators_list)
            self.listWidget_investigators.clear()
            investigators_list = arrayUpload_settings.value('investigators', type=list)
            for i in investigators_list:
                item = QListWidgetItem(i)
                self.listWidget_investigators.addItem(item)

# def mainp():
#     app = QApplication(sys.argv)
#     main_window = Preferences()
#     main_window.show()
#     sys.exit(app.exec_())
#
# if __name__ == "__main__":
#     mainp()

