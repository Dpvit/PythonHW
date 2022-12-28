"""
    Витушкин Денис
    Для введенного предложения выведите статистику символ=количество. 
    Регистр букв не учитывается.
"""

input_ = 'Privet Artem'.lower()
print(input_)
shift = 4
def encode(input_):
    output_ = ''
    for i in input_:
        output_+= chr(ord(i) + shift )

    return output_

def decode(input_):
    output_ = ''
    for i in input_:
        output_+= chr(ord(i) - shift )

    return output_

tmp = encode(input_)
print(tmp)
tmp1 = decode(tmp)
print(tmp1)

