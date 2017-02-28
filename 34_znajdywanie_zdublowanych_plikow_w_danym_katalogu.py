import os

def list_flatten(l, a=None):    # funckja spłaszczająca listy
    #check a
    if a is None:
        #initialize with empty list
        a = []

    for i in l:
        if isinstance(i, list):     #sprawdza czy i jest listą
            list_flatten(i, a)
        else:
            a.append(i)
    return a

def znajdzdubel():
    path1 = input("Podaj ścieżkę katalogu")
    os.chdir(path1)
    list = []

    for i, j, k in os.walk(path1):      #tworzymy listę plików w katalogu i ją spłaszczamy
        list.append(k)
        list = list_flatten(list)

    filelist = []   #lista niepowtarzalnych plików
    dubellist = []  # lista zdublowanych plików

    for i in list:
        if i not in filelist:
            filelist.append(i)
        elif i not in dubellist:
            dubellist.append(i)
        else:
            continue
    filelist = [j for j in filelist if j not in dubellist]  #usuwamy z listy niepowtarzalnych pliki zdublowane
    sciezkifold = []
    for i, j, k in os.walk(path1):      # tworzyli listę ścieżek folderów
        sciezkifold.append(i)

    sciezki = []
    for i in sciezkifold:
        pliczki = os.listdir(i)         # tworzymy listę plików w każdym z folderów z listy sciezkifold
        for j in pliczki:               # szukamy wszystkich plików w danym katalogu które pokrywają się ze zdublowanymi plikami
            if j in dubellist:
                sciezki.append((i + "\\" + j))      #tworzymy listę ścieżek wszystkich zdublowanych plików

    print("Pliki zdublowane to: ", dubellist)
    print("Ścieżki dostępu do plików zdublowanych: ", sciezki)

znajdzdubel()
