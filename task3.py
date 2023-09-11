from math import ceil
def sum_with_factorial(n):
    res = 0
    tmp = 1
    for i in range(1, n + 1):
        tmp *= i
        res += 1 / tmp
    return ceil(res * 100) / 100.0