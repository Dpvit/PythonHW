"""
    Витушкин Денис
    Напишите программу, которая будет суммировать все числа, введенные пользователем, 
    игнорируя при этом нечисловой ввод.
"""
sum = 0

while True:
    try:
        s=float(input())
    except ValueError:
        continue
    sum+=s
    print(sum)