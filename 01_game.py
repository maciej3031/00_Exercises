import random
random.seed()

number = random.randint(1,100)
print("Zgadnij moja liczbę z przedzialu 1-100!")
a = 0
while a != number:
    a = input()
    a = int(a)
    if a == number:
        print("Brawo!!! Zgadles!!!")
        break
    elif a < number:
        print("Za mało...")
    else:
        a > number
        print("Za dużo...")
print("Wcisnij enter aby kontynuowac")
x = input()