tablica = [("\t","Żółci", "Czerwoni", "Zieloni", "Niebiescy"), ("Żółci", 0, 3/5, 2/5, 1/1),("Czerwoni", round(5/3,1), 0, 2/5, 4/8),("Zieloni", 5/2, 5/2, 0, 2/4),("Niebiescy", 1/1, 8/4, 4/2, 0)]

zolt = 0
czer = 0
ziel = 0
nieb = 0

for i in tablica:
    for j in i:
        print("%12s" % j, end="")
    print("")

for i, k in enumerate(tablica):
    for j in k:
        if type(j) != str:
            if j > 1:
                if i == 1:
                    zolt = zolt + 3
                elif i == 2:
                    czer = czer + 3
                elif i == 3:
                    ziel = ziel + 3
                elif i == 4:
                    nieb = nieb + 3
            elif j == 1:
                if i == 1:
                    zolt = zolt + 1
                elif i == 2:
                    czer = czer + 1
                elif i == 3:
                    ziel = ziel + 1
                elif i == 4:
                    nieb = nieb + 1
            else:
                continue

druzyny = [("Żółci", zolt), ("Czerwoni", czer), ("Zieloni", ziel), ("Niebiescy", nieb)]

sorted(druzyny, key = lambda x: x[1])
druzyny.reverse()
print()
for i in druzyny:
    print("{}   {}".format(i[0],i[1]))