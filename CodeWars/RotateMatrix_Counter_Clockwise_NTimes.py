def rotate_against_clockwise(matrix, times):
    
    n = len(matrix[0])
    
    times = times % 4  
    if times == 0: return matrix
    
    for _ in range(times):
        res = []
        j = 0
        for i in range(n - 1, -1, -1):
            temp = []
            for row in matrix:
                temp.append(row[i])
            res.append(temp)
            j += 1
        matrix = res[::]
    
    return res