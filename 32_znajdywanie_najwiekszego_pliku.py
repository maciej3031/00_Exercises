import os
def znajdznajwiekszy():
    path1 = input("Podaj ścieżkę katalogu")

    print(path1)


    list = []
    for i, j, k in os.walk(path1):      #tworzymy listy ścieżek katalogów
        list.append(i)

    sizelist = []   #lista rozmiarów
    sizelistname = []   #lista nazw plików
    for i in list:
        dirlist = os.listdir(i)     #tworzymy listę plików w danym katalogu
        for j in dirlist:
            size = os.path.getsize(i + "/" + j)     #tworzymi liste rozmiarów
            sizelist.append(size)
            sizelistname.append(j)              #tworzymy listę nazw plików
    max1 = max(sizelist)                    #pobieramy maksymalną wartość pliku
    index1 = sizelist.index(max1)           #index maksymalnej wartości
    result = sizelistname[index1]           #nazwę pliku o indexie maksymalnej wartości
    print("Największy plik to: ", result, " waży on: ", max1, " bajtów")