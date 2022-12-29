"""
    Витушкин Денис
    Напишите программу, выполняющую перевод
     из буквенных оценок в числовые и обратно.
"""

while True:
    c = input()
    if c == '':
        break
    try:
        buf = ord("A") - int(c) + 5
        if int(c) not in [1, 2, 3, 4, 5]:
            raise ValueError
        else:
            print("Из int в char :",int(c),'_-> ',chr(buf))
    except ValueError:
        buf = ord("A") - ord(c) + 5
        if buf not in [1, 2, 3, 4, 5]:
            print("Некорректно")
        else:
            print("Из char в int",c,'->',buf)
        