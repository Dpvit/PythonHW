"""
    Витушкин Денис
    Как вы знаете, в языке Python для создания комментариев в коде используется символ #

"""

f = open("sample1.py")
out = open("sample_out.py","w")
for line in f:
    line_out=''
    for elem in line:
        if elem == '#':
            break
        line_out+=elem
    if not line_out.isspace():
        out.write(line_out)


