def matrix_sum(matrix):
    return sum(sum(row) for row in matrix)

mat = [
    [  7,  53, 183, 439, 863],
    [497, 383, 563,  79, 973],
    [287,  63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303]
]
# row, col = list(map(int, input('Enter row and column: ').split()))

# for k in range(row):
#     print(f'Enter row {k + 1} elements:', end=' ')
#     col_nums = list(map(int, input().split()))
#     mat.append(col_nums)

# for i in mat:
#     print(i)

print(f"Matrix sum: {matrix_sum(mat)}")
