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

def db_connect(name='root', passw = 'root', host = 'localhost', db = 'real estate'):
    mysql = "mysql+pymysql://%s:%s@%s/%s" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

"""
Tests table
"""
person = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False),Column('date_create', DateTime, default=datetime.now()))

class Person(object):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    date_create = Column(DateTime, default=datetime.now())

    def __init__(self, name, date_create):
        # self.id             = id
        self.name           = name
        self.date_create    = date_create

    def __repr__(self):
        return "<Person('%s','%s')>" % ( self.name, self.date_create)

mapper(Person, person)

"""
end table
"""

"""
класс Недвижимости
"""
mt = MetaData()

estate = Table('estate', mt, Column('id', Integer, primary_key=True),
                                    Column('city', VARCHAR(255), default=null),
                                    Column('area', VARCHAR(255), default=null),
                                    Column('street', VARCHAR(255), default=null),
                                    Column('home', VARCHAR(255), default=null),
                                    Column('storey', SmallInteger(), default=null),
                                    Column('link', VARCHAR(255), default=null),
                                    Column('yardage', Integer(), default=null),
                                    Column('state_object', Text(), default=null),
                                    Column('date_placement', Integer(), default=null),
                                    Column('date_parsing', Integer(), default=null),
                                    Column('price', Integer(), default=null),
                                    Column('currency', VARCHAR(4), default=null),
)

class Estate(object):
    __tablename__ = 'estate'
    id = Column(Integer, primary_key=True)
    def __init__(self, city, area, street, home, storey, link, yardage, state_object, comment, date_placement, date_parsing, price, currency):
        # self.id             = id
        self.city           = city
        self.area           = area
        self.street         = street
        self.home           = home
        self.storey           = storey
        self.link           = link
        self.yardage        = yardage
        self.state_object   = state_object
        self.comment        = comment
        self.date_placement = date_placement
        self.date_parsing   = date_parsing
        self.price          = price
        self.currency       = currency

    def __repr__(self):
        return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Estate, estate)

"""
end Estate class
"""

# e = db_connect()

# print table.select().limit(1)
# print e.execute(table.select().limit(1), name='NickTaporuk')
# metadata.create_all(e)

# Session = sessionmaker(bind=e)
# session = Session()
# person = Person(name='Tests')
# session.add(Person('Tests1', datetime.now()))
# session.add(Estate('Tests1', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
# print session.new
# session.commit()
# print datetime.now()


def main():
    e = db_connect()
    # print table.select().limit(1)
    # print e.execute(table.select().limit(1), name='NickTaporuk')
    # metadata.create_all(e)

    Session = sessionmaker(bind=e)
    session = Session()
    # person = Person(name='Tests')
    session.add(Person('Tests33333333333', datetime.now()))
    session.add(Estate('Tests33333333333', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
    # print session.new
    session.commit()

if __name__ == '__main__':
    main()

# main()