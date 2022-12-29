"""
    Витушкин Денис
    Доработать предыдущий класс, 
    чтобы вся информация о человеке была доступна при вызове str над экземпляром.
"""

class Human:
    def __init__(self,name,s_name,age):
        self.name = name
        self.s_name = s_name
        self.age = age
    def __str__(self) ->str:
        out = self.name +' '+ self.s_name +' '+ str(self.age)
        return out
H=Human('Denis','Vitushkin',23)
print(H.name,H.s_name, H.age)
print(H.__str__()) 