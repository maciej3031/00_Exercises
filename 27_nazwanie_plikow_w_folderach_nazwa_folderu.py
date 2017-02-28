from os import *
from glob import *

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
    chdir(d+"/"+j)
    list3 = [x for x in glob("*.py")] #filtrowanie jakim plikom zmieniamy nazwy MOŻE BY TYLKO JEDEN TAKI PLIK W FOLDERZE
    for k in list3:
        rename(list3[0], list2[i] + ".py")


