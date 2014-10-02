#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Евклидово расстояние
from recomendations import critics
from math import sqrt, pow

# Возвращает оценку подобия person1 и person2 на основе расстояния
def sim_distance(prefs,person1,person2):
# Получить список предметов, оцененных обоими
#     print(person1)
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
        # print item
            si[item] = 1
        # Если нет ни одной общей оценки, вернуть 0
        if len(si) == 0:
            return 0
        # Сложить квадраты разностей
        sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
            for item in prefs[person1] if item in prefs[person2]])
        return 1/(1+sum_of_squares)

# print u'sim_distance :'
# print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')

# Возвращает коэффициент корреляции Пирсона между p1 и p2
def sim_pearson(prefs, p1, p2):
    # Получить список предметов, оцененных обоими
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
        # Найти число элементов
    n = len(si)
    # Если нет ни одной общей оценки, вернуть 0
    if n == 0:
        return 0
    # Вычислить сумму всех предпочтений
    sum1 = sum([prefs[p1][it] for it in si])
    print sum1
    sum2 = sum([prefs[p2][it] for it in si])
    print sum2
    # Вычислить сумму квадратов
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    print sum1Sq
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    print sum2Sq
    # Вычислить сумму произведений
    pSum = sum([prefs[p1][it]*prefs[p2][it] for it in si])
    print pSum
    # Вычислить коэффициент Пирсона
    num = pSum-(sum1*sum2/n)
    print num
    den = sqrt((sum1Sq-pow(sum1, 2)/n)*(sum2Sq-pow(sum2, 2)/n))
    print den
    if den == 0:
        return 0
    r = num/den
    return r

print(u'sim_pearson :')
print sim_pearson(critics, 'Lisa Rose', 'Gene Seymour')