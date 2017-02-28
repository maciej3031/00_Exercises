# Wyszukiwanie liczb pierwszych
koniec = input("Podaj górną granicę zakresu do wyszukania liczb pierwszych:")
koniec = int(koniec)
pierwsze = list(range(koniec+1))
n = 1
while ( n < koniec ):
    n += 1
    if pierwsze[n]==0: # zerem oznaczamy liczby nie-pierwsze
        continue
    m = n * 2
    while m <= koniec:
        pierwsze[m]=0 # zerem oznaczamy liczby nie-pierwsze
        m += n
print("Znaleziono następujące liczby pierwsze:")
for n in pierwsze[1:]:
    if n: print("% i" % n,end="")