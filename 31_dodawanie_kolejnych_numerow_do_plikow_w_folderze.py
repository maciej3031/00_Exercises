from os import *
from glob import *


def dodajnumer():
    d = input("Podaj ścieżkę")
    chdir(d)
    print("Zmieniona ścieżka = ", getcwd())

    a = listdir(d)

    for i in a:
        if path.isfile(i) is True:
            list1 = [x for x in glob("*.py")]  # filtrowanie plików .py
            list2 = [x for x in glob("[0123456789]*.py")]  # filtrowanie plików .py rozpoczynających się numerem)
    list3 = [y for x, y in enumerate(list1) if
             list1[x] not in list2]  # filtrowanie tych elementów które nie rozpoczynają się numerem

    leng = len(list2)

    for i, j in enumerate(list3):  # dodanie numeru
        num = i + leng + 1
        part2 = str(num) + "_" + j
        rename(j, part2)

dodajnumer()