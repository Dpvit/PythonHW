
"""
    Витушкин Денис
    ДЧастная контора даёт в прокат ролики самых разных размеров. 
    Человек может надеть ролики любого размера, которые не меньше размера его ноги.
"""

sk_size_s = input("Введите размеры коньков через пробел:\n")
skates = [int(x) for x in sk_size_s.split()]
hmn_size_s = input("Введите размеры ног людей через пробел:\n")
hmn_size_s.split()
legs = [int(x) for x in hmn_size_s.split()]

legs.sort(reverse=True)
skates.sort()

fit = 0
for i in legs:
    if any(i <= skates_buf for skates_buf in skates):
        for j, skates_buf in enumerate(skates):
            if i <= skates_buf:
                fit += 1
                skates.pop(j)
                break
print("Наибольшее кол-во людей, которые могут взять ролики: ",fit)


