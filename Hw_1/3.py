"""
    Витушкин Денис
    Вычислите значение следующего выражения (аргументы - целые числа и вводятся с клавиатуры):...
"""
print("Enter x,y,z: ")
x , y , z = int(input("x: ")) , int(input("y: ")) , int(input("z: "))
result = round((((x**5+7)/(abs(-6)*y))**(1/3))/(7-z%y),3)
print("Result = ",result)
