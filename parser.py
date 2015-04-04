#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'
from urllib import urlopen
from BeautifulSoup import BeautifulSoup, SoupStrainer
import sys, time, os
from sqlalchemy import create_engine


# URL = 'http://weblancer.net'
# URL = 'http://github.com'
URL = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?page=50&roomCount=1&roomCount=2'

#
# mysql connection
#
def db_connect(name='root'):
     return create_engine("mysql+pymysql://root:root@localhost/yii2")

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
def get_pagination():
    link = SoupStrainer('div')
    soup = BeautifulSoup(get_html(URL), parseOnlyThese=link)
    s = soup.findAll('div', {"class": "paginator"})
    active = 0
    for i in s:
        ii = i.findAll('li',{'class':'active'})
        for tag in ii:
            # print ii
            try:
                if active < tag.span.string:
                    active = int(tag.span.string)+1
            except:
                active = 0
    return active

def set_data_to_file(name, string):
    infile = open(name, 'w')
    infile.write(str(string))


def main():
    # infile = open('test.txt', 'w')
    # infile.write(get_html(URL))
    set_data_to_file('pagination.txt', get_pagination())
    # set_data_to_file('html.txt', get_test())
    print get_pagination()
if __name__ == '__main__':
    main()