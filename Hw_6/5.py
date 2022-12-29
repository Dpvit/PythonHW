"""
    Витушкин Денис
    Вывести информацию об учениках в порядке убывания среднего балла. 
    Подсчёт среднего балла вынести в отдельный метод.
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
    def mid_grade(self) -> float:
        counter = 0
        for i in range(len(self.get_grade())):
            counter+=i
        return counter/len(self.get_grade())   


Humans = [Human('a','b','12'),Human('c','d','13'),Human('e','f','14'),Human('g','h','15'),Human('i','j','16')]
for i in range(len(Humans)):
    list_ = [i,i+1,i+2,i+3]
    Humans[i].set_grade(list_)

mid=[]
for i in range(len(Humans)):
    mid_grade = Humans[i].mid_grade() + i 
    mid.append(mid_grade)
mid.sort(reverse=True)
print(mid)