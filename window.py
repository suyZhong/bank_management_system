from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget
from UI.main_window import Ui_MainWindow
from UI.customer import Ui_customer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.db = None
        self.ui.actionManage_Customers.triggered.connect(self.openCustomer)
        self.ui.actionManage_Accounts.triggered.connect(self.openAccount)

    def openCustomer(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def openAccount(self):
        self.ui.stackedWidget.setCurrentIndex(1)