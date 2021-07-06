from UI.loans import Ui_Loans
import db

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError, OperationalError, MultipleResultsFound
from PyQt5.Qt import QMessageBox
import datetime
from sqlalchemy import or_, func

status2txt = {0: "未开始发放", 1: "未发放完", 2: "已全部发放"}


class LoansUI(QWidget, Ui_Loans):
    def __init__(self):
        super(LoansUI, self).__init__()
        self.engine = None
        self.setupUi(self)
        self.pushButton_4.clicked.connect(self.addLoan)
        self.pushButton_2.clicked.connect(self.queryLoan)
        self.tableWidget.clicked.connect(self.setTextFromTable)
        self.pushButton.clicked.connect(self.delLoan)
        self.toolButton.clicked.connect(self.showAllTable)
        self.pushButton_6.clicked.connect(self.giveMoney)
        self.lineEdit.textEdited.connect(self.queryLoan)

    def getTableText(self, row, col):
        try:
            result = self.tableWidget.item(row, col).text()
        except AttributeError:
            result = ''
        return result

    def setTextFromTable(self):
        row = self.tableWidget.currentRow()
        id = self.getTableText(row, 0)
        total_money = self.getTableText(row, 1)
        bank_name = self.getTableText(row, 2)

        self.lineEdit.setText(id)
        self.lineEdit_2.setText(total_money)
        self.comboBox.setCurrentText(bank_name)

    def showAllTable(self):
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Loan).all()
        self.showLoans(data)
        session.commit()
        session.close()

    def queryLoan(self):
        args = {}
        args['id'] = self.lineEdit.text()
        args['total_money'] = self.lineEdit_2.text()
        args['bank_name'] = self.comboBox.currentText()
        args['money'] = self.lineEdit_3.text()
        args['date'] = datetime.datetime.now()
        args = db.argStr2None(args)
        filt = []
        filt.append(db.Loan.id.like('%' + args['id'] + '%') if args['id']
                    else or_(db.Loan.id.like('%%'), db.Loan.id.is_(None)))
        filt.append(db.Loan.bank_name.like('%' + args['bank_name'] + '%') if args['bank_name']
                    else or_(db.Loan.bank_name.like('%%'), db.Loan.bank_name.is_(None)))
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Loan).filter(*filt).all()
        self.showLoans(data)
        session.commit()
        session.close()

    def showLoans(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            row = data[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.id))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.total_money)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(row.bank_name))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(status2txt[row.status]))

    def addLoan(self):
        args = {}
        args['id'] = self.lineEdit.text()
        args['total_money'] = self.lineEdit_2.text()
        args['bank_name'] = self.comboBox.currentText()
        args['money'] = self.lineEdit_3.text()
        args['date'] = datetime.datetime.now()
        try:
            tm = float(args['total_money'])
        except ValueError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Must set money POSITIVE')
            msgBox.exec_()
            return
        if tm <= 0:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Must set money POSITIVE')
            msgBox.exec_()
            return
        try:
            session = db.sessionmaker(self.engine)()
            db.addLoan(session, args['id'], args['total_money'], args['bank_name'])
            session.commit()
            session.close()
        except OperationalError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Check Primary key')
            msgBox.exec_()
            return
        except IntegrityError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, Maybe Duplicate ID')
            msgBox.exec_()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, perhaps data too long or not fit '
                                                               'right format.')
            msgBox.exec_()
            return
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Loan).all()
        self.showLoans(data)
        session.commit()
        session.close()

    def delLoan(self):
        args = {}
        args['id'] = self.lineEdit.text()
        args['total_money'] = self.lineEdit_2.text()
        args['bank_name'] = self.comboBox.currentText()

        session = db.sessionmaker(self.engine)()
        try:
            item = session.query(db.Loan).filter(db.Loan.id == args['id']).one()
        except MultipleResultsFound:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong')
            msgBox.exec_()
            return
        if item.status == 1:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', '贷款没放完，不可删除')
            msgBox.exec_()
            return
        else:
            session.query(db.Loan).filter(db.Loan.id == args['id']).delete()
        session.commit()
        session.close()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Loan).all()
        self.showLoans(data)
        session.commit()
        session.close()

    def giveMoney(self):
        args = {}
        args['loan_id'] = self.lineEdit.text()
        args['bank_name'] = self.comboBox.currentText()
        args['total_money'] = self.lineEdit_2.text()
        args['money'] = self.lineEdit_3.text()
        args['cus_id'] = self.lineEdit_4.text()
        args['date'] = datetime.datetime.now()
        args = db.argStr2None(args)
        session = db.sessionmaker(self.engine)()
        session.add(db.Pay(date=args['date'], money=args['money'], loan_id=args['loan_id'], cus_id=args['cus_id']))
        try:
            tm = float(args['money'])
        except ValueError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Must set money POSITIVE')
            msgBox.exec_()
            return
        if tm <= 0:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Must set money POSITIVE')
            msgBox.exec_()
            return
        try:
            session.flush()
        except IntegrityError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The give money SQL is wrong')
            msgBox.exec_()
            session.close()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error',
                                 'The give money SQL is wrong, perhaps data too long or not fit ')
            msgBox.exec_()
            session.close()
            return
        if not session.query(db.CustomerToLoan).filter(db.CustomerToLoan.cus_id == args['cus_id'],
                                                       db.CustomerToLoan.loan_id == args['loan_id']).all():
            session.add(db.CustomerToLoan(cus_id=args['cus_id'], loan_id=args['loan_id']))
        try:
            session.flush()
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error',
                                 'cus_id SQL may be wrong, perhaps data too long or not fit ')
            msgBox.exec_()
            session.close()
            return
        total_pay = session.query(func.sum(db.Pay.money)).filter(db.Pay.loan_id == args['loan_id']).scalar()
        try:
            item = session.query(db.Loan).filter(db.Loan.id == args['loan_id']).one()
        except MultipleResultsFound:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error',
                                 'The SQL is wrong, Maybe Duplicate ID')
            msgBox.exec_()
            return
        if total_pay:
            if total_pay == item.total_money:
                item.status = 2
                session.flush()
            elif total_pay < item.total_money:
                item.status = 1
                session.flush()
            else:
                msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'pay too much')
                msgBox.exec_()
                session.rollback()
        session.commit()
        session.close()
        self.showAllTable()
