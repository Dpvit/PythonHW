"""
    Витушкин Денис
    Вода + Воздух = Шторм
    Вода + Огонь = Пар
    Вода + Земля = Грязь
    Воздух + Огонь = Молния
    Воздух + Земля = Пыль
    Огонь + Земля = Лава

"""

class Base:
    def __init__(self) ->None:
        self.name = ''
    def __add__(self,other):
        if type(self) == Water:
            if type(other) == Air:
                return Storm()
            elif type(other) == Fire:
                return Steam()
            elif type(other) == Earth:
                return Mud()
            else:
                return None
        elif type(self) == Air:
            if type(other) == Fire:
                return Light()
            elif type(other) == Earth:
                return Dust()
            else:
                return None
        elif type(self) == Fire:
            if type(other) == Earth:
                return Lave()
            else:
                return None
        else:
            return None
            

class Water(Base):
    def __init__(self) -> None:
        self.name = "Вода"
class Fire(Base):
    def __init__(self) -> None:
        self.name = "Огонь"
class Earth(Base):
    def __init__(self) -> None:
        self.name = "Земля"
class Air(Base):
    def __init__(self) -> None:
        self.name = "Воздух"
class Storm(Base):
    def __init__(self) -> None:
        self.name = "Шторм"
class Steam(Base):
    def __init__(self) -> None:
        self.name = "Пар"
class Mud(Base):
    def __init__(self) -> None:
        self.name = "Грязь"
class Light(Base):
    def __init__(self) -> None:
        self.name = "Молния"
class Dust(Base):
    def __init__(self) -> None:
        self.name = "Пыль"
class Lave(Base):
    def __init__(self) -> None:
        self.name = "Лава"

water = Water()
air = Air()
combine = water + air
print(combine.name)