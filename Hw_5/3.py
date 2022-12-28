"""
    Витушкин Денис
    Пользователь вводит искомый ключ. Также, если он хочет, то может ввести максимальную глубину, 
    -это уровень, до которого будет просматриваться структура.  
"""

def search(html:dict,key:str,depth:int | None = None):
    if key in html:
        return html.get(key)
    if depth == 0:
        return None
    for val in html.values():
        res = search(val,key,depth-1 if depth-1 is not None else None)
        if res is not None:
            break
    else:
        res = None
    return res

html = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input("key: ")
depth = 3
print(search(html,key,depth))