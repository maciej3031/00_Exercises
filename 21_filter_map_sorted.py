l = [1, 2, 3, 4, 5]

l = [3 * x for x in l if 3*x > 4]

print(l)

k = [(x,x**2) for x in range(1,5)]

print(k)

p = [x for x in range(1,20) if x%3 == 0 or x%5 == 0]

print(p)

m = [(x,y) for x in range(1,20) for y in range(2,40,2) if 2* x == y]

print(m)

n = [(x,y) for x in range(1,5) if x%2 == 0
     for y in range(6,2,-1) if y%2 != 0]
print(n)

dziel = lambda x,y,z: (x+y)/z
print(dziel(3,5,2))

def albatros(x,y):
    return x+y

a = [*map(albatros,[1,2,3],range(4))]
print(a)

z = [*zip(range(1,10),"ABCDEFG")]
print("z =", z)

sam = lambda x: x.lower() in "aeiou"

f = [*filter(sam,"Ala ma kota, kot ma Ale")]
print(f)

ff = [*filter(lambda x: x % 2 == 0, range(0, 11))]
print(ff)

L = [("Adam",15), ("Bogdan",19), ("Ala",17), ("Zenobia", 14)]

SL = sorted(L, key = lambda L: L[1])

print(SL)