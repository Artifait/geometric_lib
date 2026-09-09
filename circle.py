import math


def area(r):
    '''Вычисление площади круга по его радиусу: circle.area(5) -> 78.54...'''
    return math.pi * r * r


def perimeter(r):
    '''Вычисление периметра круга по его радиусу: circle.perimeter(5) -> 31.42...'''
    return 2 * math.pi * r

