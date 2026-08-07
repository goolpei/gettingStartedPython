# implemented using depth-first search algorithm
def dfs(adj_matrix, node):
    # should return a list of nodes which are reachable from a given node.
    stack = [node]
    visited = {node}
    
    while stack:
        current_node = stack.pop()
        for n, neighbor in enumerate(adj_matrix[current_node]):
            if neighbor and (n not in visited):
                stack.append(n)
                visited.add(n)

    return list(visited)

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))

    
            