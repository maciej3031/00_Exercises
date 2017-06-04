A = [[5, 4, 4], [4, 3, 4], [3, 2, 4], [2, 2, 2], [3, 3, 4], [1, 4, 4], [4, 1, 1]]


def solution(A):
    res = 0
    for i, row in enumerate(A):
        for j, elem in enumerate(row):
            if i == 0 and j == 0:
                res += 1
            elif j == 0 and A[i-1][j] != elem:
                res += 1
            elif i == 0 and row[j-1] != elem:
                res += 1
            elif j != 0 and i != 0:
                if row[j-1] != elem and A[i-1][j] != elem:
                    res += 1
                elif row[j-1] == elem and A[i-1][j] == elem:
                    res -= 1

    return res

print(solution(A))