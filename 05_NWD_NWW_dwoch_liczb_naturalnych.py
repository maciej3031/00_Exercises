# Wyliczanie NWD i NWW
# 1. wprowadzanie liczb
print("Podaj dwie liczby naturalne:")
a = input("Pierwsza:")
b = input("Druga:")

a = int(a)
b = int(b)

# 2. ustalenie która jest mniejsza
if a > b:
      w = a
      m = b
else:
      w = b
      m = a
# 3. pętla główna
r = w % m
while r:
      w = m
      m = r
      r = w % m
# 4. wyświetlenie rezultatów
print("NWD liczb %i i %i wynosi %i, a ich NWW wynosi %i" % (a,b,m,a*b/m))