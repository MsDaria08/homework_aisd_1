def is_or_not(matrix, a):
    n = 5
    i = n // 2
    ind = 1
    if a == matrix[i][i]:
        return ('YES')
    if a < matrix[i][i]:
        ind = - 1

    while i >= 0 and i < n - 1:
            i = i + ind
            if a == matrix[i][i]:
                return ('YES')
                #print(a)
                break
            if a > matrix[i][i]:
                for k in range(i, n):
                    if a <= matrix[k][i] or a <= matrix[i][k]:
                        #print(str(matrix[k][i]) + ' ' + str(matrix[i][k]))
                        if k == n-1 and not(matrix[k][i] == a or matrix[i][k] == a):
                            continue
                        if matrix[k][i] == a or matrix[i][k] == a:
                            return('YES')
                            #print(a)
                            #break
            if a < matrix[i][i]:
                for k in range(i, -1, -1):
                    if a <= matrix[k][i] or a <= matrix[i][k]:
                        #print(str(matrix[k][i]) + ' ' + str(matrix[i][k]))
                        if k == 0 and not (matrix[k][i] == a or matrix[i][k] == a):
                            continue
                        if matrix[k][i] == a or matrix[i][k] == a:
                            return('NO')
                            #print(a)
                            #break

def printt(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()