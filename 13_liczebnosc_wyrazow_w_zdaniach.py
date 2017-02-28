print("Wpisz dowolny tekst")
a = str(input())

zdania = a.split(".")

n = []
for zdanie in zdania:
    wyraz = zdanie.split()
    n.append(len(wyraz))


for j, k in enumerate(n):
    print("zdanie {} ma {} wyrazów".format(j+1,k))