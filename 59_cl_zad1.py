A = [[0, 1, 9, 3], [7, 5, 8, 3], [9, 2, 9, 4], [4, 6, 7, 1]]


def solution(A):
    result = 0
    if len(A) > 2 or len(A[0]) > 2:
        for i, row in enumerate(A):
            for j, elem in enumerate(row):
                if j == 0 or j == len(row) - 1 or i == 0 or i == len(A) - 1:
                    continue
                elif row[j-1] < elem > row[j+1] and A[i-1][j] > elem < A[i+1][j]:
                    result += 1
                elif row[j-1] > elem < row[j+1] and A[i-1][j] < elem > A[i+1][j]:
                    result += 1
                else:
                    continue
    return result

print(solution(A))