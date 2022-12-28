"""
    Витушкин Денис
    Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года. 

"""
date = '10.06.1960'
def is_magic(s) ->bool:
    s=s.split('.')
    mult = int(s[0]) * int(s[1])
    last = int(s[2][2:4])
    if (mult == last):
        return True
    return False

for i in range(1,29):
    for j in range(1,13):
        for k in range(1900,1999):
            date = str(i) +'.'+ str(j) +'.'+ str(k)
            if(is_magic(date)):
                print(date)
