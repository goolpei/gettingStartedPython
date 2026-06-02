
def nb_dig(n, d):
    
    d = str(d)
    count_d = 0
    for i in range(0, n + 1):
        s = i * i
        count_d += str(s).count(d)
    
    return count_d

print(nb_dig(25, 1))