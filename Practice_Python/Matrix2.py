
def inputMatrix(matrix, rows, cols):
    for i in range(rows):
        row = []
        for j in range(cols):
            print(f'Enter element ({i}, {j}):', end=' ')
            num = int(input())
            row.append(num)
        matrix.append(row)
    return matrix


def inputMatrix2(matrix, rows, cols):
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} elements: ").split()))
        matrix.append(row)

def inputMatrix3(matrix, rows, cols):
    pass

rows, cols = map(int, input("Enter number of rows and columns: ").split())

matrix = []

inputMatrix2(matrix, rows, cols)

for row in matrix:
    print(row)