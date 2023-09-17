def fib1(n): #O(n)
    vec = [0 for i in range(n + 1)]
    if n != 0:
        vec[1] = 1
    for i in range(2, n + 1):
        vec[i] = vec[i - 1] + vec[i - 2]
    return vec[n]

def fib_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fib_recursive(n - 1) + fib_recursive(n - 2))

def fib_matrix(n):
    if n == 0: return 0
    if n == 1: return 1
    ind = 1
    a = 1
    b = 0
    begin_condition = [[1, 1], [1, 0]]
    while ind < n:
        tmp = a
        a = tmp * begin_condition[0][0] + b * begin_condition[0][1]
        b = tmp * begin_condition[1][0] + b * begin_condition[1][1]
        ind += 1
    return a
