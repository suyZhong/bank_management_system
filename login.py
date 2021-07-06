from PyQt5.QtWidgets import QDialog, QMessageBox
from sqlalchemy.orm import sessionmaker
import db
from UI.login_form import Ui_login_form
from sqlalchemy.exc import OperationalError
from window import MainWindow

class LoginDiag(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_form()
        self.ui.setupUi(self)
        self.text = ''
        self.ui.pushButton.clicked.connect(self.login)
        self.window = MainWindow()

    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()
        host = self.ui.host.text()
        port = self.ui.port.text()
        dbname = self.ui.dbname.text()
        try:
            engine = db.login(username, password, host, port, dbname)
            session = sessionmaker(engine)()
            item = session.query(db.Bank).all()
        except OperationalError:
            engine = None
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Your account is wrong')
            msgBox.exec_()
            return
        except ValueError:
            engine = None
            msgBox = QMessageBox(QMessageBox.Warning, 'Error', 'Your input is wrong')
            msgBox.exec_()
            return

        print("asd")
        self.window.engine = engine
        self.window.customer.engine = engine
        self.window.accountant.engine = engine
        self.window.loans.engine = engine
        self.window.show()
        self.close()

