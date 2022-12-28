"""
    Витушкин Денис
    Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру.
"""

str = 'sdfasdfs1dfsdasv'

str.split()
if any(i.isdigit() for i in str):
    print("Hit")
else:
    print("Miss")