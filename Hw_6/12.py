"""
    Витушкин Денис
    Создать классы для травоядного животного и травы.
"""

class Grass:
    def __init__(self) -> None:
        self.amount = 100
        self.value = 1
    def print(self):
        print("Amount of grass = ", self.amount)
class Animal:
    def __init__(self) -> None:
        self.hunger = -5

    def eat(self,grass:Grass):
        grass.amount -=1
        self.hunger +=grass.value
    def print(self):
        print("I am animal, my hunger level =",self.hunger)


a=Animal()
g=Grass()
g.print()
a.print()
a.eat(g)
g.print()
a.print()

