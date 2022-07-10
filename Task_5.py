# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
def FindDistanceBetweenPointsAB (a1, a2, b1, b2):
    distansAB = math.sqrt((b1 - a1)**2 + (b2 - a2)**2)
    return round(distansAB,2)

a1 = int (input('Введите координаты точки А: '))
a2 = int (input('Введите координаты точки А: '))
b1 = int (input('Введите координаты точки B: '))
b2 = int (input('Введите координаты точки B: '))

distansAB = FindDistanceBetweenPointsAB (a1, a2, b1, b2)
print(f'Расстояние между точкой А {a1,a2} и точкой B {b1,b2} составляет {distansAB}')
