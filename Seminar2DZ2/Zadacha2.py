# Программа принимает на вход число N и выдает набор произведений чисел от 1 до N: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# проверка на вщественное число
import random

def Enter_Number(text, type = 1): # функция ввода числа с проверкой
    print(text)
    while True:
        if type==1:
            try:
                value= int(input())
                break
            except:
                print('ошибка введите целое число')
        elif type == 2 or type == 3:
            try:
                if type == 2:
                    value= float(input())
                    break
                elif type == 3:
                    from decimal import Decimal
                    value = Decimal(input())
                    break
            except:
                print('Введите число ')
    return value





number = abs(int(input('Введите целое число: ')))
povnum = 1
list = []
for i in range(1,number+1):
    povnum *=i
    list.append(povnum)
print(list)