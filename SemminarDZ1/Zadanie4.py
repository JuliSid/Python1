n = int(input('Координаты какой четверти интересуют?: '))
if n < 1 or n > 4:
    print('Число может быть только от 1 до 4')
elif n == 1:
    print('x > 0 и y > 0')
elif n == 2:
    print('x < 0 и y > 0')
elif n == 3:
    print('x < 0 и y < 0')
elif n == 4:
    print('x > 0 и y < 0')
