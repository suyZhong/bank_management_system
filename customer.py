from UI.customer import Ui_customer
import db
from PyQt5.Qt import QStackedLayout
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from sqlalchemy.exc import IntegrityError, DataError
from PyQt5.Qt import QMessageBox

class CustomerUI(QWidget, Ui_customer):
    def __init__(self):
        super(CustomerUI, self).__init__()
        self.engine = None
        self.setupUi(self)
        self.customerAdd.clicked.connect(self.addCustomer)
        self.CusQueryButton.clicked.connect(self.queryCustomer)

    def addCustomer(self):
        id = self.CusAddID.text()
        name = self.CusAddName.text()
        phone = self.CusAddPhone.text()
        address = self.CusAddAddress.text()
        contact_name = self.CusAddCname.text()
        contact_phone = self.CusAddCphone.text()
        contact_mail = self.CusAddCaddr.text()
        contact_relation = self.CusAddRela.text()
        try:
            db.addCustomer(self.engine, id, name, phone, address, contact_name, contact_phone, contact_mail, contact_relation)
        except IntegrityError:
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
        id = self.CusAddID.text()
        name = self.CusAddName.text()
        phone = self.CusAddPhone.text()
        address = self.CusAddAddress.text()
        contact_name = self.CusAddCname.text()
        contact_phone = self.CusAddCphone.text()
        contact_mail = self.CusAddCaddr.text()
        contact_relation = self.CusAddRela.text()

        session = db.sessionmaker(self.engine)()

        session.commit()
        session.close()

    def showCustomer(self,data):
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
