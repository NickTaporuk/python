#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'
# Устанавливаем стандартную внешнюю кодировку = utf8
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
from urllib import urlopen, urlretrieve
from BeautifulSoup import BeautifulSoup, SoupStrainer
# from sqlalchemy import *
import re
import dataSqlAlchemy as db

URL = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=0&roomCount=1'
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
    obj_right   = []
    obj_left    = []
    area        = []
    yardage     = []#метраж
    c = 0
    link = SoupStrainer('div')
    for i in BeautifulSoup(get_html(url), parseOnlyThese=link).findAll('div', { "class" : "obj" }):
        # return i['class']
        # s2 = u''.join(unichr(ord(c)) for c in s)
        for ii in i.findAll('div', {'class': "obj-right"}):
            """
            валюта,цена
            """
            v = ii.span
            obj_right.append([v.string[v.string.find('$')], v.string.replace('$','')])# obj_right

        for ii in i.findAll('div', {'class': "obj-left"}):
            """
            улица
            """
            print ii.h3.a.string
            # strok = ii.h3.a.contents[0]
            # if ii.h3.a.string is not None:
                # obj_left.append(ii.h3.a.string.split(','))
            # if ii.h3.a.string:
            try:
                obj_left.append(ii.h3.a.string.split(','))
            except:
                # print "Ой!  Это некорректное число.  Попробуйте ещё раз..."
                obj_left.append([0, 0])
                continue
            for iii in ii.findAll('div', {'class': "obj-locality"}):
                """
                район
                """
                if iii.string != None:
                    area.append(iii.string)
                else:
                    area.append(iii.contents[0])
            # obj-params
            for wrap in ii.findAll('div', {'class':'obj-params'}):
                str = re.search('(\d)?\d(\.\d)?\s',wrap.div.contents[2])
                # print wrap.div.contents[2]
                # print str.group(0)
                yardage.append(str.group(0))
    # return len(area)
    all = zip(obj_right, obj_left, area, yardage)
    return all
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
    # a = ['ущшпрцуп','ущамоуцша']
    # print a[0]
    # print u'ущшпрцуп'
    t = get_lun_article()
    # urlretrieve('http://lunimg.appspot.com/lun_ua/104/104/150109845.jpg','test.jpg')
    # db.main()
    # for tt in t[0]:
        # if initer
        # str.join(',', tt)
    # print len(t[0][0])
    # print str
    # set_data_to_file('article.txt',get_lun_article())
    # set_data_to_file('article.txt', t[0][1])
    # pass


if __name__ == '__main__':
    main()
