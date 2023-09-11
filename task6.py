def sudoku(matrix, n):
    #правильная сумма чисел 1...n
    sum = 0
    for i in range(1,n * n + 1):
        sum += i

    sum1 = 0
    sum2 = 0

    vec = [[0] * n for i in range(n)]

    for i in range(n*n):
        for j in range(n*n):
            vec[i // n][j // n] += matrix[i][j]
        #сумма по строкам и столбцам
            sum1 += matrix[i][j]
            sum2 += matrix[j][i]

        if sum1 != sum or sum2 != sum:
            return('error!!!')
        else:
            sum1 = 0
            sum2 = 0

    for i in range(n):
        for j in range(n):
            if vec[i][j] != sum:
                return('error!!!')
            elif i == j and i == n -1:
                return 1

def printt(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()


