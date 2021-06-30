import sqlalchemy as sql
from configs.db_config import DB_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint


def login(username: str, password: str, host: str, port: int, dbName: str):
    DB_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbName}'
    return sql.create_engine(DB_URL)


engine = sql.create_engine(DB_URL)

baseClass = declarative_base(engine)


class Bank(baseClass):
    __tablename__ = 'bank'
    name = sql.Column(sql.String(50), primary_key=True)
    city = sql.Column(sql.String(50))
    possession = sql.Column(sql.Float, default=0.0)


class Customer(baseClass):
    __tablename__ = 'customer'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    contact_name = sql.Column(sql.String(50))
    contact_phone = sql.Column(sql.String(12))
    contact_email = sql.Column(sql.String(256))
    contact_relation = sql.Column(sql.String(20))

    empl_id = sql.Column(sql.SmallInteger, sql.ForeignKey('Employee.id'))


class Department(baseClass):
    __tablename__ = 'department'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    name = sql.Column(sql.String(50))
    manager_id = sql.Column(sql.SmallInteger)
    type = sql.Column(sql.String(20))

    bank_name = sql.Column(sql.String(50), sql.ForeignKey("bank.name"))


class Employee(baseClass):
    __tablename__ = 'employee'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    begin_date = sql.Column(sql.Date)

    bank_name = sql.Column(sql.String(50), sql.ForeignKey('Bank.name'))
    depart_id = sql.Column(sql.SmallInteger, sql.ForeignKey('Department.id'))


class Account(baseClass):
    __tablename__ = 'account'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)


class SaveAccount(baseClass):
    __tablename__ = 'save_account'
    id = sql.Column(sql.SmallInteger, sql.ForeignKey('Account.id'), primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)
    rate = sql.Column(sql.String(10))
    money_type = sql.Column(sql.String(10))
    bank_name = sql.Column(sql.String(50), sql.ForeignKey("Bank.name"), onupdate="CASCADE")


class CustomerToCA(baseClass):
    __tablename__ = 'customer_to_ca'
    last_access_date = sql.Column(sql.Date)
    ca_id = sql.Column(sql.SmallInteger, sql.ForeignKey('check_account.id'),primary_key=True)
    cus_id = sql.Column(sql.SmallInteger, sql.ForeignKey("customer.id"),primary_key=True)
    bank_name = sql.Column(sql.String(50),sql.ForeignKey('bank.name'))

class CustomerToSA(baseClass):
    __tablename__ = 'customer_to_sa'
    last_access_date = sql.Column(sql.Date)
    sa_id = sql.Column(sql.SmallInteger, sql.ForeignKey('save_account.id'), primary_key=True)
    cus_id = sql.Column(sql.SmallInteger, sql.ForeignKey("customer.id"), primary_key=True)
    bank_name = sql.Column(sql.String(50),sql.ForeignKey('bank.name'))

class CheckAccount(baseClass):
    __tablename__ = 'check_account'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)
    extra = sql.Column(sql.Float)
    bank_name = sql.Column(sql.String(50), sql.ForeignKey("Bank.name"), onupdate="CASCADE")


class CustomerToLoan(baseClass):
    __tablename__ = 'customer_to_loan'
    cus_id = sql.Column(sql.SmallInteger, sql.ForeignKey("customer.id"),primary_key=True)
    loan_id = sql.Column(sql.SmallInteger, sql.ForeignKey('loan.id'),primary_key=True)



class Loan(baseClass):
    __tablename__ = 'loan'
    id = sql.Column(sql.SmallInteger, primary_key=True)
    money = sql.Column(sql.Float)

    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))

class Pay(baseClass):
    __tablename__ = 'pay'
    id = sql.Column(sql.String(50), primary_key=True)
    date = sql.Column(sql.Date)
    money = sql.Column(sql.Float)

    loan_id = sql.Column(sql.SmallInteger, sql.ForeignKey('Loan.id'))


baseClass.metadata.clear()
baseClass.metadata.create_all()

if __name__ == '__main__':
    engine = login('root', 'zsy123', 'localhost', '3306', 'bank_system')
    DBsession = sessionmaker(engine)
    session = DBsession()
    session.add(Bank(name="zhong guo ren min bsu hang", city="hefias", possession=1.5))
    session.commit()
    session.close()
