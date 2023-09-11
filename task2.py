#Дан невозрастающий массив из 𝑁 элементов. Найти количество различных чисел среди
#элементов этого массива:
#a. Для любых элементов
#. Если известно, что все элементы массива – числа от 1 до 𝑘

def counter(vec):
    tmp = set()
    for el in vec:
        tmp.add(el)
    return(len(tmp))

def counter_alt(vec):
    repeat = 0
    for i in range(1, len(vec)):
        if vec[i] == vec[i-1]:
            repeat += 1
    return(len(vec) - repeat)