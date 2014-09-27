#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib2
import simplejson

url = 'http://geocode-maps.yandex.ru/1.x/?format=json&geocode=Sultanahmet+Camii+%C4%B0%C3%A7+Yollar%C4%B1&lang=en-US'

if __name__ == "__main__":
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    json = simplejson.load(f)
    # print json
for v in json:
    print v.get("format")