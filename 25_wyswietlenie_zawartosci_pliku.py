class Show():
    def show(self):
        self.a = input("Podaj pełną nazwę pliku do wyświetlenia")
        self.b = open(self.a,"r")
        self.c = self.b.read()
        print(self.c)

pokaz = Show()
pokaz.show()