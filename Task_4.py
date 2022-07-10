# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

def RangeOfPoints(NumberQuarter):
    range = None
    if NumberQuarter < 1 or NumberQuarter > 4: print('Incorrect data entry')
    elif NumberQuarter == 1: range = 'x > 0, y > 0'
    elif NumberQuarter == 2: range = 'x < 0, y > 0'
    elif NumberQuarter == 3: range = 'x < 0, y < 0'
    else: range ='x > 0, y < 0'
    print(f'Pange of points in {NumberQuarter} quarter is {range}')

try:
    NumberQuarter=int (input('Quarter: '))
    RangeOfPoints(NumberQuarter)
except:
    print("Incorrect data entry")