#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'nick'

def quadratOrCube(x):
    if x<0:
        return lambda x:x*x
    else:
        return lambda x:x*x*x

def oper( L, function):
    result = [function(K) for K in L]
    # for K in L:
    #     result.append(function(K))
    return result

'''Тестовая часть программы'''
x = [1, 2, 34, 45]
print oper(x, quadratOrCube(1))
