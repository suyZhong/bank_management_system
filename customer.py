from UI.customer import Ui_customer
import db
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError
from PyQt5.Qt import QMessageBox
from sqlalchemy import or_


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
            self.CusPhone_3.setText(contact_phone)
            self.CusAddress_3.setText(contact_mail)
            self.CusRela_3.setText(contact_relation)
            self.CusEmployee2_3.setText(employee)
        if self.tabWidget.currentIndex() == 3:
            self.CusID_4.setText(id)
            self.CusName_4.setText(name)
            self.CusPhone_4.setText(phone)
            self.CusAddress_4.setText(address)
            self.CusCname_4.setText(contact_name)
            self.CusPhone_4.setText(contact_phone)
            self.CusAddress_4.setText(contact_mail)
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
            db.addCustomer(self.engine, id, name, phone, address, contact_name, contact_phone, contact_mail,
                           contact_relation, employee)
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
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def queryCustomer(self):
        if self.tabWidget.currentIndex() == 1:
            idd = '%' + self.CusID_2.text() + '%'
            name = '%' + self.CusName_2.text() + '%'
            phone = '%' + self.CusPhone_2.text() + '%'
            address = '%' + self.CusAddress_2.text() + '%'
            contact_name = '%' + self.CusCname_2.text() + '%'
            contact_phone = '%' + self.CusCphone_2.text() + '%'
            contact_mail = '%' + self.CusCaddr_2.text() + '%'
            contact_relation = '%' + self.CusRela_2.text() + '%'
            employee = '%' + self.CusEmployee2.text() + '%'
        elif self.tabWidget.currentIndex() == 2:
            idd = '%' + self.CusID_3.text() + '%'
            name = '%' + self.CusName_3.text() + '%'
            phone = '%' + self.CusPhone_3.text() + '%'
            address = '%' + self.CusAddress_3.text() + '%'
            contact_name = '%' + self.CusCname_3.text() + '%'
            contact_phone = '%' + self.CusCphone_3.text() + '%'
            contact_mail = '%' + self.CusCaddr_3.text() + '%'
            contact_relation = '%' + self.CusRela_3.text() + '%'
            employee = '%' + self.CusEmployee2_2.text() + '%'
        elif self.tabWidget.currentIndex() == 3:
            idd = '%' + self.CusID_4.text() + '%'
            name = '%' + self.CusName_4.text() + '%'
            phone = '%' + self.CusPhone_4.text() + '%'
            address = '%' + self.CusAddress_4.text() + '%'
            contact_name = '%' + self.CusCname_4.text() + '%'
            contact_phone = '%' + self.CusCphone_4.text() + '%'
            contact_mail = '%' + self.CusCaddr_4.text() + '%'
            contact_relation = '%' + self.CusRela_4.text() + '%'
            employee = '%' + self.CusEmployee2_3.text() + '%'

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).filter(db.Customer.id.like(idd),
                                                 db.Customer.name.like(name),
                                                 db.Customer.phone.like(phone),
                                                 db.Customer.address.like(address),
                                                 db.Customer.contact_name.like(contact_name),
                                                 db.Customer.contact_phone.like(contact_phone),
                                                 db.Customer.contact_email.like(contact_mail),
                                                 db.Customer.contact_relation.like(contact_relation),
                                                 or_(db.Customer.empl_id.like(employee),
                                                     db.Customer.empl_id.is_(None))).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def delCustomer(self):
        id = self.CusID_3.text()
        msgBox = QMessageBox(QMessageBox.Warning, 'Warning', 'Are you sure to delete? It is not invertible')
        msgBox.exec_()
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).filter(db.Customer.id == id)
        data.delete()
        session.commit()
        session.close()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def updateCustomer(self):
        id = self.CusID_4.text()
        name = self.CusName_4.text()
        phone = self.CusPhone_4.text()
        address = self.CusAddress_4.text()
        contact_name = self.CusCname_4.text()
        contact_phone = self.CusCphone_4.text()
        contact_mail = self.CusCaddr_4.text()
        contact_relation = self.CusRela_4.text()
        employee = self.CusEmployee2_3.text()
        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).filter(db.Customer.id == id).update(
            {'name': name, 'phone': phone, 'address': address, 'contact_name': contact_name,
             'contact_phone': contact_phone, 'contact_email': contact_mail, 'contact_relation': contact_relation,
             'empl_id': employee})
        session.commit()
        session.close()

        session = db.sessionmaker(self.engine)()
        data = session.query(db.Customer).all()
        self.showCustomer(data)
        session.commit()
        session.close()

    def showCustomer(self, data):
        self.tableWidget.clearContents()
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
