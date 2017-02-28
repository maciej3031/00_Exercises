import random
random.seed()

def zgadnijliczbe():
    number = random.randint(1000, 9999)  # losowa liczba 4 cyfrowa generowana przez program
    j=0
    while True:
        inp = int(input("Podaj liczbę"))
        if inp == number:       #jeżeli podana przez użytokwnika liczba siezgadza koniec
            print("Brawo zgadłeś!")
            break
        else:
            lista = []          # pusta lista potrzebna do zgodności
            for i, k in enumerate(str(inp)):        #bierzemy ponumerowane wszystkie cyfry w liczbie podanej przez uzytkownika i zamienionej na stringa
                if k in str(number) and list(str(number))[i] == k:      #jeżeli dana cyfra(string) znajduje się w liczbie programu i jest na dobrym miejscu
                        lista.append(k)                             # to dąłączamy sprawdzoną i zgodną cyfre do listy
        j += 1
        print("Próby: {}, Zgodność: {}".format(j, len(lista)))      #dlugosc listy to ilosc zgodnych cyfr

zgadnijliczbe()