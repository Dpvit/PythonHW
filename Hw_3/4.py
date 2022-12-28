"""
    Витушкин Денис
    Напишите программу, которая запрашивает у пользователя деталь,
     считает их количество, а также общую стоимость.Д
"""
guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print("Сейчас на вечеринке {} человек: {}".format(len(guests), guests))
    input_ = input_ut("Гость пришёл или ушёл? ")
    if input_ == "пришел":
        input_ = input_ut("Имя гостя: ")
        if len(guests) <= 6:
            guests.append(input_)
            print("Привет, {}!".format(input_))
        else:
            print("Прости, {}, но мест нет.".format(input_))
    elif input_ == "ушел":
        input_ = input_ut("Имя гостя: ")
        print("Пока, {}".format(guests.pop(guests.index(input_))))
    elif input_ == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    else:
        print("Че?")