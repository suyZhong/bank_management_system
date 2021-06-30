import sqlalchemy as sql
from configs.db_config import DB_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def login(username: str, password: str, host: str, port: int, dbName: str):
    DB_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbName}'
    return sql.create_engine(DB_URL)


engine = sql.create_engine(DB_URL)

baseClass = declarative_base()


class Bank(baseClass):
    __tablename__ = 'bank'
    name = sql.Column(sql.String(50), primary_key=True)
    city = sql.Column(sql.String(50))
    possession = sql.Column(sql.Float, default=0.0)


class Customer(baseClass):
    __tablename__ = 'customer'
    id = sql.Column(sql.String(16), primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    contact_name = sql.Column(sql.String(50))
    contact_phone = sql.Column(sql.String(12))
    contact_email = sql.Column(sql.String(256))
    contact_relation = sql.Column(sql.String(20))


class Department(baseClass):
    __tablename__ = 'department'
    id = sql.Column(sql.String(16), primary_key=True)
    name = sql.Column(sql.String(50))
    type = sql.Column(sql.String(20))


class Employee(baseClass):
    __tablename__ = 'employee'
    id = sql.Column(sql.String(16), primary_key=True)
    name = sql.Column(sql.String(50))
    phone = sql.Column(sql.String(12))
    address = sql.Column(sql.String(50))
    begin_date = sql.Column(sql.Date)


class Account(baseClass):
    __tablename__ = 'account'
    id = sql.Column(sql.String(16), primary_key=True)
    rest = sql.Column(sql.Float)
    date = sql.Column(sql.Date)


class SaveAccount(Account):
    rate = sql.Column(sql.String(10))
    money_type = sql.Column(sql.String(10))


class CheckAccount(Account):
    extra = sql.Column(sql.Float)




# baseClass.metadata.create_all()

if __name__ == '__main__':
    engine = login('root', 'Suyuz230023', 'localhost', '3306', 'bank_system')
    DBsession = sessionmaker(engine)
    session = DBsession()
    session.add(Bank(name="zhong guo ren min bu hang", city="hefi", possession=1.5))
    session.commit()
    session.close()
