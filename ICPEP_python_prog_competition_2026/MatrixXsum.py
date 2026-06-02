# matrix X sum
n = int(input("Enter matrix N: ")) # N*N

mat = []
X_sum = 0
print("Enter matrix elements: ")
for i in range(n):
    temp = list(map(int, input().split()))
    while len(temp) != n:
        print(f"Invalid. Input row {i + 1} again.")
        temp = list(map(int, input().split()))
    mat.append(temp)
    X_sum += mat[i][i] + mat[i][n - 1 - i]

if n % 2 != 0:
    X_sum -= mat[(n - 1) // 2][(n - 1) // 2]    

print(f"Matrix X Sum: {X_sum}")