# Получить список чисел. Превратите его в список квадратов этих чисел.

import random

N= 5
list1 = []
for i in range(N):
    list1.append(random.randint(1,5))
print(list1)

for i in range(len(list1)):
    list1[i] **=2
print(list1)