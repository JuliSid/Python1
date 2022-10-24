# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1

# n = int(input('Введите число '))
# dict = {}
# for i in range (1,n+1):
# dict[i] = 3*i + 1
# print(dict)



print(f'Введите число:')
n = int(input())
d = {a: (3 * a + 1) for a in range(1, n + 1)}

print(d.keys())
print(d.values())
