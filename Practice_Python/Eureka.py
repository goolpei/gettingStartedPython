def isEureka(n):
    num_len = len(str(n))
    sum = 0
    for i, num in enumerate(str(n), start = 1):
        num = int(num)
        sum += num ** i
    return True if sum == n else False
    

def sum_dig_pow(a, b):
    res = []
    
    for num in range(a, b + 1):
        if isEureka(num):
            res.append(num)
    return res
    

print(isEureka(135))