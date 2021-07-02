import sqlalchemy as sql
from configs.db_config import DB_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship


def login(username: str, password: str, host: str, port: int, dbName: str):
    DB_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbName}'
    return sql.create_engine(DB_URL)

def addCustomer(engine ,id, name, phone, address, cname, cphone, cmail, crelation):
    session = sessionmaker(engine)()
    session.add(Customer(id=id, name=name, phone=phone, address=address, contact_name = cname,contact_phone = cphone,contact_email = cmail, contact_relation = crelation))
    session.commit()
    session.close()

engine = sql.create_engine(DB_URL)

baseClass = declarative_base()
# baseClass.metadata.clear()


class Bank(baseClass):
    __tablename__ = 'bank'
    name = sql.Column(sql.String(50), primary_key=True)
    city = sql.Column(sql.String(50))
    possession = sql.Column(sql.Float, default=0.0)

    empls = relationship('Employee')
    sa = relationship('SaveAccount')
    ca = relationship('CheckAccount')



class Customer(baseClass):
    __tablename__ = 'customer'
    id = sql.Column(sql.String(25), primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    contact_name = sql.Column(sql.String(50))
    contact_phone = sql.Column(sql.String(12))
    contact_email = sql.Column(sql.String(256))
    contact_relation = sql.Column(sql.String(20))

    empl_id = sql.Column(sql.String(25), sql.ForeignKey('employee.id'))


class Department(baseClass):
    __tablename__ = 'department'
    id = sql.Column(sql.String(25), primary_key=True)
    name = sql.Column(sql.String(50))
    manager_id = sql.Column(sql.String(25))
    type = sql.Column(sql.String(20))

    bank_name = sql.Column(sql.String(50), sql.ForeignKey("bank.name"))


class Employee(baseClass):
    __tablename__ = 'employee'
    id = sql.Column(sql.String(25), primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    begin_date = sql.Column(sql.Date)

    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))
    depart_id = sql.Column(sql.String(25), sql.ForeignKey('department.id'))
    customers = relationship('Customer')



class SaveAccount(baseClass):
    __tablename__ = 'save_account'
    id = sql.Column(sql.String(25), primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)
    rate = sql.Column(sql.String(10))
    money_type = sql.Column(sql.String(10))
    bank_name = sql.Column(sql.String(50), sql.ForeignKey("bank.name"), onupdate="CASCADE")


class CustomerToCA(baseClass):
    __tablename__ = 'customer_to_ca'
    last_access_date = sql.Column(sql.Date)
    ca_id = sql.Column(sql.String(25), sql.ForeignKey('check_account.id'),primary_key=True)
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"),primary_key=True)
    bank_name = sql.Column(sql.String(50),sql.ForeignKey('bank.name'))

class CustomerToSA(baseClass):
    __tablename__ = 'customer_to_sa'
    last_access_date = sql.Column(sql.Date)
    sa_id = sql.Column(sql.String(25), sql.ForeignKey('save_account.id'), primary_key=True)
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"), primary_key=True)
    bank_name = sql.Column(sql.String(50),sql.ForeignKey('bank.name'))

class CheckAccount(baseClass):
    __tablename__ = 'check_account'
    id = sql.Column(sql.String(25), primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)
    extra = sql.Column(sql.Float)
    bank_name = sql.Column(sql.String(50), sql.ForeignKey("bank.name"), onupdate="CASCADE")


class CustomerToLoan(baseClass):
    __tablename__ = 'customer_to_loan'
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"),primary_key=True)
    loan_id = sql.Column(sql.String(25), sql.ForeignKey('loan.id'),primary_key=True)



class Loan(baseClass):
    __tablename__ = 'loan'
    id = sql.Column(sql.String(25), primary_key=True)
    money = sql.Column(sql.Float)

    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))

class Pay(baseClass):
    __tablename__ = 'pay'
    id = sql.Column(sql.String(50), primary_key=True)
    date = sql.Column(sql.Date)
    money = sql.Column(sql.Float)

    loan_id = sql.Column(sql.String(25), sql.ForeignKey('loan.id'))

# baseClass.metadata.create_all()

if __name__ == '__main__':
    engine = login('root', 'zsy123', 'localhost', '3306', 'bank_system')
    DBsession = sessionmaker(engine)
    session = DBsession()
    # session.add(Bank(name="zhossng guoen min bsu hang", city="hefias"))
    # session.add(Employee(id='1231223', name='null'))
    data = session.query(Customer).filter(Customer.id.like('%'+'s'+'%')).all()
    for i in data:
        print(i.id)
    session.commit()
    session.close()
