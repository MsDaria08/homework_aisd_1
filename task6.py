def sudoku(matrix, n):
    #правильная сумма и произведение чисел 1...n
    sum = 0
    mult = 1
    for i in range(1, n * n + 1):
        sum += i
        mult *= i

    sum1 = 0
    sum2 = 0
    mult1 = 1
    mult2 = 1

    vec = [[0] * n for i in range(n)]
    vec_mult = [[1] * n for i in range(n)]

    for i in range(n*n):
        for j in range(n*n):
            vec[i // n][j // n] += matrix[i][j]
            vec_mult[i // n][j // n] *= matrix[i][j]
            sum1 += matrix[i][j]
            sum2 += matrix[j][i]
            mult1 *= matrix[i][j]
            mult2 *= matrix[j][i]

        if sum1 != sum or sum2 != sum or mult1 != mult or mult2 != mult:
            return('error!!!')
        else:
            sum1 = 0
            sum2 = 0
            mult1 = 1
            mult2 = 1

    for i in range(n):
        for j in range(n):
            if vec[i][j] != sum or vec_mult[i][j] != mult:
                return('error!!!')
            elif i == j and i == n - 1:
                return 1

def printt(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


