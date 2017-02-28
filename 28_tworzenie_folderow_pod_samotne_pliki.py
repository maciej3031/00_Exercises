from os import *
from glob import *
from shutil import *

#Pełna ścieżka:
d = input("Podaj ścieżkę katalogu")
chdir(d)
print(d)

print("Zmieniona ścieżka = ", getcwd())

a = listdir(d)


list = [x for x in glob("*.py")]


for i, j in enumerate(list):
    j = j[0:-3]
    mkdir(d + "/" + j)
    move(list[i], d + "/" + j)