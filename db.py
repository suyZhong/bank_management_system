import sqlalchemy as sql
from configs.db_config import DB_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

debug = 0

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


def argStr2None(args: dict):
    for k in args.keys():
        if args[k] == '':
            args[k] = None
    return args


def addLoan(session, id, total_money, bank_name):
    args = locals()
    args = argStr2None(args)
    print(args)
    session.add(Loan(id=args['id'], total_money=args['total_money'], status=0, bank_name=args['bank_name']))



def addCusAccount(session, accType, sa_id, cus_id, bank_name):
    args = locals()
    args = argStr2None(args)
    if accType:
        session.add(CustomerToSA(sa_id=args['sa_id'], cus_id=args['cus_id'], bank_name=args['bank_name']))
    else:
        session.add(CustomerToCA(ca_id=args['sa_id'], cus_id=args['cus_id'], bank_name=args['bank_name']))


def addCustomer(session, id, name, phone, address, cname, cphone, cmail, crelation, empl_id):
    args = locals()
    args = argStr2None(args)
    session.add(Customer(id=args['id'], name=args['name'], phone=args['phone'], address=args['address'],
                         contact_name=args['cname'], contact_phone=cphone,
                         contact_email=args['cmail'], contact_relation=args['crelation'], empl_id=args['empl_id']))


def addAccount(session, accType, id, rest, date, bank_name, rate, money_type, extra):
    args = locals()
    args = argStr2None(args)
    if accType:
        #  is saving
        session.add(SaveAccount(id=args['id'], rest=args['rest'], date=args['date'], bank_name=args['bank_name'],
                                rate=args['rate'], money_type=args['money_type']))
    else:
        session.add(CheckAccount(id=args['id'], rest=args['rest'], date=args['date'], bank_name=args['bank_name'],
                                 extra=args['extra']))


engine = sql.create_engine(DB_URL)

baseClass = declarative_base()
if debug:
    baseClass = declarative_base(engine)
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
    payRel = relationship('CustomerToSA', backref='SaveAccount', passive_deletes=True)


class CustomerToCA(baseClass):
    __tablename__ = 'customer_to_ca'
    last_access_date = sql.Column(sql.Date)
    ca_id = sql.Column(sql.String(25), sql.ForeignKey('check_account.id', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"), primary_key=True)
    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))
    __table_args__ = (UniqueConstraint('cus_id', 'bank_name', name='one_cus_to_ca'),)


class CustomerToSA(baseClass):
    __tablename__ = 'customer_to_sa'
    last_access_date = sql.Column(sql.Date)
    sa_id = sql.Column(sql.String(25), sql.ForeignKey('save_account.id', ondelete="CASCADE",onupdate="CASCADE"), primary_key=True)
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"), primary_key=True)
    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))
    __table_args__ = (UniqueConstraint('cus_id', 'bank_name', name='one_cus_to_sa'),)


class CheckAccount(baseClass):
    __tablename__ = 'check_account'
    id = sql.Column(sql.String(25), primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)
    extra = sql.Column(sql.Float)
    bank_name = sql.Column(sql.String(50), sql.ForeignKey("bank.name"))

    payRel = relationship('CustomerToCA', backref='CheckAccount', passive_deletes=True)


class CustomerToLoan(baseClass):
    __tablename__ = 'customer_to_loan'
    cus_id = sql.Column(sql.String(25), sql.ForeignKey("customer.id"), primary_key=True, onupdate="CASCADE")
    loan_id = sql.Column(sql.String(25), sql.ForeignKey('loan.id', ondelete="CASCADE"), primary_key=True)


class Loan(baseClass):
    __tablename__ = 'loan'
    id = sql.Column(sql.String(25), primary_key=True)
    total_money = sql.Column(sql.Float)
    status = sql.Column(sql.Integer)

    bank_name = sql.Column(sql.String(50), sql.ForeignKey('bank.name'))
    c2l = relationship('CustomerToLoan', backref='loan', passive_deletes=True)
    payRel = relationship('Pay', backref='pay',passive_deletes=True)


class Pay(baseClass):
    __tablename__ = 'pay'
    pid = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    date = sql.Column(sql.Date)
    money = sql.Column(sql.Float)

    cus_id = sql.Column(sql.String(50), sql.ForeignKey('customer.id'))
    loan_id = sql.Column(sql.String(25), sql.ForeignKey('loan.id', ondelete="CASCADE"))


if debug:
    baseClass.metadata.create_all()

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
