mark_type_list = ["1", "2", "3", "4", "5", "6"]
mark_list = []
i = "1"

while i:
    i = input()
    if i in mark_type_list:
         mark_list.append(i)
    else:
        continue
lol = []

for j in mark_list:
    if type(j) is str:
        j = int(j)
        lol.append(j)
mark_list = lol

s = sum(mark_list)
n = len(mark_list)
if n != 0:
    result = s / n
    print(result)