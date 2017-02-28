from os import *
from shutil import *


#Pełna ścieżka:
d = input("Podaj ścieżkę katalogu")
chdir(d)
print(d)

print("Zmieniona ścieżka = ", getcwd())

a = listdir(d)
list2 = []
for c in a:
    if path.isdir(c) is True:
        list2.append(c)

for i, j in enumerate(list2):
    d1 = d + "/" + j + "/" + j + ".py"
    move(d1, d)
    rmdir(list2[i])

# MOŻE BY TYLKO JEDEN PLIK W KAŻDYM KASOWANYM FOLDERZE
