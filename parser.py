#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from BeautifulSoup import BeautifulSoup, SoupStrainer
# import sys, time, os

__author__ = 'nick'

# URL = 'http://weblancer.net'
# URL = 'http://github.com'
URL = 'http://www.lun.ua/%D0%BF%D1%80%D0%BE%D0%B4%D0%B0%D0%B6%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D0%B5%D0%B2?roomCount=1&roomCount=2'

def get_html(url):
    response = urlopen(url)
    return response.read()
    # pass

def get_test():
    links = SoupStrainer('div')
    soup = BeautifulSoup(get_html(URL), parseOnlyThese=links)
    return soup.findAll('div', { "class" : "obj" })

def get_pagination():
    link = SoupStrainer('div')
    soup = BeautifulSoup(get_html(URL), parseOnlyThese=link)
    return soup.findAll('div', {"class": "paginator"})

def set_data_to_file(name, string):
    infile = open(name, 'w')
    infile.write(str(string))


def main():
    # print(get_html(URL))
    # infile = open('test.txt', 'w')
    # infile.write(get_html(URL))
    # pass
    # s = get_test()
    # print s
    # set_data_to_file('pagination.txt', get_pagination())
    # set_data_to_file('html.txt', get_test())
    s = get_pagination()
    # print [tag['class'] for tag in s]
    for i in s:
        ii = i.findAll('li')
        for tag in ii:
            for t in tag:
                try:
                    # print str(ii[1].contents)
                    # ii[1].contents
                    # print tag.contents
                    # print t.name
                    if t.name == 'a':
                        print t.string
                    else:
                        print 'None'

                except:
                    print 'bad string'
                    continue

if __name__ == '__main__':
    main()