rzym1 = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
rzym2 = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


x = str(input("Podaj liczbę rzymską mniejszą:"))
print("Liczba rzymska", x ,"w notacji arabskiej to: ")
la = 0

for i in rzym1:
    if i in x:
        la += rzym1[i]
        x = x.replace(i,"a")


for i in rzym2:
    if i in x:
        n = x.count(i)
        la += n * rzym2[i]
        x = x.replace(i,"a")


print(la)


