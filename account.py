from UI.account import Ui_account
import db
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError
from PyQt5.Qt import QMessageBox
from sqlalchemy import or_
import datetime


class AccountUI(QWidget, Ui_account):
    def __init__(self):
        super(AccountUI, self).__init__()
        self.args = {}
        self.engine = None
        self.setupUi(self)
        self.setBoxReadOnly()
        self.savingState = self.isSaving.checkState()
        self.isChecking.clicked.connect(self.setBoxReadOnly)
        self.isSaving.clicked.connect(self.setBoxReadOnly)
        self.isSaving_2.clicked.connect(self.setBoxReadOnly)
        self.isChecking_2.clicked.connect(self.setBoxReadOnly)
        self.isSaving_3.clicked.connect(self.setBoxReadOnly)
        self.isChecking_3.clicked.connect(self.setBoxReadOnly)
        self.isSaving_4.clicked.connect(self.setBoxReadOnly)
        self.isChecking_4.clicked.connect(self.setBoxReadOnly)
        self.AccID_2.textChanged.connect(self.queryAccount)
        self.AccID_3.textChanged.connect(self.queryAccount)
        self.AccID_4.textChanged.connect(self.queryAccount)
        self.Confirm.clicked.connect(self.addAccount)
        self.Confirm_2.clicked.connect(self.delAccount)
        self.Confirm_3.clicked.connect(self.updateAccount)
        self.Confirm_4.clicked.connect(self.queryAccount)
        self.toolButton.clicked.connect(self.showAllTable)
        self.pushButton.clicked.connect(self.queryAccount)
        self.tableWidget.clicked.connect(self.setTextFromTable)
        self.tabWidget.currentChanged.connect(self.setBoxReadOnly)

    def setBoxReadOnly(self):
        # print(self.isSaving.checkState())
        if self.tabWidget.currentIndex() == 0:
            self.savingState = self.isSaving.checkState()
            if self.savingState:
                self.AccRate.setEnabled(True)
                self.currencyType.setEnabled(True)
                self.AccExtra.setEnabled(False)
            else:
                self.AccExtra.setEnabled(True)
                self.AccRate.setEnabled(False)
                self.currencyType.setEnabled(False)
        elif self.tabWidget.currentIndex() == 1:
            self.savingState = self.isSaving_2.checkState()
            if self.isSaving_2.checkState():
                self.AccRate_2.setEnabled(True)
                self.currencyType_2.setEnabled(True)
                self.AccExtra_2.setEnabled(False)
            else:
                self.AccExtra_2.setEnabled(True)
                self.AccRate_2.setEnabled(False)
                self.currencyType_2.setEnabled(False)
        elif self.tabWidget.currentIndex() == 2:
            self.savingState = self.isSaving_3.checkState()
            if self.isSaving_3.checkState():
                self.AccRate_3.setEnabled(True)
                self.currencyType_3.setEnabled(True)
                self.AccExtra_3.setEnabled(False)
            else:
                self.AccExtra_3.setEnabled(True)
                self.AccRate_3.setEnabled(False)
                self.currencyType_3.setEnabled(False)
        else:
            self.savingState = self.isSaving_4.checkState()
            if self.isSaving_4.checkState():
                self.AccRate_4.setEnabled(True)
                self.currencyType_4.setEnabled(True)
                self.AccExtra_4.setEnabled(False)
            else:
                self.AccExtra_4.setEnabled(True)
                self.AccRate_4.setEnabled(False)
                self.currencyType_4.setEnabled(False)

    def getTableText(self, row, col):
        try:
            result = self.tableWidget.item(row, col).text()
        except AttributeError:
            result = ''
        if result == 'None':
            result = ''
        return result

    def setTextFromTable(self):
        if self.tabWidget.currentIndex() == 0:
            return
        row = self.tableWidget.currentRow()
        id = self.getTableText(row, 0)
        rest = self.getTableText(row, 1)
        date = self.getTableText(row, 2)
        bank = self.getTableText(row, 3)
        rate = self.getTableText(row, 4)
        extra = self.getTableText(row, 4)
        money_type = self.getTableText(row, 5)
        if self.tabWidget.currentIndex() == 1:
            self.AccID_2.setText(id)
            self.dateEdit_2.setDate(datetime.datetime.strptime(date,"%Y-%m-%d"))
            self.AccPoss_2.setText(rest)
            self.AccBank_2.setCurrentText(bank)
            if self.savingState:
                self.AccRate_2.setText(rate)
                self.currencyType_2.setCurrentText(money_type)
            else:
                self.AccExtra_2.setText(extra)
        elif self.tabWidget.currentIndex() == 2:
            self.AccID_3.setText(id)
            self.dateEdit_3.setDate(datetime.datetime.strptime(date, "%Y-%m-%d"))
            self.AccPoss_3.setText(rest)
            self.AccBank_3.setCurrentText(bank)
            if self.savingState:
                self.AccRate_3.setText(rate)
                self.currencyType_3.setCurrentText(money_type)
            else:
                self.AccExtra_3.setText(extra)
        if self.tabWidget.currentIndex() == 3:
            self.AccID_4.setText(id)
            self.dateEdit_4.setDate(datetime.datetime.strptime(date, "%Y-%m-%d"))
            self.AccPoss_4.setText(rest)
            self.AccBank_4.setCurrentText(bank)
            if self.savingState:
                self.AccRate_4.setText(rate)
                self.currencyType_4.setCurrentText(money_type)
            else:
                self.AccExtra_4.setText(extra)

    def showAllTable(self):
        session = db.sessionmaker(self.engine)()
        if self.savingState:
            data = session.query(db.SaveAccount).all()
        else:
            data = session.query(db.CheckAccount).all()
        self.showAccount(data)
        session.commit()
        session.close()

    def addAccount(self):
        self.savingState = self.isSaving.checkState()
        aid = self.AccID.text()
        rest = self.AccPoss.text()
        date = self.dateEdit.text()
        bank_name = self.AccBank.currentText()
        rate = self.AccRate.text()
        cType = self.currencyType.currentText()
        extra = self.AccExtra.text()
        try:
            db.addAccount(self.engine, self.savingState, aid, rest, date, bank_name, rate, cType, extra)
        except IntegrityError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong')
            msgBox.exec_()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, perhaps data too long or not fit '
                                                               'right format.')
            msgBox.exec_()
            return
        self.showAllTable()

    def queryAccount(self):
        if self.tabWidget.currentIndex() == 1:
            self.args['id'] = self.AccID_2.text()
            self.args['rest'] = self.AccPoss_2.text()
            self.args['date'] = self.dateEdit_2.text()
            self.args['bank_name'] = self.AccBank_2.currentText()
            self.args['rate'] = self.AccRate_2.text()
            self.args['money_type'] = self.currencyType_2.currentText()
            self.args['extra'] = self.AccExtra_2.text()
        elif self.tabWidget.currentIndex() == 2:
            self.args['id'] = self.AccID_3.text()
            self.args['rest'] = self.AccPoss_3.text()
            self.args['date'] = self.dateEdit_3.text()
            self.args['bank_name'] = self.AccBank_3.currentText()
            self.args['rate'] = self.AccRate_3.text()
            self.args['money_type'] = self.currencyType_3.currentText()
            self.args['extra'] = self.AccExtra_3.text()
        elif self.tabWidget.currentIndex() == 3:
            self.args['id'] = self.AccID_4.text()
            self.args['rest'] = self.AccPoss_4.text()
            self.args['date'] = self.dateEdit_4.text()
            self.args['bank_name'] = self.AccBank_4.currentText()
            self.args['rate'] = self.AccRate_4.text()
            self.args['money_type'] = self.currencyType_4.currentText()
            self.args['extra'] = self.AccExtra_4.text()
        self.args = db.argStr2None(self.args)
        if self.savingState:
            self.args.pop('extra')
        else:
            self.args.pop('money_type')
            self.args.pop('rate')
        if self.args['id']:
            self.args['id'] = '%' + self.args['id'] + '%'
        self.args['date'] = datetime.datetime.strptime(self.args['date'], "%Y/%m/%d")

        filt = []
        if self.savingState:
            filt.append(db.SaveAccount.id.like(self.args['id']) if self.args['id']
                        else or_(db.SaveAccount.id.like('%%'), db.SaveAccount.id.is_(None)))
            filt.append(db.SaveAccount.rest == float(self.args['rest']) if self.args['rest']
                        else or_(db.SaveAccount.rest.like('%%'), db.SaveAccount.rest.is_(None)))
            filt.append(db.SaveAccount.date ==self.args['date'])
            filt.append(db.SaveAccount.bank_name.like(self.args['bank_name']) if self.args['bank_name']
                        else or_(db.SaveAccount.bank_name.like('%%'), db.SaveAccount.bank_name.is_(None)))
            filt.append(db.SaveAccount.rate.like(self.args['rate']) if self.args['rate']
                        else or_(db.SaveAccount.rate.like('%%'), db.SaveAccount.rate.is_(None)))
            filt.append(db.SaveAccount.money_type.like(self.args['money_type']) if self.args['money_type']
                        else or_(db.SaveAccount.money_type.like('%%'), db.SaveAccount.money_type.is_(None)))
        else:
            filt.append(db.CheckAccount.id.like(self.args['id'])if self.args['id']
                        else or_(db.CheckAccount.id.like('%%'), db.CheckAccount.id.is_(None)))
            filt.append(db.CheckAccount.rest.like(self.args['rest']) if self.args['rest']
                        else or_(db.CheckAccount.rest.like('%%'), db.CheckAccount.rest.is_(None)))
            filt.append(db.CheckAccount.date.like(self.args['date']) if self.args['date']
                        else or_(db.CheckAccount.date.like('%%'), db.CheckAccount.date.is_(None)))
            filt.append(db.CheckAccount.bank_name.like(self.args['bank_name']) if self.args['bank_name']
                        else or_(db.CheckAccount.bank_name.like('%%'), db.CheckAccount.bank_name.is_(None)))
            filt.append(db.CheckAccount.extra.like(self.args['extra']) if self.args['extra']
                        else or_(db.CheckAccount.extra.like('%%'), db.CheckAccount.extra.is_(None)))
        session = db.sessionmaker(self.engine)()
        if self.savingState:
            data = session.query(db.SaveAccount).filter(*filt).all()
        else:
            data = session.query(db.CheckAccount).filter(*filt).all()
        self.showAccount(data)
        session.commit()
        session.close()

    def delAccount(self):
        self.savingState = self.isSaving.checkState()
        id = self.AccID_2.text()
        msgBox = QMessageBox(QMessageBox.Warning, 'Warning', 'Are you sure to delete? It is not invertible')
        msgBox.exec_()
        session = db.sessionmaker(self.engine)()
        if self.savingState:
            data = session.query(db.SaveAccount).filter(db.SaveAccount.id == id)
        else:
            data = session.query(db.CheckAccount).filter(db.CheckAccount.id == id)
        data.delete()
        session.commit()
        session.close()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        if self.savingState:
            data = session.query(db.SaveAccount).all()
        else:
            data = session.query(db.CheckAccount).all()
        self.showAccount(data)
        session.commit()
        session.close()

    def updateAccount(self):
        self.savingState = self.isSaving.checkState()
        aid = self.AccID_3.text()
        self.args['id'] = self.AccID_3.text()
        self.args['rest'] = self.AccPoss_3.text()
        self.args['date'] = self.dateEdit_3.text()
        self.args['bank_name'] = self.AccBank_3.currentText()
        self.args['rate'] = self.AccRate_3.text()
        self.args['money_type'] = self.currencyType_3.currentText()
        self.args['extra'] = self.AccExtra_3.text()
        self.args = db.argStr2None(self.args)
        session = db.sessionmaker(self.engine)()

        if self.savingState:
            self.args.pop('extra')
        else:
            self.args.pop('money_type')
            self.args.pop('rate')
        if self.savingState:
            data = session.query(db.SaveAccount).filter(db.SaveAccount.id == aid).update(self.args)
        else:
            data = session.query(db.CheckAccount).filter(db.SaveAccount.id == aid).update(self.args)
        session.commit()
        session.close()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        if self.savingState:
            data = session.query(db.SaveAccount).all()
        else:
            data = session.query(db.CheckAccount).all()
        self.showAccount(data)
        session.commit()
        session.close()

    def showAccount(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(data))
        if self.savingState:
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem())
            self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem())
            self.tableWidget.horizontalHeaderItem(4).setText('利率')
            self.tableWidget.horizontalHeaderItem(5).setText('货币类型')
            for i in range(len(data)):
                row = data[i]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(row.id))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.rest)))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.date)))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(row.bank_name))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(row.rate)))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(row.money_type))
                # self.tableWidget.setItem(i, 6, QTableWidgetItem(row.id))
        else:
            self.tableWidget.setHorizontalHeaderItem(4, QTableWidgetItem())
            self.tableWidget.setHorizontalHeaderItem(5, QTableWidgetItem())
            self.tableWidget.horizontalHeaderItem(4).setText('透支额')
            self.tableWidget.horizontalHeaderItem(5).setText('')
            for i in range(len(data)):
                row = data[i]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(row.id))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.rest)))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.date)))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(row.bank_name))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(str(row.extra)))


