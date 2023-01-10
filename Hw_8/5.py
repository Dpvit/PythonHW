
alp='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
d={}
for c in alp:
    d[c]=0
print(d)

from zipfile import ZipFile

with ZipFile("voyna-i-mir.zip", "r") as myzip:
    myzip.extract("voyna-i-mir.txt")

file_txt = open("voyna-i-mir.txt",'rb')
for line in file_txt:
    for c in line:
        if chr(1072-32+c) in d:
            d[chr(1072-32+c)]+=1
        
print(d)