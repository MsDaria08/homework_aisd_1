def without_one(vec):
    res = [1 for i in range(len(vec))]
    tmp = 1
    for i in range(1, len(vec)):
        tmp *= vec[i - 1]
        res[i] = tmp
    tmp = 1
    for i in range(len(vec) - 2, -1, -1):
        tmp *= vec[i + 1]
        res[i] *= tmp
    return res