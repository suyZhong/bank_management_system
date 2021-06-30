from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_login_form(object):
    def setupUi(self, login_form):
        login_form.setObjectName("login_form")
        login_form.setEnabled(True)
        login_form.resize(800, 600)
        login_form.setSizeGripEnabled(False)
        login_form.setModal(False)
        self.calendarWidget = QtWidgets.QCalendarWidget(login_form)
        self.calendarWidget.setGeometry(QtCore.QRect(450, 60, 304, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.graphicsView = QtWidgets.QGraphicsView(login_form)
        self.graphicsView.setGeometry(QtCore.QRect(100, 270, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.lcdNumber = QtWidgets.QLCDNumber(login_form)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 312, 171, 151))
        self.lcdNumber.setProperty("intValue", 12)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lineEdit = QtWidgets.QLineEdit(login_form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 140, 113, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(login_form)
        QtCore.QMetaObject.connectSlotsByName(login_form)

    def retranslateUi(self, login_form):
        _translate = QtCore.QCoreApplication.translate
        login_form.setWindowTitle(_translate("login_form", "Dialog"))


def main():
    """
    主函数，用于运行程序
    :return: None
    """
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_login_form()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()