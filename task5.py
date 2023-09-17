def is_or_not(matrix, a):
    i = 0
    j = len(matrix) - 1
    while i < len(matrix)  and j >= 0:
        if matrix[i][j] == a:
            return('YES')
        if matrix[i][j] < a:
            i += 1
        else:
            j -= 1
    return('NO')

def printt(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()