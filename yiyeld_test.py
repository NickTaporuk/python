#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'nick'

def isSimple(x):
    for k in range(2, x/2):
        if x%k == 0:
            return False
        return True

def test():
    yield 1
    yield 4.0
    yield 3.7
    yield u'Hello nick Taporuk'

for k in test():
    print(k, type(k))