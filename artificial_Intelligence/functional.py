#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Евклидово расстояние
from recomendations import critics

# Возвращает оценку подобия person1 и person2 на основе расстояния
def sim_distance(prefs,person1,person2):
# Получить список предметов, оцененных обоими
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1
        # Если нет ни одной общей оценки, вернуть 0
        if len(si) == 0:
            return 0
        # Сложить квадраты разностей
        sum_of_squares = sum([pow(prefs[person1][item]-prefs[person2][item], 2)
            for item in prefs[person1] if item in prefs[person2]])
        return 1/(1+sum_of_squares)

print sim_distance(critics,critics['Lisa Rose'],critics['Michael Phillips'])