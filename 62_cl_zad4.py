A = [2, -4, 6, -3, 9]


def solution(A):
    res = None
    for i in range(1, len(A)+1):
        for j in range(len(A)):
            temp = abs(sum(A[j:j+i]))
            if res == None or temp < res:
                res = temp
    return res

print(solution(A))