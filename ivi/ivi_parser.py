#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'nick'


import dataSqlAlchemy as db
from xml.etree import ElementTree
from sqlalchemy import *
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from datetime import datetime

"""

"""

metadata = MetaData()

def db_connect(name='root', passw = 'root', host = 'localhost', db = 'ivi'):
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

"""
класс Genre
"""
mt = MetaData()

genre = Table('films_genres', mt, Column('id', Integer, primary_key=True),
                                    Column('ivi_id', Integer),
                                    Column('name_rus`', VARCHAR(255), default=null),
                                    Column('category_id', VARCHAR(255), default=null),
                                    Column('genre_link', VARCHAR(255), default=null),)

class Genre(object):
    __tablename__ = 'films_genres'
    id = Column(Integer, primary_key=True)
    def __init__(self, ivi_id, name_rus, category_id, genre_link):
        # self.id             = id
        self.ivi_id           = ivi_id
        self.name_rus         = name_rus
        self.category_id      = category_id
        self.genre_link       = genre_link

    # def __repr__(self):
        # return "<Estate('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.city, self.area, self.street, self.home, self.storey, self.link, self.yardage, self.state_object, self.comment, self.date_placement, self.date_parsing, self.price, self.currency)

mapper(Genre, genre)

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

def insert_genre(data):
    # gs = Genre(data[0], data[1], data[2], data[3])
    # print data[1]
    # for dat in data:
    #     print dat
    e = db_connect()

    # genre.insert(data[0], data[1], data[2], data[3])
    # e.execute()
    Session = sessionmaker(bind=e)
    session = Session()
    session.add(Genre(1, '1', '1', '1'))
    # session.add(Genre(data[0], data[1], data[2], data[3]))
    # session.add(gs)
    session.commit()
    # print session

"""

"""

URL = '/var/www/pythonParser/ivi'
# Жанры
def parse_genres():
    return '%s/genre.xml' % URL

# категории фильмов
def parse_category():
    return '%s/category.xml' % URL

# актёры
def parse_actors():
    return '%s/category.xml' % URL

# films
def parse_films():
    return '%s/category.xml' % URL

def parseIviXml_Category(link):
    with open(link, 'rt') as f:
        """
            Название
            ID
            LINK
        """
        name = []
        id = []
        link = []
        """
            End
        """
        tree = ElementTree.parse(f)
        # root = tree.Element("root")
        for node in tree.iter('title'):
            name.append(node.text)

        for node in tree.iter('id'):
            # print node.tag,node.text, node.attrib
            id.append(node.text)

        for node in tree.iter('hru'):
            # print node.tag,node.text, node.attrib
            link.append(node.text)

        return zip(name, id, link)

def parseIviXml_Genre(link):
    with open(link, 'rt') as f:
        """
            Название
            ID
            LINK
        """
        id = []
        category_id = []
        title = []
        description = []
        hru = []
        """
            End
        """
        tree = ElementTree.parse(f)

        for node in tree.iter('id'):
            # print node.tag,node.text, node.attrib
            id.append(node.text)

        for node in tree.iter('category_id'):
            category_id.append(node.text)

        for node in tree.iter('title'):
            title.append(node.text)

        # for node in tree.iter('description'):
        #     description.append(node.text)

        for node in tree.iter('hru'):
            hru.append(node.text)

        return zip(id, title, category_id, hru)



def main():
    # print 1
    # parseIviXml(parse_genres())
    # category = parseIviXml_Category(parse_category())
    # print category
    gr = parseIviXml_Genre(parse_genres())
    for gnr in gr:
        # print genr
        insert_genre(gnr)
    # print genre
    # pass

if __name__ == '__main__':
    main()