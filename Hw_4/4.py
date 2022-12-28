"""
    Витушкин Денис
    Для введенного предложения выведите статистику символ=количество. 
    Регистр букв не учитывается.
"""

returnal = {}

s = '123sadfasdfnvasndhasdfioewiufsd'.lower()
s_unique = set(s)
for i in s_unique:
    returnal[i] = s.count(i)

print(returnal)