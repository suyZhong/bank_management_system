from PyQt5.QtWidgets import QMainWindow
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget
from UI.main_window import Ui_MainWindow
from customer import CustomerUI
import db


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.engine = None
        self.ui.actionManage_Customers.triggered.connect(self.openCustomer)
        self.ui.actionManage_Accounts.triggered.connect(self.openAccount)
        self.ui.actionManage_Loans.triggered.connect(self.openLoans)
        self.customer = CustomerUI()
        self.ui.stackedWidget.addWidget(self.customer)

    def openCustomer(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def openAccount(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def openLoans(self):
        self.ui.stackedWidget.setCurrentIndex(2)


