# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.setEnabled(True)
        login_form.resize(532, 315)
        login_form.setSizeGripEnabled(False)
        login_form.setModal(False)
        self.gridLayout = QtWidgets.QGridLayout(login_form)
        self.gridLayout.setObjectName("gridLayout")
        self.dbname = QtWidgets.QLineEdit(login_form)
        self.dbname.setObjectName("dbname")
        self.gridLayout.addWidget(self.dbname, 4, 1, 1, 1)
        self.username = QtWidgets.QLineEdit(login_form)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(login_form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(login_form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.host = QtWidgets.QLineEdit(login_form)
        self.host.setPlaceholderText("")
        self.host.setObjectName("host")
        self.gridLayout.addWidget(self.host, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(login_form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.port = QtWidgets.QLineEdit(login_form)
        self.port.setObjectName("port")
        self.gridLayout.addWidget(self.port, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(login_form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(login_form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(login_form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(login_form)
        self.password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.password.setInputMask("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 1)
        self.pushButton.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.dbname.raise_()
        self.port.raise_()
        self.host.raise_()
        self.password.raise_()
        self.username.raise_()

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "??????????????????????????????"))
        self.dbname.setText(_translate("login_form", "bank_system"))
        self.username.setText(_translate("login_form", "root"))
        self.pushButton.setText(_translate("login_form", "??????"))
        self.label_5.setText(_translate("login_form", "database"))
        self.host.setText(_translate("login_form", "localhost"))
        self.label_2.setText(_translate("login_form", "password"))
        self.port.setText(_translate("login_form", "3306"))
        self.label_3.setText(_translate("login_form", "host???"))
        self.label.setText(_translate("login_form", "username???"))
        self.label_4.setText(_translate("login_form", "port"))
        self.password.setText(_translate("login_form", "zsy123"))
