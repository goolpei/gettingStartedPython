def calc_diaNantiDia_sum(m):
    n = len(m)
    k = len(m) - 1
    main_dia_sum = 0
    anti_dia_sum = 0
    for i, j in enumerate(range(n)):
        main_dia_sum += m[i][j]
        anti_dia_sum += m[i][k]
        k -= 1
    return main_dia_sum == anti_dia_sum
def negateRow(m, row):
    y = m[::]
    y[row] = [-n for n in y[row]]
    return y
def negateCol(m, col):
    y = m[::]
    for row in y:
        row[col] = -row[col]
    return y
    
row_col = int(input("Enter row and col: "))
mat = []
print("Enter the grid: ")
for n in range(row_col):
    temp = list(map(int, input().split()))
    mat.append(temp)
 
if calc_diaNantiDia_sum(mat):
    print("-1 -1")
else:
    found = False
    for tries_row in range(row_col):
        temp = negateRow(mat, tries_row)
        if calc_diaNantiDia_sum(temp):
            print(f"R {tries_row}")
            found = True
            break
    if not found:
        for tries_col in range(row_col):
            temp = negateCol(mat, tries_col)
            if calc_diaNantiDia_sum(temp):
                print(f"C {tries_col}")
                found = True
                break
        if not found:
            print("IMPOSSIBLE") 
