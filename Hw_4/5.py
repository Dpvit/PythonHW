"""
    Витушкин Денис
    Для введенного предложения выведите статистику символ=количество. 
    Регистр букв не учитывается.
"""

input_ = 'Privet Artem'.lower()
print(input_)
shift = 4
def my_encode(input_):
    output_ = ''
    for i in input_:
        output_+= chr(ord(i) + shift )

    return output_

def my_decode(input_):
    output_ = ''
    for i in input_:
        output_+= chr(ord(i) - shift )

    return output_

tmp = my_encode(input_)
print(tmp)
tmp1 = my_decode(tmp)
print(tmp1)

