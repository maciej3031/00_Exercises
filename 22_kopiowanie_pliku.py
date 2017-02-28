n = input("Podaj nazwe pliku do odczytu")

oryg = open(n,"r+b")

kop = open("kopia"+n,"w+b")

while True:
    b = oryg.read()
    if not b: break
    kop.write(b)
kop.close()
oryg.close()

print("zakończono kopiowanie")



