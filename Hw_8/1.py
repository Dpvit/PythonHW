"""
    Витушкин Денис
    На вход подается файл input_numbers.txt, 
    где записано N целых чисел, которые могут быть разделены пробелами и концами строк. Напишите программу, которая выводит сумму чисел в выходной файл output_sum.txt
"""

f= open("file.txt")
sum=0
for i in f:
    for j in i:
        try:
            h = int(j)
        except ValueError:
            continue
        sum+=h

print(sum)