# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

n = int(input('Введите число :'))
list = [round((1+1/n)**n, 15) for n in range(1, n+1)]
print(f'Сумма: {round(sum(list), 15)}')



#2 

n = int(input('Введите число :'))
d= {}
sum = 0
for i in range(1, n+1):
    d[i] = round((1+1/i)**i, 15)
    sum+=d[i]
print(d)
print(round(sum,2))