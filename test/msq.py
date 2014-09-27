#!/usr/bin/env python
# -*- coding:utf-8 -*-
import math

def discr(a,b,c):
    if isinstance(a, int):
        a=float(a)
    elif not isinstance(a, float):
        raise TypeError()
    try:
        D =b*b-4*a*c
        if D<0:
            return []
        else:
            x1 = (-b+math.sqrt(D))/(2*a)
            x2 = (-b-math.sqrt(D))/(2*a)
            return [x1, x2]
    except ZeroDivisionError:
        x=-c/b
        return [x, None]


def t(x):
    return x**3