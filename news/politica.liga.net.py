#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'

from sqlalchemy import *
from xml.etree import ElementTree
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import unicodedata
import time
from urllib import urlopen, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer
import re

URL = 'http://news.liga.net'
URL_finence = 'http://finance.liga.net/'
links = {'politica':'all/politics/', 'economika':'all/economics/', 'world':'all/world/', 'proishestviya':'all/incident/', 'sport':'all/sport/', 'culture':'all/culture/','obhestvo':'all/society/'}
# http://news.liga.net/


metadata = MetaData()

def db_connect(name='root', passw = 'root', host = 'localhost', db = '2shans_local'):
    mysql = "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()

"""
    lige.net news table
"""
news_info = Table('news_info', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('text_ru', Text),
                  Column('text_ua', Text),
                  Column('text_en', Text),
                  Column('poster', CHAR(100)),
                  Column('date_create', TIMESTAMP, default=int(time.time())),
                  Column('description_ua', Text),
                  Column('description_ru', Text),
                  Column('description_en', Text),
                  Column('description_en', Text),
                  Column('genre_id', Integer),
                  Column('links_parse', CHAR(200)),)

class News_info(object):
    __tablename__ = 'news_info'
    id = Column(Integer, primary_key=True)
    date_create = Column(TIMESTAMP, default=int(time.time()))

    def __init__(self, text_ru, text_ua, text_en, poster, date_create, description_ua, description_ru, description_en, genre_id, links_parse):
        self.text_ru = text_ru
        self.text_ua = text_ua
        self.text_en = text_en
        self.poster = poster
        self.date_create = date_create
        self.description_ua = description_ua
        self.description_ru = description_ru
        self.description_en = description_en
        self.genre_id = genre_id
        self.links_parse = links_parse

    def __repr__(self):
        return "<News_info('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')>" % (self.text_ru, self.text_ua, self.text_en, self.poster, self.description_ua, self.description_en,self.description_ru, self.date_create, self.genre_id, self.subgenre_id)

mapper(News_info, news_info)

"""
end table
"""

def parse_news_link(link):
    return "%s/%s" % (URL, link)

def get_html(url):
    response = urlopen(url)
    return response.read()

e = db_connect()
def main():
    contents_links = []
    # """
    for i in BeautifulSoup(urlopen(parse_news_link(links['politica']))).findAll('div', { "class" : "last_news_list" }):
        for ii in i.findAll('ul', {'class': "ul"}):
            for iii in ii.findAll('li'):
                for iiii in iii.findAll('div', {'class': "title"}):
                    news = SoupStrainer('a', href=re.compile('/news/'))
                    for iiiii in iiii.findAll('a', href=re.compile('/news/')):
                        contents_links.append(iiiii['href'])

    img = []
    contents = []
    descriptions = []
    for i in contents_links:
        for ii in BeautifulSoup(urlopen(URL + i)).findAll('div', {"class": "news_detail"}):
            print ii.h1.string
            descriptions.append(ii.h1.string)
            for iii in ii.findAll('div', {"class": "img"}):
                # print iii.div.img['src']
                img.append(iii.div.img['src'])

            for d in ii.findAll('div', {"class": "text _ga1_on_"}):
                contents.append((str(d)))

    for i, p in enumerate(descriptions):
        urll = (URL)+img[i].encode('utf-8')

        liga_net_contents = News_info(contents[i], contents[i], contents[i], urll, int(time.time()), descriptions[i], descriptions[i], descriptions[i], 1, 'liga.net')
        Session = sessionmaker(bind=e)
        session = Session()
        session.add(liga_net_contents)
        session.commit()
    # """

if __name__ == '__main__':
    main()