from math import hypot

print("Podaj współrzędną x i y pierwszego punktu")
px1 = float(input())
py1 = float(input())
print("Podaj współrzędną x i y drugiego punktu")
px2 = float(input())
py2 = float(input())

k = hypot(px2-px1,py2-py1)
print("Odleglość wynosi: {}".format(k))
print("Odległość wynosi: %.2f" % k)