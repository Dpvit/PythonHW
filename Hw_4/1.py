"""
    Витушкин Денис
    Дан список из чисел.
Определите их НОК (наименьшее общее кратное) и НОД (наибольший общий делитель).
"""

def NOK(a,b) -> int:
    a_max = max(a, b)
    b_min = min(a, b)
    while b_min > 0:
        a_max -= b_min
        if a_max < b_min:
            tmp = a_max
            a_max = b_min
            b_min = tmp
    return a_max

def NOD(a,b) ->int:
    return a*b//NOK(a,b)

print(NOK(6,12))