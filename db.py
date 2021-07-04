import sqlalchemy as sql
from configs.db_config import DB_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship


def initInsertion(engine):
    session = sessionmaker(engine)()
    session.add(Bank(name='Tiger bank', city='tiger', possession=1e25))
    session.add(Bank(name='Lion bank', city='lion', possession=2e13))
    session.add(Bank(name='Doggy bank', city='dog', possession=2500))
    session.add(Bank(name='Eagle bank', city='eagle', possession=3e14))
    session.add(Department(id='1234321', name='Face', manager_id='114514', bank_name='Tiger bank'))
    session.add(Department(id='1234322', name='Nose', manager_id='114514', bank_name='Tiger bank'))
    session.add(Department(id='1234323', name='Mouth', manager_id='114514', bank_name='Tiger bank'))
    session.add(Department(id='1234324', name='Teeth', manager_id='114514', bank_name='Tiger bank'))
    session.add(Department(id='1333321', name='Face', manager_id='114514', bank_name='Lion bank'))
    session.add(Department(id='1333322', name='Nose', manager_id='114514', bank_name='Lion bank'))
    session.add(Department(id='1333323', name='Mouth', manager_id='114514', bank_name='Lion bank'))
    session.add(Department(id='1333324', name='Teeth', manager_id='114514', bank_name='Lion bank'))
    session.add(Department(id='1444321', name='Face', manager_id='114514', bank_name='Doggy bank'))
    session.add(Department(id='1444322', name='Nose', manager_id='114514', bank_name='Doggy bank'))
    session.add(Department(id='1444323', name='Mouth', manager_id='114514', bank_name='Doggy bank'))
    session.add(Department(id='1444324', name='Teeth', manager_id='114514', bank_name='Doggy bank'))
    session.add(Department(id='5551321', name='Face', manager_id='114514', bank_name='Eagle bank'))
    session.add(Department(id='5551322', name='Nose', manager_id='114514', bank_name='Eagle bank'))
    session.add(Department(id='5551323', name='Mouth', manager_id='114514', bank_name='Eagle bank'))
    session.add(Department(id='5551324', name='Teeth', manager_id='114514', bank_name='Eagle bank'))
    session.add(Employee(id='12345', name='White Tiger1', phone='30303023', address='meng jia la',
                begin_date='2020/9/12', bank_name='Tiger bank', depart_id='1234321', type='manager'))
    session.add(Employee(id='12346', name='White Tiger2', phone='30303043', address='meng jia la',
                begin_date='2020/9/12', bank_name='Tiger bank', depart_id='1234322', type='general'))
    session.add(Employee(id='12347', name='White Tiger3', phone='30303054', address='meng jia la',
                begin_date='2020/9/12', bank_name='Tiger bank', depart_id='1234323', type='general'))
    session.add(Employee(id='12348', name='White Tiger4', phone='30303065', address='meng jia la',
                begin_date='2020/9/12', bank_name='Tiger bank', depart_id='1234324', type='general'))

    session.add(Employee(id='12349', name='White Eagle1', phone='30303012', address='America',
                begin_date='2020/9/11', bank_name='Eagle bank', depart_id='1333321', type='manager'))
    session.add(Employee(id='12350', name='White Eagle2', phone='30303034', address='America',
                begin_date='2020/9/11', bank_name='Eagle bank', depart_id='1333322', type='general'))
    session.add(Employee(id='12351', name='White Eagle3', phone='30303354', address='America',
                begin_date='2020/9/11', bank_name='Eagle bank', depart_id='1333323', type='general'))
    session.add(Employee(id='22351', name='White Eagle4', phone='30303354', address='America',
                begin_date='2020/9/11', bank_name='Eagle bank', depart_id='1333324', type='general'))

    session.add(Employee(id='14349', name='White Doggy1', phone='30212312', address='Japan',
                begin_date='2020/8/6', bank_name='Doggy bank', depart_id='1333321', type='manager'))
    session.add(Employee(id='14350', name='White Doggy2', phone='21233034', address='Japan',
                begin_date='2020/8/6', bank_name='Doggy bank', depart_id='1333322', type='general'))
    session.add(Employee(id='14351', name='White Doggy3', phone='21233354', address='Japan',
                begin_date='2020/8/6', bank_name='Doggy bank', depart_id='1333323', type='general'))
    session.add(Employee(id='24351', name='White Doggy4', phone='21233354', address='Japan',
                begin_date='2020/8/6', bank_name='Doggy bank', depart_id='1333324', type='general'))

    session.add(Employee(id='18349', name='White Lion', phone='24303012', address='Waganda',
                begin_date='2020/9/11', bank_name='Lion bank', depart_id='1333321', type='manager'))
    session.add(Employee(id='18350', name='White Lion', phone='24302434', address='Waganda',
                begin_date='2020/9/11', bank_name='Lion bank', depart_id='1333322', type='general'))
    session.add(Employee(id='18351', name='White Lion', phone='24303354', address='Waganda',
                begin_date='2020/9/11', bank_name='Lion bank', depart_id='1333323', type='general'))
    session.add(Employee(id='28351', name='White Lion', phone='24303354', address='Waganda',
                begin_date='2020/9/11', bank_name='Lion bank', depart_id='1333324', type='general'))

    session.commit()
    session.close()

def login(username: str, password: str, host: str, port: int, dbName: str):
    DB_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbName}'
    return sql.create_engine(DB_URL)

def addCustomer(engine ,id, name, phone, address, cname, cphone, cmail, crelation, empl_id):
    session = sessionmaker(engine)()
    if empl_id != '':
        session.add(Customer(id=id, name=name, phone=phone, address=address, contact_name = cname,contact_phone = cphone,contact_email = cmail, contact_relation = crelation, empl_id=empl_id))
    else:
        session.add(Customer(id=id, name=name, phone=phone, address=address, contact_name = cname,contact_phone = cphone,contact_email = cmail, contact_relation = crelation))
    session.commit()
    session.close()

engine = sql.create_engine(DB_URL)

# baseClass = declarative_base(engine)
baseClass = declarative_base()
baseClass.metadata.clear()


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
    type = sql.Column(sql.String(20))

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
    initInsertion(engine)
    session = DBsession()
    # session.add(Bank(name="zhossng guoen min bsu hang", city="hefias"))
    # session.add(Employee(id='1231223', name='null'))
    # data = session.query(Customer).filter(Customer.id.like('%'+'s'+'%')).all()
    # for i in data:
        # print(i.id)
    session.commit()
    session.close()
