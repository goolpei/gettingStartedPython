def upper_triangular(mat):
    
    n = len(mat)
    k = n - 2
    for row in mat[n-1:0:-1]:
        for num in row[:k + 1]:
            if num != 0: return False
        k -= 1
    return True

m = [[1, 1, 1], 
     [0, 1, 1], 
     [0, 0, 1]]
  
m2 = [[0, 0, 1], 
      [0, 1, 1], 
      [1, 1, 1]]

for row in m2:
    print(row[::-1])
