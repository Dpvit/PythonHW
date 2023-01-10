"""
    Витушкин Денис
    Необходимо реализовать калькулятор. Пользователь вводит строку из 3 элементов,
    разделенных пробелом
"""

while True:
    a,oper,b = input().split()
    a = float(a)
    b = float(b)
    if oper == '+':
        print(a + b)
    elif oper == '-':
        print(a - b)
    elif oper == '*':
        print(a * b)
    elif oper == '/':
        print(a / b)
    elif oper == '%':
        print(a % b)
    elif oper == '//':
        print(a // b)
    else:
        print("None")