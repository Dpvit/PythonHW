"""
    Витушкин Денис
    Реализуйте методы вычисления площади и периметра прямоугольника.
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def perimeter(self):
        return ((self.p2.x - self.p1.x)*2 + (self.p2.y - self.p1.y)*2)
    def ploshad(self):
        return ((self.p2.x - self.p1.x)*(self.p2.y - self.p1.y))

p1 = Point(0,0)
p2 = Point(2,2)
r =Rectangle(p1,p2)
print(r.perimeter())
print(r.ploshad())