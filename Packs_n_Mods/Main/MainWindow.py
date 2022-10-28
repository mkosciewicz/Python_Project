from PyQt5 import QtWidgets
# from PyQt5 import uic
from Toolbox.Qt_Designer.ui_codes.MainWindow_code import Ui_MainWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # uic.loadUi("untitled.ui", self)
        # self.show()
        # self.ui.tab_2.connect(self.mapa_tab)
        self.ui.actionClose.triggered.connect(exit)


def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
