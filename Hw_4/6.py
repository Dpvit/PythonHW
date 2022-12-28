"""
    Витушкин Денис
    Напишите функцию, которая принимает неограниченное количество числовых аргументов 
    и возвращает кортеж из двух списков:

"""

def razdelitel(*argv):
    pos = []
    neg = []
    for i in argv:
        if i>=0:
            pos.append(i)
        elif i<0:
            neg.append(i)
        else:
            print("???")
    pos.sort() 
    neg.sort(reverse=True)
    
    return pos,neg

print(razdelitel(1,2,3,-4,-21,33,12,42,-3,0))