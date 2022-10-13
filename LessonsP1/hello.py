# print('Hello World')



# value = None
# a = 123
# b = 1.23
# value = 'Привет'
# print(type(a))
# print(type(b))
# print(type(value))


# s= 'Hello \"World\"'
# print(s)

# s= 'Hello \n World' # переход на новую строку
# print(s)


# print(a, b, value, s) # вывод нескольких значений. Вариант 1

# print('{} - {} - {} - {}'.format(a,b, value, s)) # вывод нескольких значений. Вариант 2

# print(f'{a} - {b} - {value} - {s}') # вывод нескольких значений. Вариант 3

# print('{3} - {0} - {2} - {1}'.format(a,b, value, s)) # вывод нескольких значений. Вариант 4



# list = [1, 2, 3, 'Bucva', 'a'] # Сщздание списков, вместо массивов. Хранилище. Лучше в одном списке хранить все одного типа
# print(list)

# print('Введите число а ') # Ввод и вывод инфо
# a = int(input())
# print('Введите число b ')
# b = int(input())
# print(a,'+', b,'=', a+b)


# a = - 123 # Унарный минус
# a = 12
# b= 5
# c= a+b

# c= a//b # целочисленное деление 
# c = a%b # остаток от деления

# c = a**b # Возведение в степень

# c = round(a/b , 3)

# print(c)

# a=3
# a+=5 # a=a+5

# Операторы if , else, elif

# day = int(input('Введите номер дня недели: '))
# if day > 7 or day < 1:
#     print('Попробуйте еще раз')
# elif day == 6 or day == 7:
#     print('Выходной! Ура!')
# else:
#     print('Работать!')

# Операторы while
# a = 23
# b = 0
# while a!= 0:
#     b = b*10 +(a%10)
#     a//=10
# print(b)

# Операторы while , else

# a = 23
# b = 0
# while a!= 0:
#     b = b*10 +(a%10)
#     a//=10
# else:
#     print('Stop')
# print(b)


#  Цикл for  Вариант 1

# list = [1,2,3,4]
# for i in list:
#     print(i)

#  Цикл for  Вариант 2

# r = range(10)
# for i in r:
#     print(i)


# о строках

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39 количество символов в строке
# print('ещё' in text) # True подстроки
# print(text.isdigit()) # False  числа в строке
# print(text.islower()) # True есть ли заглавные буквы
# print(text.replace('ещё','ЕЩЁ')) # заменить 
# for c in text:
#  print(c)



#Срезы
# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# Функции

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
