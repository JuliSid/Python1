# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите номер дня недели: '))
if day > 7 or day < 1:
    print('Попробуйте еще раз')
elif day == 6 or day == 7:
    print('Выходной! Ура!')
else:
    print('Работать!')