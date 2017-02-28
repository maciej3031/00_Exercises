print("Równanie typu: ax^2 + bx + c")

print("Podaj a")
a = input()

print("Podaj b")
b = input()

print("Podaj c")
c = input()

print("podaj dokładność")
i = input()

a = float(a)
b = float(b)
c = float(c)
i = int(i)

if a == 0:
    print("Równanie nie jest równaniem kwadratowym")
else:
    delta = b*b - 4*a*c
    if delta == 0:
        wynik =round( -b/(2*a), i)
        print("Istnieje jeden pierwiastek równy {}".format(wynik))
    elif delta > 0:
        wynik1 = round((-b - (delta ** 0.5)) / (2 * a), i)
        wynik2 = round((-b + (delta ** 0.5)) / (2 * a), i)
        print("Istnieją dwa pierwiastki równe odpowiednio {} i {}".format(wynik1,wynik2))
    else:
        wynik1 = (-b - (delta ** 0.5)) / (2 * a)
        wynik2 = (-b + (delta ** 0.5)) / (2 * a)
        re1 = round(wynik1.real, i)
        im1 = round(wynik1.imag, i)
        wynik1 = re1 + im1*1j

        re2 = round(wynik2.real, i)
        im2 = round(wynik2.imag, i)
        wynik2 = re2 + im2 * 1j

        print("Istnieją dwa pierwiastki zespolone równe odpowiednio {} i {}".format(wynik1, wynik2))


