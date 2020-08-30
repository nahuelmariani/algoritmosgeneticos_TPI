from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import parque_eolico_ui

class MainApp(QtWidgets.QMainWindow, parque_eolico_ui.Ui_mainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.dialogs = list()

def main():
    app = QtWidgets.QApplication(sys.argv)
    principal = MainApp()
    principal.show()
    #app.exec_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
