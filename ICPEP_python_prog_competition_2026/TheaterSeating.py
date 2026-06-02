# TheaterSeating
row, col = map(int, input("Enter number of rows and columns: ").split())
mat = [[0 for x in range(col)] for y in range(row)]

for i in range(row):
    r, start_c, end_c = map(int, input(f"Enter request number {i + 1}: ").split()) # row, starting col, end col
    if (-1 < start_c <= end_c < col and -1 < r < row and sum(mat[r][start_c:end_c + 1]) == 0):
        print(f"Request {i + 1}: BOOKED")
        mat[r][start_c:end_c + 1] = [1 for x in range(start_c, end_c + 1)]
    else:
        print(f"Request {i + 1}: INVALID")

count = sum([sum(r) for r in mat])
print("Seating arrangement: ")
mat = [[str(co) for co in ro] for ro in mat]
for r in mat:
    print(' '.join(r))
print(f"Total goers: {count}")