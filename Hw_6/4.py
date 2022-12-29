"""
    Витушкин Денис
    Добавить поле grades, в котором будет храниться список оценок. 
    Создать список учеников, заполняя оценки каждого случайными числами
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
    def set_grade(self,list_):
        self.grades = list_
    def get_grade(self) -> list:
        return self.grades

Humans = [Human('a','b','12'),Human('c','d','13'),Human('e','f','14'),Human('g','h','15'),Human('i','j','16')]
for i in range(len(Humans)):
    list_ = [i,i+1,i+2,i+3]
    Humans[i].set_grade(list_)

for i in range(len(Humans)):
    print(Humans[i].get_grade())
