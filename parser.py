#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'
from urllib import urlopen
from BeautifulSoup import BeautifulSoup, SoupStrainer
import sys, time, os
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

URL = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=2&roomCount=1&roomCount=2'
MAX_PAGE = 100
#
# mysql connection
#
def db_connect(name='root', passw = 'root', host = 'localhost', db = 'real estate'):
    mysql = "mysql+pymysql://%s:%s@%s/%s" % (name, passw, host, db)
    return create_engine(mysql, echo=True).connect()

def get_html(url):
    response = urlopen(url)
    return response.read()
    # pass

def get_test():
    links = SoupStrainer('div')
    soup = BeautifulSoup(get_html(URL), parseOnlyThese=links)
    return soup.findAll('div', { "class" : "obj" })
#
# lun.ua get pagination
#
def get_pagination(page = 1):
    link = SoupStrainer('div')
    active = 0
    for i in BeautifulSoup(get_html(URL), parseOnlyThese=link).findAll('div', {"class": "paginator"}):
        ii = i.findAll('li',{'class':'active'})
        for tag in ii:
            # print ii
            try:
                if active < tag.span.string:
                    active = int(tag.span.string)+page
            except:
                active = 0
    return active
#
#
#
def get_plain_lun():
    pass

#
#
#
def get_url_lun(page = 0, roomCountry = 1):
    URL     = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=2&roomCount=1&roomCount=2'
    base    = 'http://www.lun.ua/'
    route   = '%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2'
    query   = '%s%s?page=%s&roomCount=%s' % (base, route, page, roomCountry)
    return query
    # pass


def set_data_to_file(name, string):
    # infile = open(name, 'w') #запись в файл
    infile = open(name, 'a')
    infile.write(str(string))

class Person(Base):
    __table_name__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

def main():
    # infile = open('test.txt', 'w')
    # infile.write(get_html(URL))
    # set_data_to_file('pagination.txt', get_pagination())
    # set_data_to_file('html.txt', get_test())
    # print get_pagination(1)
    # print table.columns
    # print metadata.tables
    # metadata.create_all(e)

    # print table.insert()
    # result = e.execute('SELECT * FROM `real estate`.estate')
    # print result.scalar()
    # for row in result:
    #     print dict(row)
    # print get_html(get_url_lun(2, 3))
    # pass
    metadata = MetaData()
    # table = Table('person', metadata, Column('id', Integer, primary_key=True), Column('name', String(25), nullable=False))
    # e = db_connect()
    # table.insert()
    # print table.select().limit(1)
    # print table.select().order_by(table.columns.name)
    # e.execute(table.insert(),name='NickTaporuk')
    Base = declarative_base(metadata=metadata)
    # print Base
    print Person(Base)

if __name__ == '__main__':
    main()

class Estate(object):
    def __init__(self, id, city, area, street, home, storey, link, yardage, state_object, comment, date_placement, date_parsing, price, currency):
        self.id             = id
        self.city           = city
        self.area           = area
        self.street         = street
        self.home           = home
        self.storey         = storey
        self.link           = link
        self.yardage        = yardage
        self.state_object   = state_object
        self.comment        = comment
        self.date_placement = date_placement
        self.date_parsing   = date_parsing
        self.price          = price
        self.currency       = currency

    def __repr__(self):
        return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.id, self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)
