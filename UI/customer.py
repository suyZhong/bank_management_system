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
        customer.resize(1003, 586)
        self.gridLayout = QtWidgets.QGridLayout(customer)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(customer)
        self.tabWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.add = QtWidgets.QWidget()
        self.add.setObjectName("add")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.add)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.CusAddCphone = QtWidgets.QLineEdit(self.add)
        self.CusAddCphone.setObjectName("CusAddCphone")
        self.gridLayout_3.addWidget(self.CusAddCphone, 14, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.add)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 8, 1, 1, 1)
        self.CusAddAddress = QtWidgets.QLineEdit(self.add)
        self.CusAddAddress.setObjectName("CusAddAddress")
        self.gridLayout_3.addWidget(self.CusAddAddress, 7, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.add)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.CusAddName = QtWidgets.QLineEdit(self.add)
        self.CusAddName.setObjectName("CusAddName")
        self.gridLayout_3.addWidget(self.CusAddName, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.add)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 8, 0, 1, 1)
        self.CusAddID = QtWidgets.QLineEdit(self.add)
        self.CusAddID.setObjectName("CusAddID")
        self.gridLayout_3.addWidget(self.CusAddID, 1, 0, 1, 2)
        self.CusAddPhone = QtWidgets.QLineEdit(self.add)
        self.CusAddPhone.setText("")
        self.CusAddPhone.setObjectName("CusAddPhone")
        self.gridLayout_3.addWidget(self.CusAddPhone, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.add)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 1, 1, 1)
        self.CusAddCname = QtWidgets.QLineEdit(self.add)
        self.CusAddCname.setObjectName("CusAddCname")
        self.gridLayout_3.addWidget(self.CusAddCname, 9, 0, 1, 1)
        self.CusAddCaddr = QtWidgets.QLineEdit(self.add)
        self.CusAddCaddr.setObjectName("CusAddCaddr")
        self.gridLayout_3.addWidget(self.CusAddCaddr, 11, 0, 1, 2)
        self.CusAddRela = QtWidgets.QLineEdit(self.add)
        self.CusAddRela.setObjectName("CusAddRela")
        self.gridLayout_3.addWidget(self.CusAddRela, 9, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.add)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 10, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.add)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)
        self.customerAdd = QtWidgets.QPushButton(self.add)
        self.customerAdd.setDefault(True)
        self.customerAdd.setObjectName("customerAdd")
        self.gridLayout_3.addWidget(self.customerAdd, 20, 0, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.add)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.add)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 12, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.add)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.clearButton = QtWidgets.QPushButton(self.add)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout_3.addWidget(self.clearButton, 19, 0, 1, 2)
        self.CusEmployee = QtWidgets.QComboBox(self.add)
        self.CusEmployee.setObjectName("CusEmployee")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.CusEmployee.addItem("")
        self.gridLayout_3.addWidget(self.CusEmployee, 14, 1, 1, 1)
        self.tabWidget.addTab(self.add, "")
        self.query = QtWidgets.QWidget()
        self.query.setObjectName("query")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.query)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CusPhone_2 = QtWidgets.QLineEdit(self.query)
        self.CusPhone_2.setText("")
        self.CusPhone_2.setObjectName("CusPhone_2")
        self.gridLayout_2.addWidget(self.CusPhone_2, 3, 1, 1, 1)
        self.CusAddress_2 = QtWidgets.QLineEdit(self.query)
        self.CusAddress_2.setObjectName("CusAddress_2")
        self.gridLayout_2.addWidget(self.CusAddress_2, 5, 0, 1, 2)
        self.CusRela_2 = QtWidgets.QLineEdit(self.query)
        self.CusRela_2.setObjectName("CusRela_2")
        self.gridLayout_2.addWidget(self.CusRela_2, 7, 1, 1, 1)
        self.clearButton_2 = QtWidgets.QPushButton(self.query)
        self.clearButton_2.setObjectName("clearButton_2")
        self.gridLayout_2.addWidget(self.clearButton_2, 14, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(self.query)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.query)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.query)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 10, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.query)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 2, 1, 1, 1)
        self.CusID_2 = QtWidgets.QLineEdit(self.query)
        self.CusID_2.setObjectName("CusID_2")
        self.gridLayout_2.addWidget(self.CusID_2, 1, 0, 1, 2)
        self.CusName_2 = QtWidgets.QLineEdit(self.query)
        self.CusName_2.setObjectName("CusName_2")
        self.gridLayout_2.addWidget(self.CusName_2, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.query)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 6, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.query)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 4, 0, 1, 1)
        self.CusQueryButton = QtWidgets.QPushButton(self.query)
        self.CusQueryButton.setDefault(True)
        self.CusQueryButton.setObjectName("CusQueryButton")
        self.gridLayout_2.addWidget(self.CusQueryButton, 15, 0, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.query)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 6, 0, 1, 1)
        self.CusCname_2 = QtWidgets.QLineEdit(self.query)
        self.CusCname_2.setObjectName("CusCname_2")
        self.gridLayout_2.addWidget(self.CusCname_2, 7, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.query)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 8, 0, 1, 1)
        self.CusCaddr_2 = QtWidgets.QLineEdit(self.query)
        self.CusCaddr_2.setObjectName("CusCaddr_2")
        self.gridLayout_2.addWidget(self.CusCaddr_2, 9, 0, 1, 2)
        self.CusCphone_2 = QtWidgets.QLineEdit(self.query)
        self.CusCphone_2.setObjectName("CusCphone_2")
        self.gridLayout_2.addWidget(self.CusCphone_2, 11, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.query)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 10, 1, 1, 1)
        self.CusEmployee2 = QtWidgets.QLineEdit(self.query)
        self.CusEmployee2.setObjectName("CusEmployee2")
        self.gridLayout_2.addWidget(self.CusEmployee2, 11, 1, 1, 1)
        self.tabWidget.addTab(self.query, "")
        self.dele = QtWidgets.QWidget()
        self.dele.setObjectName("dele")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.dele)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_23 = QtWidgets.QLabel(self.dele)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 8, 0, 1, 1)
        self.CusEmployee2_2 = QtWidgets.QLineEdit(self.dele)
        self.CusEmployee2_2.setObjectName("CusEmployee2_2")
        self.gridLayout_4.addWidget(self.CusEmployee2_2, 11, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.dele)
        self.label_28.setObjectName("label_28")
        self.gridLayout_4.addWidget(self.label_28, 4, 0, 1, 1)
        self.CusCname_3 = QtWidgets.QLineEdit(self.dele)
        self.CusCname_3.setObjectName("CusCname_3")
        self.gridLayout_4.addWidget(self.CusCname_3, 7, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.dele)
        self.label_27.setObjectName("label_27")
        self.gridLayout_4.addWidget(self.label_27, 10, 0, 1, 1)
        self.CusDelButton = QtWidgets.QPushButton(self.dele)
        self.CusDelButton.setDefault(True)
        self.CusDelButton.setObjectName("CusDelButton")
        self.gridLayout_4.addWidget(self.CusDelButton, 13, 0, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.dele)
        self.label_29.setObjectName("label_29")
        self.gridLayout_4.addWidget(self.label_29, 6, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.dele)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 10, 1, 1, 1)
        self.CusPhone_3 = QtWidgets.QLineEdit(self.dele)
        self.CusPhone_3.setText("")
        self.CusPhone_3.setObjectName("CusPhone_3")
        self.gridLayout_4.addWidget(self.CusPhone_3, 3, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.dele)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 6, 0, 1, 1)
        self.CusRela_3 = QtWidgets.QLineEdit(self.dele)
        self.CusRela_3.setObjectName("CusRela_3")
        self.gridLayout_4.addWidget(self.CusRela_3, 7, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.dele)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.dele)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 2, 0, 1, 1)
        self.clearButton_3 = QtWidgets.QPushButton(self.dele)
        self.clearButton_3.setObjectName("clearButton_3")
        self.gridLayout_4.addWidget(self.clearButton_3, 12, 0, 1, 2)
        self.CusCaddr_3 = QtWidgets.QLineEdit(self.dele)
        self.CusCaddr_3.setObjectName("CusCaddr_3")
        self.gridLayout_4.addWidget(self.CusCaddr_3, 9, 0, 1, 2)
        self.CusAddress_3 = QtWidgets.QLineEdit(self.dele)
        self.CusAddress_3.setObjectName("CusAddress_3")
        self.gridLayout_4.addWidget(self.CusAddress_3, 5, 0, 1, 2)
        self.CusCphone_3 = QtWidgets.QLineEdit(self.dele)
        self.CusCphone_3.setObjectName("CusCphone_3")
        self.gridLayout_4.addWidget(self.CusCphone_3, 11, 0, 1, 1)
        self.CusName_3 = QtWidgets.QLineEdit(self.dele)
        self.CusName_3.setObjectName("CusName_3")
        self.gridLayout_4.addWidget(self.CusName_3, 3, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.dele)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.CusID_3 = QtWidgets.QLineEdit(self.dele)
        self.CusID_3.setObjectName("CusID_3")
        self.gridLayout_4.addWidget(self.CusID_3, 1, 0, 1, 2)
        self.tabWidget.addTab(self.dele, "")
        self.change = QtWidgets.QWidget()
        self.change.setObjectName("change")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.change)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_38 = QtWidgets.QLabel(self.change)
        self.label_38.setObjectName("label_38")
        self.gridLayout_5.addWidget(self.label_38, 0, 0, 1, 1)
        self.CusID_4 = QtWidgets.QLineEdit(self.change)
        self.CusID_4.setObjectName("CusID_4")
        self.gridLayout_5.addWidget(self.CusID_4, 1, 0, 1, 2)
        self.label_32 = QtWidgets.QLabel(self.change)
        self.label_32.setObjectName("label_32")
        self.gridLayout_5.addWidget(self.label_32, 2, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.change)
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 2, 1, 1, 1)
        self.CusName_4 = QtWidgets.QLineEdit(self.change)
        self.CusName_4.setObjectName("CusName_4")
        self.gridLayout_5.addWidget(self.CusName_4, 3, 0, 1, 1)
        self.CusPhone_4 = QtWidgets.QLineEdit(self.change)
        self.CusPhone_4.setText("")
        self.CusPhone_4.setObjectName("CusPhone_4")
        self.gridLayout_5.addWidget(self.CusPhone_4, 3, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.change)
        self.label_37.setObjectName("label_37")
        self.gridLayout_5.addWidget(self.label_37, 4, 0, 1, 1)
        self.CusAddress_4 = QtWidgets.QLineEdit(self.change)
        self.CusAddress_4.setObjectName("CusAddress_4")
        self.gridLayout_5.addWidget(self.CusAddress_4, 5, 0, 1, 2)
        self.label_35 = QtWidgets.QLabel(self.change)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 6, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.change)
        self.label_33.setObjectName("label_33")
        self.gridLayout_5.addWidget(self.label_33, 6, 1, 1, 1)
        self.CusCname_4 = QtWidgets.QLineEdit(self.change)
        self.CusCname_4.setObjectName("CusCname_4")
        self.gridLayout_5.addWidget(self.CusCname_4, 7, 0, 1, 1)
        self.CusRela_4 = QtWidgets.QLineEdit(self.change)
        self.CusRela_4.setObjectName("CusRela_4")
        self.gridLayout_5.addWidget(self.CusRela_4, 7, 1, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.change)
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 8, 0, 1, 1)
        self.CusCaddr_4 = QtWidgets.QLineEdit(self.change)
        self.CusCaddr_4.setObjectName("CusCaddr_4")
        self.gridLayout_5.addWidget(self.CusCaddr_4, 9, 0, 1, 2)
        self.label_36 = QtWidgets.QLabel(self.change)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 10, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.change)
        self.label_34.setObjectName("label_34")
        self.gridLayout_5.addWidget(self.label_34, 10, 1, 1, 1)
        self.CusCphone_4 = QtWidgets.QLineEdit(self.change)
        self.CusCphone_4.setObjectName("CusCphone_4")
        self.gridLayout_5.addWidget(self.CusCphone_4, 11, 0, 1, 1)
        self.CusEmployee2_3 = QtWidgets.QLineEdit(self.change)
        self.CusEmployee2_3.setObjectName("CusEmployee2_3")
        self.gridLayout_5.addWidget(self.CusEmployee2_3, 11, 1, 1, 1)
        self.clearButton_4 = QtWidgets.QPushButton(self.change)
        self.clearButton_4.setObjectName("clearButton_4")
        self.gridLayout_5.addWidget(self.clearButton_4, 12, 0, 1, 2)
        self.CusQueryButton_3 = QtWidgets.QPushButton(self.change)
        self.CusQueryButton_3.setDefault(True)
        self.CusQueryButton_3.setObjectName("CusQueryButton_3")
        self.gridLayout_5.addWidget(self.CusQueryButton_3, 13, 0, 1, 2)
        self.tabWidget.addTab(self.change, "")
        self.gridLayout.addWidget(self.tabWidget, 4, 0, 3, 1)
        self.label = QtWidgets.QLabel(customer)
        self.label.setMinimumSize(QtCore.QSize(0, 24))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3, QtCore.Qt.AlignHCenter)
        self.toolButton = QtWidgets.QToolButton(customer)
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 4, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(customer)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setRowCount(28)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 6, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(customer)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 1, 1, 2, QtCore.Qt.AlignHCenter)

        self.retranslateUi(customer)
        self.tabWidget.setCurrentIndex(1)
        self.clearButton.clicked.connect(self.CusAddCaddr.clear)
        self.clearButton.clicked.connect(self.CusAddCphone.copy)
        self.clearButton.clicked.connect(self.CusAddCname.clear)
        self.clearButton.clicked.connect(self.CusAddRela.clear)
        self.clearButton.clicked.connect(self.CusAddAddress.clear)
        self.clearButton.clicked.connect(self.CusAddName.clear)
        self.clearButton.clicked.connect(self.CusAddPhone.clear)
        self.clearButton.clicked.connect(self.CusAddID.clear)
        self.clearButton_2.clicked.connect(self.CusCaddr_2.clear)
        self.clearButton_2.clicked.connect(self.CusCphone_2.clear)
        self.clearButton_2.clicked.connect(self.CusRela_2.clear)
        self.clearButton_2.clicked.connect(self.CusCname_2.clear)
        self.clearButton_2.clicked.connect(self.CusAddress_2.clear)
        self.clearButton_2.clicked.connect(self.CusName_2.clear)
        self.clearButton_2.clicked.connect(self.CusID_2.clear)
        self.clearButton_2.clicked.connect(self.CusPhone_2.clear)
        self.clearButton_3.clicked.connect(self.CusCphone_3.clear)
        self.clearButton_3.clicked.connect(self.CusCaddr_3.clear)
        self.clearButton_3.clicked.connect(self.CusCname_3.clear)
        self.clearButton_3.clicked.connect(self.CusRela_3.clear)
        self.clearButton_3.clicked.connect(self.CusAddress_3.clear)
        self.clearButton_3.clicked.connect(self.CusName_3.clear)
        self.clearButton_3.clicked.connect(self.CusPhone_3.clear)
        self.clearButton_3.clicked.connect(self.CusID_3.clear)
        self.clearButton_3.clicked.connect(self.CusEmployee2_2.clear)
        self.clearButton_4.clicked.connect(self.CusCphone_4.clear)
        self.clearButton_4.clicked.connect(self.CusEmployee2_3.clear)
        self.clearButton_4.clicked.connect(self.CusCaddr_4.clear)
        self.clearButton_4.clicked.connect(self.CusCname_4.clear)
        self.clearButton_4.clicked.connect(self.CusRela_4.clear)
        self.clearButton_4.clicked.connect(self.CusAddress_4.clear)
        self.clearButton_4.clicked.connect(self.CusPhone_4.clear)
        self.clearButton_4.clicked.connect(self.CusName_4.clear)
        self.clearButton_4.clicked.connect(self.CusID_4.clear)
        self.clearButton_2.clicked.connect(self.CusEmployee2.clear)
        QtCore.QMetaObject.connectSlotsByName(customer)

    def retranslateUi(self, customer):
        _translate = QtCore.QCoreApplication.translate
        customer.setWindowTitle(_translate("customer", "Form"))
        self.label_10.setText(_translate("customer", "???????????????"))
        self.label_3.setText(_translate("customer", "?????????"))
        self.label_7.setText(_translate("customer", "???????????????"))
        self.label_5.setText(_translate("customer", "?????????"))
        self.label_9.setText(_translate("customer", "?????????????????????"))
        self.label_6.setText(_translate("customer", "??????"))
        self.customerAdd.setText(_translate("customer", "Confirm"))
        self.label_8.setText(_translate("customer", "???????????????"))
        self.label_19.setText(_translate("customer", "????????????"))
        self.label_4.setText(_translate("customer", "??????"))
        self.clearButton.setText(_translate("customer", "Clear"))
        self.CusEmployee.setCurrentText(_translate("customer", "12346"))
        self.CusEmployee.setItemText(0, _translate("customer", "12346"))
        self.CusEmployee.setItemText(1, _translate("customer", "12347"))
        self.CusEmployee.setItemText(2, _translate("customer", "12348"))
        self.CusEmployee.setItemText(3, _translate("customer", "12349"))
        self.CusEmployee.setItemText(4, _translate("customer", "12350"))
        self.CusEmployee.setItemText(5, _translate("customer", "12351"))
        self.CusEmployee.setItemText(6, _translate("customer", "18349"))
        self.CusEmployee.setItemText(7, _translate("customer", "18350"))
        self.CusEmployee.setItemText(8, _translate("customer", "18351"))
        self.CusEmployee.setItemText(9, _translate("customer", "22351"))
        self.CusEmployee.setItemText(10, _translate("customer", "24351"))
        self.CusEmployee.setItemText(11, _translate("customer", "28351"))
        self.CusEmployee.setItemText(12, _translate("customer", "12345"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add), _translate("customer", "??????"))
        self.clearButton_2.setText(_translate("customer", "Clear"))
        self.label_14.setText(_translate("customer", "?????????"))
        self.label_18.setText(_translate("customer", "??????"))
        self.label_12.setText(_translate("customer", "???????????????"))
        self.label_15.setText(_translate("customer", "?????????"))
        self.label_11.setText(_translate("customer", "???????????????"))
        self.label_16.setText(_translate("customer", "??????"))
        self.CusQueryButton.setText(_translate("customer", "Confirm"))
        self.label_13.setText(_translate("customer", "???????????????"))
        self.label_17.setText(_translate("customer", "?????????????????????"))
        self.label_20.setText(_translate("customer", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.query), _translate("customer", "??????"))
        self.label_23.setText(_translate("customer", "?????????????????????"))
        self.label_28.setText(_translate("customer", "??????"))
        self.label_27.setText(_translate("customer", "???????????????"))
        self.CusDelButton.setText(_translate("customer", "Delete"))
        self.label_29.setText(_translate("customer", "???????????????"))
        self.label_26.setText(_translate("customer", "????????????"))
        self.label_21.setText(_translate("customer", "???????????????"))
        self.label_25.setText(_translate("customer", "?????????"))
        self.label_22.setText(_translate("customer", "??????"))
        self.clearButton_3.setText(_translate("customer", "Clear"))
        self.label_24.setText(_translate("customer", "?????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dele), _translate("customer", "??????"))
        self.label_38.setText(_translate("customer", "?????????"))
        self.label_32.setText(_translate("customer", "??????"))
        self.label_30.setText(_translate("customer", "?????????"))
        self.label_37.setText(_translate("customer", "??????"))
        self.label_35.setText(_translate("customer", "???????????????"))
        self.label_33.setText(_translate("customer", "???????????????"))
        self.label_31.setText(_translate("customer", "?????????????????????"))
        self.label_36.setText(_translate("customer", "???????????????"))
        self.label_34.setText(_translate("customer", "????????????"))
        self.clearButton_4.setText(_translate("customer", "Clear"))
        self.CusQueryButton_3.setText(_translate("customer", "Confirm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change), _translate("customer", "??????"))
        self.label.setText(_translate("customer", "Customer Management"))
        self.toolButton.setText(_translate("customer", "..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("customer", "?????????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("customer", "??????"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("customer", "?????????"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("customer", "??????"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("customer", "???????????????"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("customer", "???????????????"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("customer", "???????????????"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("customer", "???????????????"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("customer", "??????id"))
        self.label_2.setText(_translate("customer", "?????????"))
