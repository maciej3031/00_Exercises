import random
random.seed()

list = []
while len(list) < 6:
    a = random.randint(1,49)
    if a not in list:
        list.append(a)
    else:
        continue
list.sort()
print(list)
