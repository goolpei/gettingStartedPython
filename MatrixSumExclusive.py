def matrix_sum(matrix: list[list[int]]) -> int:
    
    n = len(matrix)
    sums = []
    started_index = []

    for k in range(n):
        seen_rows = []
        seen_cols = []
        num_collection = []
        started_index_collection = []
        for i in range(n):
            
            for j in range(n):
                if i not in seen_rows and j not in seen_cols and [i, j] not in started_index:
                    seen_rows.append(i)
                    seen_cols.append(j)
                    started_index_collection.append([i, j])
                    num_collection.append(matrix[i][j])
                
        sums.append(sum(num_collection))
        started_index.append(started_index_collection[0])

    return max(sums)


matrix = [
            [ 5, 9, 11],
            [ 7, 2,  8],
            [10, 3,  7]
        ]

print(matrix_sum(matrix))