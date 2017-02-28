class Wczytaj():
    def wczytaj(self):
        self.list = []
        while True:
            self.name = input("Podaj imię studenta: ")
            if not self.name: break
            self.surname = input("Podaj nazwisko studenta: ")
            self.group = input("Podaj grupę dziekańską studenta: ")
            self.l = [self.name, self.surname, self.group]
            self.list.append(self.l)
    def zapisz(self,a):
        for i in self.list:
            for j in i:
                a.write(j + "\t")
            a.write("\n")

try:
    a = open("lista.txt","r+")
    b = a.read()
    print("Lista studentów w pliku to:")
    print(b)
    print("Czy chcesz dodać studentów do listy? (y,n)")
    y = input()
    if y == "y":
        a.seek(0,2)
        w = Wczytaj()
        w.wczytaj()
        w.zapisz(a)

    else:
        print("Nie dodano nikogo nowego")

except FileNotFoundError:
    print("Brak pliku, Czy chcesz go utworzyć i wczytać do niego dane (y/n)?")
    x = input()
    if  x == "y":
        a = open("lista.txt", "a+")
        w = Wczytaj()
        w.wczytaj()
        w.zapisz(a)

    else:
        print("Nie utworzono pliku")


