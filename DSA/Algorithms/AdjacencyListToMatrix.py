def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]

    for node in adj_list:
        if adj_list[node]:
            for neighbor in adj_list[node]:
                adj_matrix[node][neighbor] = 1
        print(adj_matrix[node])
            
    return adj_matrix

#adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})