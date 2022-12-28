"""
    Витушкин Денис
    Вы загадываете число от 1 до 100 (включительно). 
    Компьютер спрашивает у вас «Твое число равно, меньше или больше, чем число N?»,  
    где N — число, которое хочет проверить компьютер.

"""

def calculate():
    min=0
    max = 100
    while True:
        tmp = min + (max - min)//2
        print(min,max,'!!!')
        print(tmp,end='')
        answer = int(input("?"))
        if(answer == 1):
            print("!")
            break
        if(answer == 2):
            min=tmp
            print(min)
        if(answer == 3):
            max=tmp
            print(max)

calculate()

        