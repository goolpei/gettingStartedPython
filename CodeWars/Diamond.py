def diamond(n):
    if n <= 0 or n % 2 == 0: return None  
    
    # n * n size diamond
    res = ""
    
    k = n // 2
    mid = (n // 2) + 1
    j = 1
    l = n
    for i in range(n):
        if i < mid:
            res += (' ' *   k  ) + ('*' * (i + 1)) + ('*' * i) + '\n'
            #print((' ' *   k  ) + ('*' * (i + 1)) + ('*' * i))
            k -= 1
        else:
            l -= 2
            res += (' ' * j ) + ('*' * l) + '\n'
            #print((' ' * j ) + ('*' * l) + '\n')
            j += 1
    return res
    


print(diamond(21))