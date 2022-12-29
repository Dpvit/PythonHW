"""
    Витушкин Денис
    Описать класс десятичного счётчика. Он должен обладать внутренней переменной, 
    хранящей текущее значение, методами повышения значения (increment) и понижения (decrement), получения текущего значения get_counter. 
    Учесть, что счётчик не может опускаться ниже 0.
"""
class Counter:
    def __init__(self) -> None:
        self.counter = 0
    def increment(self) ->None:
        self.counter +=1
    def decrement(self) ->None:
        if(self.counter == 0):
             return
        self.counter -=1
    def get_value(self) -> int:
        return self.counter
    
c=Counter()
c.increment()
print(c.get_value())
c.increment()
print(c.get_value())
c.decrement()
print(c.get_value())
c.decrement()
print(c.get_value())
c.decrement()
print(c.get_value())