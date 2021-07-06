from UI.business import Ui_business
import db

from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError, OperationalError, MultipleResultsFound
from PyQt5.Qt import QMessageBox
import datetime
from sqlalchemy import or_, func,distinct


class BusinessUI(QWidget, Ui_business):
    def __init__(self):
        super(BusinessUI, self).__init__()
        self.engine = None
        self.setupUi(self)
        self.savingState = self.checkBox.checkState()
        self.checkBox.clicked.connect(self.checkSavingState)
        self.checkBox_2.clicked.connect(self.checkSavingState)
        self.pushButton.clicked.connect(self.queryBusiness)

    def checkSavingState(self):
        self.savingState = self.checkBox.checkState()

    def queryBusiness(self):
        self.checkSavingState()
        startTime = self.dateEdit.text()
        endTime = self.dateEdit_2.text()
        startTime = datetime.datetime.strptime(startTime, "%Y/%m/%d")
        endTime = datetime.datetime.strptime(endTime, "%Y/%m/%d")
        if self.savingState:
            session = db.sessionmaker(self.engine)()
            data = session.query(db.SaveAccount.bank_name, func.count(db.CustomerToSA.cus_id).label('cus_id'),
                                 func.sum(db.SaveAccount.rest).label('rest')).filter(db.SaveAccount.date >= startTime,
                                    db.SaveAccount.date <= endTime, db.SaveAccount.id == db.CustomerToSA.sa_id).\
                group_by(db.SaveAccount.bank_name).all()
            self.showBusiness(data)
            session.commit()
            session.close()
            # print(len(data))
            # print(data[0].cus_id)
        else:
            session = db.sessionmaker(self.engine)()
            data = session.query(db.Loan.bank_name, func.count(distinct(db.CustomerToLoan.cus_id)).label('cus_id'),
                                 func.sum(db.Pay.money).label('rest')).filter(db.Pay.date >= startTime,
                                    db.Pay.date <= endTime, db.Pay.loan_id==db.CustomerToLoan.loan_id,
                                    db.Loan.id == db.CustomerToLoan.loan_id).group_by(db.Loan.bank_name).all()
            self.showBusiness(data)
            session.commit()
            session.close()
        if len(data) == 0:
            msgBox = QMessageBox(QMessageBox.Warning, 'Warning', 'No result')
            msgBox.exec_()


    def showBusiness(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            row = data[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.bank_name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(row.cus_id)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(row.rest)))
