# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customer(object):
    def setupUi(self, customer):
        customer.setObjectName("customer")
        customer.resize(571, 422)
        self.verticalLayout = QtWidgets.QVBoxLayout(customer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(customer)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.graphicsView = QtWidgets.QGraphicsView(customer)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.tableView = QtWidgets.QTableView(customer)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(customer)
        QtCore.QMetaObject.connectSlotsByName(customer)

    def retranslateUi(self, customer):
        _translate = QtCore.QCoreApplication.translate
        customer.setWindowTitle(_translate("customer", "Form"))
        self.label.setText(_translate("customer", "Customer Manager"))
