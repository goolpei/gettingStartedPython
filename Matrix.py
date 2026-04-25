# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in mat:
#     print(row)

# rows, cols = 3, 3

# mat = [[0] * cols for _ in range(rows)]

# for row in mat:
#     print(row)

# grid = [[0] * 3] * 3

# for row in grid:
#     for val in row:
#         print(val, end=' ')
#     print()

# print()

# grid[0][0] = 5

# for row in grid:
#     for val in row:
#         print(val, end=' ')
#     print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        print(f'Value at ({i}, {j}) is {matrix[i][j]}')


transposed = [list(row) for row in zip(*matrix) ]

flat = [val for row in matrix for val in row]

for row in transposed:
    print(row)

print(flat)