import sys

ekran = sys.stdout
a = open("plik1.txt","w+")
sys.stdout = a


print("Mega")

sys.stdout = ekran

print("cokolwiek")

a.close()
