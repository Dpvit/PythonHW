"""
    Витушкин Денис
    Дана строка s и символ k. Реализуйте функцию, 
    рисующую рамку из символа k вокруг данной строки, например:
"""

s = 'abcDDcba'
k = '*'

print(k*(len(s)+2))
print(k,s,k,sep='')
print(k*(len(s)+2))