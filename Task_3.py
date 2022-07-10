# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# которой находится эта точка (или на какой оси она находится).

def Quarter(x, y):
    quarter = None
    if x == 0 or y == 0: print('Incorrect data entry')
    elif x > 0 and y > 0: quarter = 1
    elif x < 0 and y > 0: quarter = 2
    elif x < 0 and y < 0: quarter = 3
    else: quarter = 4
    print(f'Point with coordinates {x, y} is located in {quarter} quarter')

x=int (input('Enter x: '))
y=int (input('Enter y: '))
Quarter(x, y)