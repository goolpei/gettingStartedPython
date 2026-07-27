def matrixfy(name):  
    matrix = []
    l = len(name)
    if l == 0: return "name must be at least one letter"
    n = 0
    while n * n < l:
        n += 1
    
    p = n * n - l
    name += '.' * p

    k = 0
    for _ in range(n):
        temp = []
        for _ in range(n):
            temp.append(name[k])
            k += 1
        matrix.append(temp)

    return matrix

def matrixfy2(name):
    matrix = []
    l = len(name)
    if l == 0: return "name must be at least one letter"
    n = 0
    while n * n < l:
        n += 1
    
    p = n * n - l
    name += '.' * p
    l = len(name)

    for i in range(0, l, n):
        matrix.append(list(name[i : i + n]))

    return matrix

print(matrixfy2('jsees'))