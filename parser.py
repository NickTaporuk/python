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
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
URL = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=2&roomCount=1&roomCount=2'
MAX_PAGE = 100
"""
mysql connection
"""
def db_connect(name='root', passw = 'root', host = 'localhost', db = 'real estate'):
    mysql = "mysql+pymysql://%s:%s@%s/%s" % (name, passw, host, db)
    return create_engine(mysql, echo=False).connect()
"""

"""
def get_html(url):
    response = urlopen(url)
    return response.read()
"""

"""
def get_lun_article(url =URL):
    obj_right = []
    obj_left = []
    c = 0
    link = SoupStrainer('div')
    for i in BeautifulSoup(get_html(url), parseOnlyThese=link).findAll('div', { "class" : "obj" }):
        # return i['class']

        for ii in i.findAll('div', {'class': "obj-right"}):
            v = ii.span
            obj_right.append([v.string[v.string.find('$')], v.string.replace('$','')])# obj_right

        for ii in i.findAll('div', {'class': "obj-left"}):
            v = ii.h3
            print v
            # obj_left.append([v.string[v.string.find('$')], v.string.replace('$','')])# obj_right

            #  obj = {ii.span.string.find('$')} # currency
    # return soup.findAll('div', { "class" : "obj" })
    # return len(obj_right)
    return obj_right
"""
lun.ua get pagination
"""

def get_pagination(page = 1,url = URL):
    link = SoupStrainer('div')
    active = 0
    for i in BeautifulSoup(get_html(url), parseOnlyThese=link).findAll('div', {"class": "paginator"}):
        ii = i.findAll('li', {'class': 'active'})
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
def get_url_lun(page = 0, roomCountry = 1):
    URL     = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=2&roomCount=1&roomCount=2'
    base    = 'http://www.lun.ua/'
    route   = '%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2'
    query   = '%s%s?page=%s&roomCount=%s' % (base, route, page, roomCountry)
    return query
    # pass


def set_data_to_file(name, string, action = 'w'):
    infile = open(name, action)#дозапись - a,запись-w...
    infile.write(str(string))
#
#
#
def main():
    # set_data_to_file('pagination.txt', get_pagination())
    # set_data_to_file('html.txt', get_lun_article(get_url_lun(5,2)))
    # print get_url_lun()
    # print get_pagination(1)
    # print table.columns
    set_data_to_file('article.txt',get_lun_article())
    # pass

if __name__ == '__main__':
    main()
