from math import *

print("Podaj kąt w stopniach")
a = float(input())


k = radians(a)
print("sin{}° = ".format(a) + str(round(sin(k),3)))
print("cos{}° = ".format(a) + str(round(cos(k),3)))

if tan(k) > 1000000000 or tan(k) < -1000000000:
    print("tan{}° nie istnieje".format(a))
else:
    print("tan{}° = ".format(a) + str(round(tan(k), 3)))

if 1/tan(k) > 1000000000 or 1/tan(k) < -1000000000:
    print("cot{}° nie istnieje".format(a))
else:
    print("cot{}° = ".format(a) + str(round(1 / tan(k), 3)))


