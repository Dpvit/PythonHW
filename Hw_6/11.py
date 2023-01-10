"""
    Витушкин Денис
    Доработать предыдущую задачу, чтобы можно было складывать двое часов друг с другом. 
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

    def __add__(self,other):
        curr_min = self.min + other.min
        curr_h = self.hours + other.hours
        if curr_min > 59:
            curr_min -= 60
            curr_h+=1
        if curr_h > 23:
            curr_h -= 24
        self.min = curr_min
        self.hours = curr_h
        return Clock(self.hours,self.min)

c1 = Clock(12,22)
c2 = Clock(12,44)
c3=c1.__add__(c2)
c3.show_time()