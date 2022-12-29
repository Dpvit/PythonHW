"""
    Витушкин Денис
    Создать класс, описывающий человека. Должны быть поля для имени, фамилии и возраста.
    Создать экземпляр и вывести информацию о человеке.
"""

class Human:
    def __init__(self,name,s_name,age):
        self.name = name
        self.s_name = s_name
        self.age = age

H=Human('Denis','Vitushkin',23)
print(H.name, H.s_name, H.age) 