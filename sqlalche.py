#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'

from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from datetime import datetime

metadata = MetaData()
table = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False),Column('date_create', DateTime, default=datetime.now()))

def db_connect(name='root', passw = 'root', host = 'localhost', db = 'real estate'):
    mysql = "mysql+pymysql://%s:%s@%s/%s" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

#
#
#
class Person(object):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    date_create = Column(DateTime, default=datetime.now())
    table = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False),Column('date_create', DateTime, default=datetime.now()))


    def __init__(self, name, date_create):
        # self.id             = id
        self.name           = name
        self.date_create    = date_create

    def __repr__(self):
        return "<Person('%s','%s')>" % ( self.name, self.date_create)
e = db_connect()

mapper(Person, table)
# print table.select().limit(1)
# print e.execute(table.select().limit(1), name='NickTaporuk')
# metadata.create_all(e)

Session = sessionmaker(bind=e)
session = Session()
# person = Person(name='Tests')
session.add(Person('Tests1', datetime.now()))
# print session.new
session.commit()
# print datetime.now()