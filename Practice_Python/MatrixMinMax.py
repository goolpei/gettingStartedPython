def matrix_min(matrix):
    return min(min(x) for x in matrix)

def matrix_max(matrix):
    return max(max(x) for x in matrix)

def matrix_max2(matrix):
    
    res = max(matrix[0])
    for row in matrix:
        if max(row) > res: res = max(row)
    return res


mat = [
    [  7,  53, 183, 439, 863],
    [497, 383, 563,  79, 973],
    [287,  63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303]
]

print(f"Minimum num: {matrix_min(mat)}")
print(f"Maximum num: {matrix_max2(mat)}")