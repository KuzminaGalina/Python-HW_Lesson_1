# 1- Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

def WhatsTheDay (NumberOfDay):
    if NumberOfDay<1 or NumberOfDay>7:
        print('There is no such day')
    elif NumberOfDay >5:
        print('This is weekend')
    else:
        print('This is weekday')

NumberOfDay1=int (input('Enter the day number '))
WhatsTheDay(NumberOfDay1)


