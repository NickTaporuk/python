#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'


# import pickle
import shelve
db = []
# ['sue'] = 110
db.append(110)
db.append(111)
db.append(112)
db.append(113)
db.append(114)
# db['sue']['pay'] = 110

# dbfile = open('people-pickle', 'wb')
db = shelve.open('people-shelve')
# pickle.dump(db, dbfile)
db['bob'] = [1234]
db['sue'] = [4321]
db.close()


