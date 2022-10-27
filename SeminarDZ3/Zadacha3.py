# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list = [random.randint(99, 1000) / 100 for i in range(random.randint(1, 10))]
print('Заданный список: ', list)

list2 = [round((i%1),2) for i in list]
min = 1
max = 0
for i in list2:
    if i < min and i!=0: min = i       
    if i > max: max = i
print(round((max-min),2))