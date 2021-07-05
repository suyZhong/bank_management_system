from UI.accountant import Ui_accountant
import db
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError
from PyQt5.Qt import QMessageBox
from sqlalchemy import or_

class AccountUI(QWidget, Ui_accountant):
    def __init__(self):
        super(AccountUI, self).__init__()
        self.engine = None
        self.setupUi(self)
        self.isChecking.clicked.connect(self.setBoxReadOnly)
        self.isSaving.clicked.connect(self.setBoxReadOnly)
        self.Confirm.clicked.connect(self.addAccount)

    def setBoxReadOnly(self):
        # print(self.isSaving.checkState())
        if self.isSaving.checkState():
            self.AccRate.setEnabled(True)
            self.currencyType.setEnabled(True)
            self.AccExtra.setEnabled(False)
        else:
            self.AccExtra.setEnabled(True)
            self.AccRate.setEnabled(False)
            self.currencyType.setEnabled(False)

    def addAccount(self):
        accType = self.isSaving.checkState()
        aid = self.AccID.text()
        rest = self.AccPoss.text()
        date = self.dateEdit.text()
        print(date)
        bank_name = self.AccBank.text()
        rate = self.AccRate.text()
        cType = self.currencyType.currentText()
        extra = self.AccExtra.text()
        try:
            db.addAccount(self.engine, accType, aid, rest, date, bank_name, rate, cType, extra)
        except IntegrityError:
            print(IntegrityError)
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong')
            msgBox.exec_()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, perhaps data too long or not fit '
                                                               'right format.')
            msgBox.exec_()
            return
        session = db.sessionmaker(self.engine)()
        if accType:
            data = session.query(db.SaveAccount).all()
        else:
            data = session.query(db.CheckAccount).all()
        # self.showCustomer(data)
        session.commit()
        session.close()

