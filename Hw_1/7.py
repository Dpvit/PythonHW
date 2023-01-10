"""
    Витушкин Денис
    Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.
"""
def find_all(str_):
    sum=0
    mult=1
    for char in str_:
        sum+= int(char)
        mult*= int(char)
    return sum,mult


print("Enter numbers: ")
a , b = str(input("a: ")) , str(input("b: "))
print("Result for ",int(a) , ":  " , find_all(a))
print("Result for ",int(b) , ": " , find_all(b))