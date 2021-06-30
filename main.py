from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from login import LoginDiag
from window import MainWindow

from UI.login_form import Ui_login_form
import sys
import db



def main():
    app = QApplication(sys.argv)
    # window = MainWindow()
    # window2 = MainWindow()
    dialog = LoginDiag()
    # ui = Ui_login_form()
    # ui.setupUi(dialog)
    # ui.pushButton.clicked.connect(window_login)
    dialog.show()
    # window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()