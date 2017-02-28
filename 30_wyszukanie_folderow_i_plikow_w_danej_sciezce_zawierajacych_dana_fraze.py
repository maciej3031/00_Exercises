import os
import glob


def znajdzplikfolder():
    path1 = input("Podaj ścieżkę katalogu")
    os.chdir(path1)
    print(path1)

    word = input("Podaj szukaną frazę")

    list = []
    for i, j, k in os.walk(path1):
        list.append(i)  # tworzy listę wszystkich ścieżek katalogów
    print(list)

    list2 = []
    for x in list:  # w każdy katalogu szukamy plików i katalogów zawierających daną fraze
        directs = glob.glob("*{}*".format(word))
        list2.append(directs)

    list2 = [y for y in list2 if y != []]  # usuwamy puste elementy z listy
    print(list2)


znajdzplikfolder()