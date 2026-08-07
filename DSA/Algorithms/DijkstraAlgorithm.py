import heapq

def find_shortest_path(adj_matrix, start_node, target_node = None):
    INF = float('inf')
    n = len(adj_matrix)

    distances = [INF] * n
    distances[start_node] = 0
    previous = [None] * n
    visited = set()