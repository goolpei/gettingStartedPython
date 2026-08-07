from typing import List
def generate_matrix(n: int) -> List[List[int]]: 
    # returns an n*n (row, column) matrix
    result = []
    for i in range(n):
        result.append([(i, j) for j in range(n)])

    return result

m = generate_matrix(5)
for i in m:
    print(i)

