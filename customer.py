from UI.customer import Ui_customer
import db
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError,OperationalError
from PyQt5.Qt import QMessageBox
from sqlalchemy import or_
import traceback


class CustomerUI(QWidget, Ui_customer):
    def __init__(self):
        super(CustomerUI, self).__init__()
        self.engine = None
        self.setupUi(self)
        self.customerAdd.clicked.connect(self.addCustomer)
        self.CusQueryButton.clicked.connect(self.queryCustomer)
        self.CusDelButton.clicked.connect(self.delCustomer)
        self.CusQueryButton_3.clicked.connect(self.updateCustomer)
        self.CusID_2.textChanged.connect(self.queryCustomer)
        self.CusID_3.textChanged.connect(self.queryCustomer)
        self.CusID_4.textChanged.connect(self.queryCustomer)
        self.clearButton_2.clicked.connect(self.tableWidget.clearContents)
        self.tableWidget.clicked.connect(self.setTextFromTable)
        self.toolButton.clicked.connect(self.showAllTable)

    def getTableText(self, row, col):
        try:
            result = self.tableWidget.item(row, col).text()
        except AttributeError:
            result = ''
        return result

    def setTextFromTable(self):
        if self.tabWidget.currentIndex() == 0:
            return
        if self.tabWidget.currentIndex() == 1:
            return
        row = self.tableWidget.currentRow()
        id = self.getTableText(row, 0)
        name = self.getTableText(row, 1)
        phone = self.getTableText(row, 2)
        address = self.getTableText(row, 3)
        contact_name = self.getTableText(row, 4)
        contact_phone = self.getTableText(row, 5)
        contact_mail = self.getTableText(row, 6)
        contact_relation = self.getTableText(row, 7)
        employee = self.getTableText(row, 8)
        if self.tabWidget.currentIndex() == 2:
            self.CusID_3.setText(id)
            self.CusName_3.setText(name)
            self.CusPhone_3.setText(phone)
            self.CusAddress_3.setText(address)
            self.CusCname_3.setText(contact_name)
            self.CusCphone_3.setText(contact_phone)
            self.CusCaddr_3.setText(contact_mail)
            self.CusRela_3.setText(contact_relation)
            self.CusEmployee2_2.setText(employee)
        if self.tabWidget.currentIndex() == 3:
            self.CusID_4.setText(id)
            self.CusName_4.setText(name)
            self.CusPhone_4.setText(phone)
            self.CusAddress_4.setText(address)
            self.CusCname_4.setText(contact_name)
            self.CusCphone_4.setText(contact_phone)
            self.CusCaddr_4.setText(contact_mail)
            self.CusRela_4.setText(contact_relation)
            self.CusEmployee2_3.setText(employee)

    def addCustomer(self):
        id = self.CusAddID.text()
        name = self.CusAddName.text()
        phone = self.CusAddPhone.text()
        address = self.CusAddAddress.text()
        contact_name = self.CusAddCname.text()
        contact_phone = self.CusAddCphone.text()
        contact_mail = self.CusAddCaddr.text()
        contact_relation = self.CusAddRela.text()
        # employee = self.CusEmployee.text()
        employee = self.CusEmployee.currentText()

        try:
            session = db.sessionmaker(self.engine)()
            db.addCustomer(session, id, name, phone, address, contact_name, contact_phone, contact_mail,
                           contact_relation, employee)

            session.commit()
            session.close()
        except IntegrityError:
            print(IntegrityError)
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong. Duplicate detect')
            msgBox.exec_()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, perhaps data too long or not fit '
                                                               'right format.')
            msgBox.exec_()
            return
        except OperationalError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Maybe try to set ID')
            msgBox.exec_()
            return

        self.showAllTable()

    def showAllTable(self):
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def queryCustomer(self):
        args = {}
        if self.tabWidget.currentIndex() == 1:
            args['id'] = self.CusID_2.text()
            args['name'] = self.CusName_2.text()
            args['phone'] = self.CusPhone_2.text()
            args['address'] = self.CusAddress_2.text()
            args['contact_name'] = self.CusCname_2.text()
            args['contact_phone'] = self.CusCphone_2.text()
            args['contact_email'] = self.CusCaddr_2.text()
            args['contact_relation'] = self.CusRela_2.text()
            args['empl_id'] = self.CusEmployee2.text()
        elif self.tabWidget.currentIndex() == 2:
            args['id'] = self.CusID_3.text()
            args['name'] = self.CusName_3.text()
            args['phone'] = self.CusPhone_3.text()
            args['address'] = self.CusAddress_3.text()
            args['contact_name'] = self.CusCname_3.text()
            args['contact_phone'] = self.CusCphone_3.text()
            args['contact_email'] = self.CusCaddr_3.text()
            args['contact_relation'] = self.CusRela_3.text()
            args['empl_id'] = self.CusEmployee2_2.text()
        elif self.tabWidget.currentIndex() == 3:
            args['id'] = self.CusID_4.text()
            args['name'] = self.CusName_4.text()
            args['phone'] = self.CusPhone_4.text()
            args['address'] = self.CusAddress_4.text()
            args['contact_name'] = self.CusCname_4.text()
            args['contact_phone'] = self.CusCphone_4.text()
            args['contact_email'] = self.CusCaddr_4.text()
            args['contact_relation'] = self.CusRela_4.text()
            args['empl_id'] = self.CusEmployee2_3.text()
        args = db.argStr2None(args)
        for k in args.keys():
            if args[k]:
                args[k] = '%' + args[k] + '%'
        filt = []
        filt.append(db.Customer.id.like(args['id']) if args['id']
                    else or_(db.Customer.id.like('%%'), db.Customer.id.is_(None)))
        filt.append(db.Customer.name.like(args['name']) if args['name']
                    else or_(db.Customer.name.like('%%'), db.Customer.name.is_(None)))
        filt.append(db.Customer.phone.like(args['phone']) if args['phone']
                    else or_(db.Customer.phone.like('%%'), db.Customer.phone.is_(None)))
        filt.append(db.Customer.address.like(args['address']) if args['address']
                    else or_(db.Customer.address.like('%%'), db.Customer.address.is_(None)))
        filt.append(db.Customer.contact_email.like(args['contact_email']) if args['contact_email']
                    else or_(db.Customer.contact_email.like('%%'), db.Customer.contact_email.is_(None)))
        filt.append(db.Customer.contact_phone.like(args['contact_phone']) if args['contact_phone']
                    else or_(db.Customer.contact_phone.like('%%'), db.Customer.contact_phone.is_(None)))
        filt.append(db.Customer.contact_relation.like(args['contact_relation']) if args['contact_relation']
                    else or_(db.Customer.contact_relation.like('%%'), db.Customer.contact_relation.is_(None)))
        filt.append(db.Customer.empl_id.like(args['empl_id']) if args['empl_id']
                    else or_(db.Customer.empl_id.like('%%'), db.Customer.empl_id.is_(None)))

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).filter(*filt).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def delCustomer(self):
        id = self.CusID_3.text()
        try:
            session = db.sessionmaker(self.engine)()
            data = session.query(db.Customer).filter(db.Customer.id == id)
            flag = data.delete()
            session.commit()
            session.close()
        except IntegrityError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Cannot delete a customer with an Account or A loan')
            msgBox.exec_()
            return
        if not flag:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'No result found')
            msgBox.exec_()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def updateCustomer(self):
        args = {}
        id = self.CusID_4.text()
        args['name'] = self.CusName_4.text()
        args['phone'] = self.CusPhone_4.text()
        args['address'] = self.CusAddress_4.text()
        args['contact_name'] = self.CusCname_4.text()
        args['contact_phone'] = self.CusCphone_4.text()
        args['contact_email'] = self.CusCaddr_4.text()
        args['contact_relation'] = self.CusRela_4.text()
        args['empl_id'] = self.CusEmployee2_3.text()
        args = db.argStr2None(args)
        try:
            session = db.sessionmaker(self.engine)()
            flag = session.query(db.Customer).filter(db.Customer.id == id).update(args)
            if not flag:
                msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'No result found')
                msgBox.exec_()
            session.commit()
            session.close()
        except IntegrityError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'SQL wrong, Maybe reference wrong')
            msgBox.exec_()
            return
        except DataError:
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'The SQL is wrong, perhaps data too long or not fit '
                                                               'right format.')
            msgBox.exec_()
            return


        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def showCustomer(self, data):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(data))
        for i in range(len(data)):
            row = data[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.id))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row.name))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(row.phone))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(row.address))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(row.contact_name))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(row.contact_phone))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(row.contact_email))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(row.contact_relation))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(row.empl_id))
