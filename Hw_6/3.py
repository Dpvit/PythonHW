"""
    Витушкин Денис
    Добавить метод greet, вызов которого будет выводить в консоль информацию о человеке в формате "Привет!
    Меня зовут Петров Василий, мне 12 лет".
"""

class Human:
    def __init__(self,name,s_name,age):
        self.name = name
        self.s_name = s_name
        self.age = age
    def __str__(self) ->str:
        out = self.name +' '+ self.s_name +' '+ str(self.age)
        return out
    def greet(self) -> None:
        print('Меня зовут',self.name,self.s_name,', мне',self.age,'года.')
H=Human('Denis','Vitushkin',23)
#print(H.name,H.s_name, H.age)
#print(H.__str__()) 
H.greet()