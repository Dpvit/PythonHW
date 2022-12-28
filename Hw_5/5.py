"""
    Витушкин Денис
    Дано натуральное число N. Выведите слово YES, если число N 
    является точной степенью двойки, или слово NO в противном случае.

"""



input_ = bin(int(input()))
str_ = input_[2:]
res = 'YES'
for i in str_:
    if i == '0':
        res = 'NO'
        break
print(res)