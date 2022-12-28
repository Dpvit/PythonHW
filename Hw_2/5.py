"""
    Витушкин Денис
    Создайте пустой словарь для хранения информации о себе и выполните операции, 
    описанные в заготовке.
"""
# 1. Создание словаря
# Создать пустой словарь
info = dict()

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = 'Vitushkin Denis Pavlovich'
info["дата_рождения"] = "Dec 12 1999"
info["место_рождения"] = "Montreal, Canada"
 
# Напечатать словарь
print(info)

# Создать ключ "хобби" со значением = список из строк -
# наименований хобби (например "плавание" и т.д.)
info['хобби'] = ['поесть','полежать','поесть']

# Добавить "программирование" в список хобби
info['хобби'].append('программирование')

# Создать ключ "животные" со значением = кортеж из строк -
# имен домашних животных (например "кошка Мурка" и т.д.)
info['животные'] = ('Кошка Мурка','итд')

# Создать ключ "ЕГЭ" и поместить в него пустой словарь
info['ЕГЭ'] = dict()

# В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# где ключ - наименование предмета, а значение - количество баллов
info['ЕГЭ']['Русский'] = 80
info['ЕГЭ']['Математика'] = 81
info['ЕГЭ']['Физика'] = 82
info['ЕГЭ']['Английский'] = 83
info['ЕГЭ']['Обществознание'] = 84
info['ЕГЭ']['Информатика'] = 85

# Удалите комментарий и допишите код


# Добавить экзамен, который не был сдан, после чего удалить его
info['ЕГЭ']['Химия'] = -1
del info['ЕГЭ']['Химия']

# Создать ключ "вузы" и поместить в него пустой словарь
info['вузы'] = dict()


# В словарь info["вузы"] добавить информацию о вузах,
# где ключ - аббревиатура вуза, а значение -
# количество баллов для специальности, на которую хотели поступить
info['вузы']['MSU'] = 460
info['вузы']['HSE'] = 123


# 2. Вывод на экран
print("Данные:")
# Получившийся словарь
print(info)

# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = tuple(info['ЕГЭ'].keys())
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = list(info['вузы'])
print("Вузы:", uni)

# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info.pop('фио')
# Начинается на гласную? (True/False)
starts_with_vowel = (name[0] in ('A', 'E', 'Y', 'U', 'O', 'I'))
print("* мое имя начинается на гласную букву:", starts_with_vowel)

# Выделить месяц из info["дата_рождения"]
month = info.pop('дата_рождения')
# Родился зимой или летом? (True/False)
born_in_winter_or_summer = born_in_winter_or_summer = month[:3] in ('Dec', 'Jan', 'Feb', 'Jun', 'Jul', 'Aug')
print("* родился летом или зимой:", born_in_winter_or_summer)

# Количество хобби и первое из них
hobbies_count = hobbies_count = len(info['хобби'])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info['хобби'][0]))

# Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(len(info['ЕГЭ'])))


# Сумма баллов по экзаменам
sum_mark = sum(info['ЕГЭ'].values())
print("* сумма баллов = {}".format(sum_mark))

# Максимальный балл среди сданных
max_mark = max(info['ЕГЭ'].values())
print("* макс. балл = {}".format(max_mark))

# Количество вузов, в которые Вы проходите по баллам
# Подсказка: определить, проходите Вы или нет, можно простым сравнением
# суммы баллов с проходным баллом вуза - ``True/False``.
# Для того, чтобы определить количество таких вузов, преобразуйте
# сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
vuz_count = 0
for i in info['вузы'].values():
    if (i == 'Английский' or i=='Обществознание'): continue
    vuz_count += int(sum_mark >= i)
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))



# --------------
# Пример вывода:
#
# {'фио': 'Иванов Иван Иванович', 'место_рождения': 'Париж',
#  'дата_рождения': '01/09/1995'}
# Данные:
# {'фио': 'Иванов Иван Иванович', 'животные': ('кошка Мурка',),
#  'вузы': {'МИРЭА': 240, 'МГУ': 295, 'МГТУ им. Баумана': 255},
#  'хобби': ['игра на гитаре', 'туризм', 'программирование'],
#  'ЕГЭ': {'Математика': 90, 'Информатика': 88, 'Русский язык': 67},
#  'дата_рождения': '01/09/1995', 'место_рождения': 'Париж'}
# Предметы: Информатика, Математика, Русский язык
# Вузы: МГТУ им. Баумана, МГУ, МИРЭА

# Ответы на вопросы:
# * мое имя начинается на гласную букву: True
# * родился летом или зимой: False
# * у меня 3 хобби, первое "игра на гитаре"
# * после окончания школы сдавал 3 экз.
# * сумма баллов = 245
# * макс. балл = 90
# * кол-во вузов в которые прохожу: 1



