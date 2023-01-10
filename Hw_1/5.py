"""
    Витушкин Денис
    Дано уравнение ax + b = 0 и отрезок [m;n]. Ответьте на вопрос, попадает ли решение уравнения в указанный отрезок.
"""
print("Enter a,b:")
a , b = float(input("a: ")) , float(input("b: "))
print("Enter m,n:")
m , n = float(input("m: ")) , float(input("n: "))
x =- b / a
print("Result = " , (x >= m and x <= n))