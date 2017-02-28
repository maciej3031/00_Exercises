import os
from time import *

def znajdznajstarszy():
    path1 = input("Podaj ścieżkę katalogu")
    os.chdir(path1)
    print(path1)


    list = []
    for i, j, k in os.walk(path1):      #tworzymy listy ścieżek katalogów
        list.append(i)

    agelist = []   #lista czasu utworzenia
    agelistname = []   #lista nazw plików
    for i in list:
        dirlist = os.listdir(i)     #tworzymy listę plików w danym katalogu
        for j in dirlist:
            age = os.path.getctime(i + "/" + j)     #tworzymi liste czasów powstania
            agelist.append(age)
            agelistname.append(j)              #tworzymy listę nazw plików

    min1 = min(agelist)               #pobieramy najstarszą wartośc pliku
    index1 = agelist.index(min1)           #index najstarszej wartości
    result = agelistname[index1]           #nazwę pliku o indexie najstarszego czasu powstania
    min1 = localtime(min1-3600)
    print("Najstarszy plik to: ", result, " powstał on: ", "{}/{}/{}".format(min1[2],min1[1],min1[0]), "o godzinie: {}:{}:{}".format(min1[3],min1[4],min1[5]))

znajdznajstarszy()
