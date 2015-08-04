#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nictaporuk@yandex.ru'
__copyright__ = 'Copyright 2015 NickTaporuk'
__version__ = '0.0.1'


class Person:
    def __init__(self, name, age, pay = 0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
    def __str__(self):
        return ('<%s => %s: %s, %s>' % (self.__class__.__name__,  self.name,  self.job,  self.pay))

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, persent):
        self.pay *= (1.0 + persent)

class Manager(Person):
    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')

    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)

if __name__ == '__main__':
    # print 1111
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    sue.giveRaise(.3)
    print bob.lastName(),sue.pay

    tom = Manager(name='Tom Doe', age=50, pay=50000)
    tom.giveRaise(.2)
    print(tom.lastName(), tom.pay)
    print tom
# print __name__