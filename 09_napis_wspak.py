t = input()
for i in t.split():
    l = list(i)
    l.reverse()
    print(''.join(l), end=" ")