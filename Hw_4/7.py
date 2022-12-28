"""
    Витушкин Денис
    Строка называется палиндромом, если она пишется одинаково в обоих направлениях. Например, 
    палиндромами в английском языке являются слова «anna», «civic», «level», «hannah».

"""

def is_palindrom(s) ->bool:
    k=len(s) - 1
    for i in range(len(s)//2):
        if s[i] == s[k]:
            i+=1
            k-=1
        else:
            return False
    return True

s1='haaah'
print(is_palindrom(s1))
s2='haassha'
print(is_palindrom(s2))