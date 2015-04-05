#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'


from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
from datetime import datetime

def db_connect(name='root', passw = 'root', host = 'localhost', db = 'real estate'):
    mysql = "mysql+pymysql://%s:%s@%s/%s" % (name, passw, host, db)
    return create_engine(mysql, echo=True).connect()

metadata = MetaData()
# table = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False))
Base = declarative_base()


# class Person(object):
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    date_create = Column(DateTime, nullable=False)

    # __mapper_args__ = {
    #                 'version_id_col': timestamp,
    #                 'version_id_generator': lambda v:datetime.now()
    #             }
    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name
    #
    # def __repr__(self):
    #     return "<Person('%s','%s')>" % (self.id, self.name)

e = db_connect()

print Person.__mapper__

metadata.create_all(e)

person = Person()
print person.select()
# Session = sessionmaker(bind=e)
# session = Session()
# person = Person(name='NickTaporuk',date_create=datetime.now())
# session.add(person)
# print session.new
# session.flush()
# print mapper(Person, table)
