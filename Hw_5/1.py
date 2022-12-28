"""
    Витушкин Денис
    Процесс выравнивания (flattening)
    
"""
list_ = [1, [2, 3], [4, [5, [6, 7]]], [[[8],9], [10]]]

def flattening(list_: list) -> list:
    if not isinstance(list_, (list, tuple)):
        return []
    list_copy = list_.copy()
    if len(list_copy) < 1:
        return []
    if isinstance(list_copy[0], int):
        return [list_copy[0]] + flattening(list_copy[1:])
    if isinstance(list_copy[0], list):
        return flattening(list_copy[0]) + flattening(list_copy[1:])


print(list_)
print(flattening(list_))
    






