"""
    Витушкин Денис
    Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со словами
"""

name = str(input("Enter name: "))
print(name , "- чемпион!")

print("-" * len(name))

name=name.lower()
print("len = " , len(name))

if 'п' in name:
    print(True)
else:
    print(False)

counter = 0
for char in name:
    if char == 'а':
        counter += 1
print(counter)