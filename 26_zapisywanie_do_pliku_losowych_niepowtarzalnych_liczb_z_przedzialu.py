class Losuj():

    def losuj(self, a, b, n, t):
        import random
        random.seed()
        self.list = []
        while len(self.list) < n:
            self.x = random.randint(a, b)
            if self.x not in self.list:
                self.list.append(self.x)
            else:
                continue

        for j in self.list:
            j = str(j)
            t.write(j + "\n")

a = int(input("Podaj dolną granicę: "))

b = int(input("odaj górną granicę: "))

n = int(input("Podaj liczbę wierszy: "))

L = Losuj()

t = open("losuj.txt", "w+")

if n <= b-a:
    L.losuj(a,b,n,t)
elif n > b-a:
    n = b-a
    L.losuj(a, b, n, t)
