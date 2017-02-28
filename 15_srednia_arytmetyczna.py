def avg(*n):
    if len(n) == 0:
        return 0
    else:
        a = sum(n)/len(n)
        return a
print(avg(12,2321,6,23,64,23))