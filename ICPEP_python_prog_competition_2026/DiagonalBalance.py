n = int(input("Enter row and col: "))
matrix = []
print("Enter the grid:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    
main_sum = 0
anti_sum = 0
for i in range(n):
    main_sum += matrix[i][i]
    anti_sum += matrix[i][n - 1 - i]
    
if main_sum == anti_sum:
    print("-1 -1")
    exit()
    
for r in range(n):
    on_main = matrix[r][r]
    on_anti = matrix[r][n - 1 - r]
    
    new_main = main_sum - (2 * on_main)
    new_anti = anti_sum - (2 * on_anti)
    
    if new_main ==  new_anti:
        print(f"R {r}")
        exit()
        
for c in range(n):
    on_main = matrix[c][c]
    on_anti = matrix[n - 1 - c][c]
    
    new_main = main_sum - (2 * on_main)
    new_anti = anti_sum - (2 * on_anti)
    
    if new_main == new_anti:
        print(f"C {c}")
        exit()
        
print("IMPOSSIBLE")