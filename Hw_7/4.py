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
        if type(self) == Water or type(other) == Water:
            if type(other) == Air or type(self) == Air:
                return Storm()
            if type(other) == Fire or type(self) == Fire:
                return Steam()
            if type(other) == Earth or type(self) == Earth:
                return Mud()
        if type(self) == Air or type(other) == Air:
            if type(other) == Fire or type(self) == Fire:
                return Light()
            if type(other) == Earth or type(self) == Earth:
                return Dust()
        if type(self) == Fire or type(other) == Fire:
            if type(self) == Earth or type(other) == Earth:
                return Lave()
        if type(self) == Storm or type(other) == Storm:
            if type(self) == Dust or type(other) == Dust:
                return DustStorm()

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
class DustStorm(Base):
    def __init__(self) -> None:
        self.name = "Песчаная Буря"
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