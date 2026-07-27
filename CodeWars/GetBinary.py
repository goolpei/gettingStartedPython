def get_binary(num):  
    res = ''
    if num <= 0: return 0
    while num > 0:
    
        if num % 2 == 0:
            res += '0'
        else:
            res += '1'

        num //= 2
            
    return res[::-1]

num = 100
print(get_binary(num))

# 100 // 2 = 50 (0) remainder = 0
# 50 // 2 = 25 (0)
# 25 // 2 = 12 (1)
# 12 // 2 = 6 (0)
# 6 // 2 = 3 (0)
# 3 // 2 = 1 (1)
# 1 // 2 = 0 (1)

# 1100100