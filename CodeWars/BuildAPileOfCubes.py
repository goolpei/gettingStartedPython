def find_nb(sum_c):
    sum = 0   
    count = 0
    
    while True:
        if sum == sum_c:
            return count
        if sum > sum_c:
            return -1
        count += 1
        sum = sum + count ** 3