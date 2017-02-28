import random

def rzut_kostka():
    return random.randint(1, 6)

wynik_zawodnika1 = 0
wynik_zawodnika2 = 0
nr_tury = 1

def tura(n):
    global wynik_zawodnika1
    global wynik_zawodnika2
    global nr_tury
    for i in range(n):
        rzut_zawodnika1 = rzut_kostka() + rzut_kostka()
        rzut_zawodnika2 = rzut_kostka() + rzut_kostka()
        print('Tura ', nr_tury)
        print('Pierwszy zawodnik wyrzucil', rzut_zawodnika1, 'a drugi zawodnik wyrzucil',  rzut_zawodnika2)
        if rzut_zawodnika1 > rzut_zawodnika2:
            print('Wygral pierwszy zawodnik')
            wynik_zawodnika1 += 1
        elif rzut_zawodnika1 < rzut_zawodnika2:
            print('Wygral drugi zawodnik')
            wynik_zawodnika2 += 1
        else:
            print('Remis')
        print("Punktacja:")
        print('Zawodnik 1 : ', wynik_zawodnika1)
        print('Zawodnik 2 : ', wynik_zawodnika2)
        nr_tury += 1


def dogrywka():
    print('Potrzebna jest dogrywka')
    tura(1)
    if wynik_zawodnika1 > wynik_zawodnika2:
        print('Całą grę wygrał zawodnik 1')
    elif wynik_zawodnika2 > wynik_zawodnika1:
        print('Całą grę wygrał zawodnik 2')
    else:
        dogrywka()

tura(10)  # przykładowo

if wynik_zawodnika1 > wynik_zawodnika2:
    print('Całą grę wygrał zawodnik 1')
elif wynik_zawodnika2 > wynik_zawodnika1:
    print('Całą grę wygrał zawodnik 2')
else:
    dogrywka()

print("'Zażółć gęślą jaźń1234567890!@%^&*()_+-=[];',./<>?:{}'")