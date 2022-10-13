# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#1

# max = 0
# if a1 > a2:
#     max = a1
# else:
#     max = a2
# if a3 > max:
#     max = a3
# if a4 > max:
#     max = a4
# if a5 > max:
#     max = a5

# print(max)

#2

max = int(input(f'Введите 1 число: '))

for i in range(4):
    i += 1
    N = int(input(f'Введите {i+1} число: '))
if N > max:
    max = N
print(max)