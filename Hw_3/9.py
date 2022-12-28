"""
    Витущкин Денис
    N друзей постоянно берут в долг друг у друга деньги. В какой-то момент им надоело забывать, 
    кто, кому и сколько должен, и они придумали систему долговых расписок.
"""

n = int(input("Друзей:"))
k = int(input("Расписок:"))

friends = [0 for i in range(1,n+1)]

for i in range(1, k+1):
    print("Счет начинается с 0")
    a = int(input('Кому: '))
    b = int(input('От кого: '))
    c = int(input('Сколько: '))
    print('\n')
    friends[a] += c
    friends[b] -= c

print('Баланс:')
for i in range(len(friends)):
    print(i,"Друг:",friends[i])