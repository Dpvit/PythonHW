"""
    Витушкин Денис
    На вход подается файл calc_nums.txt, в котором хранятся записи вида
    100 + 34
    23 / 4
"""

file_ = open('calc_nums.txt','r')
res=0
for str_ in file_:
    mass = str_.split(' ')
    if mass[1] == '+':
        res+=int(mass[0]) + int(mass[2])
    elif mass[1] == '-':
        res+=int(mass[0]) - int(mass[2])
    elif mass[1] == '*':
        res+=int(mass[0]) * int(mass[2])
    elif mass[1] == '/':
        res+=int(mass[0]) / int(mass[2])
    elif mass[1] == '%':
        res+=int(mass[0]) % int(mass[2])
    elif mass[1] == '//':
        res+=int(mass[0]) // int(mass[2])
    else:
        continue

print(res)