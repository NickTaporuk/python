#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'nick'
import time
start = time.clock()
class Parent:
    def __init__(self,data=0):
        self.data = data
    def setdata(self, data):
        self.data = data

    @staticmethod
    def show(cls):
        print cls.data

class Child(Parent):
    def show(self):
        print self

p = Parent(1111)
p.setdata(12)
# p.show()

end = time.clock()

print (end - start)