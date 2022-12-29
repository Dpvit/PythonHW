"""
    Витушкин Денис
    Создать класс для часов.
"""

class Clock:
    def __init__(self,s_hours,s_min):
        self.hours = s_hours
        self.min = s_min

    def add_min(self):
        if(self.min == 59):
            self.min = 0
            self.hours+=1
            if(self.hours == 24):
                self.hours =0
        else:
            self.min+=1

    def add_hour(self):
        self.hours+=1
        if(self.hours == 24):
            self.hours =0
    def show_time(self):
        print(self.hours, ':', self.min if self.min !=0 else '00')

c=Clock(12,58)
c.add_min()
c.show_time()
c.add_min()
c.show_time()
c.add_hour()
c.show_time()


        