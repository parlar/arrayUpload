from pywinauto.application import Application
app = Application().start("C:/Program Files (x86)/BlueGnome/BlueFuse Multi/bluemarker.exe")
dlg = app.top_window()
dlg.OK.click()
app.LoginDialog.edit.type_keys('larsson4')
app.LoginDialog.OK.click()

#app.UntitledNotepad.menu_select("Hjälp->Om anteckningar")
#app.AboutNotepad.OK.click()
#app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)