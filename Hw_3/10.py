"""
    Витущкин Денис
    Пользователь вводит последовательность из N чисел. Напишите программу, 
    которая определяет, какое минимальное количество и каких чисел надо приписать 
    в конец этой последовательности, чтобы она стала симметричной.

"""

n = int(input('Кол-во чисел: '))
list = []
for i in range(n):
    list.append(int(input('Числo: ')))

add = []
for i in range(len(list)):
    if (list[i:] == list[i:][::-1]):
        add = list[:i][::-1]
        break

print('Последовательность: {}\nНужно приписать чисел: {}\nСами числа: {}'.format(
    list,
    len(add),
    add,
))