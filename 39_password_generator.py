import random
random.seed()

letters = "abcdefghijklmnoprstuvwxyz"
numbers = "1234567890"
special = r"!@#$%^&*_+"

def strong():
    x = random.randint(6,8)
    y = random.randint(3,6)
    z = random.randint(2,4)
    word = [random.choice([i for i in letters]) for i in range(x)]
    num = [random.choice([i for i in numbers]) for i in range(y)]
    spe = [random.choice([i for i in special]) for i in range(z)]
    lista = word + num + spe
    random.shuffle(lista)
    password = "".join(lista)
    return password

def weak():
    x = random.randint(4, 6)
    y = random.randint(2, 3)
    word = [random.choice([i for i in letters]) for i in range(x)]
    num = [random.choice([i for i in numbers]) for i in range(y)]
    lista = word + num
    random.shuffle(lista)
    password = "".join(lista)
    return password

print("Do you want strong or week password? [s/w]")

inp = input()

if inp == "s":
    print(strong())
elif inp == "w":
    print(weak())
else:
    print("Błąd. Nieznane polecenie.")


