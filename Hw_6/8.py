"""
    Витушкин Денис
    Добавьте в класс Rectangle метод contains. Метод принимает точку и возвращает True, если точка находится внутри
    прямоугольника и False в противном случае..
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
    def contains(self,point:Point) ->bool:
        if (self.p1.x < point.x < self.p2.x) and (self.p1.x < point.x < self.p2.x) :
            return True
        return False


p1 = Point(0,0)
p2 = Point(2,2)
r =Rectangle(p1,p2)
point = Point(1,1)
print(r.contains(point))