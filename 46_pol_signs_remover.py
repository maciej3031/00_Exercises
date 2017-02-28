import os

def pol_signs_remover(name = None):
    if not name:
        name = input("Podaj nazwę pliku w formacie np.: 'dane.py'. Bez apostrofów. \n"
                 "Plik z programem musi się znajdować w tym samym folderze co plik formatowany: ")
    plik = open("{}".format(name), "r+", encoding = "UTF-8")
    plik.seek(0,0)
    x = plik.read().replace("ą", "a").replace("ć", "c").replace("ę", "e").replace("ł", "l").replace("ń", "n").replace("ó", "o").replace("ś", "s").replace("ź", "z").replace("ż", "z")
    namesplit = os.path.splitext(name)
    plik_copy = open(namesplit[0] + "_eng" + namesplit[1], "w")
    plik_copy.write(u"{}".format(x))
    plik.close()
    plik_copy.close()

if __name__ == "__main__":
    pol_signs_remover("test.py")