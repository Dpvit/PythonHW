"""
    Витушкин Денис
    Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:...
"""
import math

print("Enter two int:")
x,y = int(input("x: ")),int(input("y: "))

print("+ = ",x+y)
print("- = ",x-y)
print("* = ",x*y)
print("/ = ",round(x/y,2))
print("// = ",x//y)
print("% = ",x%y)
print("** = ",x**y)
print("log10(x) = ",round(math.log10(x),2))
print("log10(y) = ",round(math.log10(y),2))
print("x > y = ",x>y)
print("x >= y = ",x>=y)
print("x < y = ",x<y)
print("x <= y = ",x<=y)
print("x != y = ",x!=y)
print("x == y = ",x==y)
