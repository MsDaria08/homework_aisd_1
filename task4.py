def skipped_num(vec):
    sum = 0
    for i in range(len(vec)):
        sum = sum + i - vec[i]
    return(sum + len(vec))