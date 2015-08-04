#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nick'

import sys

# sys.stdout.write('Введите ваше имя\n')
# if len(sys.argv) != 2:
#     print 'Введите ваше имя\n'
# name = sys.stdin.readline()
print sys.argv
# print dir(name)


def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start

@coroutine
def receiver():
    print('Готов к приему значений')
    while True:
        n = (yield)
        print('Получено %s' % n)

r = receiver()
r.send('Hello World')