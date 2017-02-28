from time import sleep
from math import ceil
from random import shuffle

def choinka():
    n = int(input("How many rows? "))
    __christmas_tree(n)

def __christmas_tree(n):
    total = sum([2 * i + 1 for i in range(n)])
    # print(total)
    stars_num = int(total * 0.7)
    v_num = int(ceil(total * 0.1))
    o_num = int(ceil(total * 0.1))
    i_num = total - stars_num - v_num - o_num

    chars = stars_num * "*" + v_num * "V" + o_num * "O" + i_num * "i"
    char_list = [i for i in chars]
    shuffle(char_list)
    # print(char_list)

    for i in range(n):
        print("".join(char_list[0:(2 * i + 1)]).center(2 * n + 1))
        del char_list[0:(2 * i + 1)]
    print("***".center(2 * n + 1))
    print("***".center(2 * n + 1))
    print("")
    print("Balls: %3i Pct: %6.2f" % (o_num, (100 * o_num) / total))
    print("Cones: %3i Pct: %6.2f" % (v_num, (100 * v_num) / total))
    print("Candl: %3i Pct: %6.2f" % (i_num, (100 * i_num) / total))
    print("Stars: %3i Pct: %6.2f" % (stars_num, (100 * stars_num) / total))
    print("Total: %3i Pct: %6.2f" % (total, (100 * total) / total))
if __name__ == "__main__":
    choinka()
