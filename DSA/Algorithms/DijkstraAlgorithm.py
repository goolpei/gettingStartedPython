import heapq

def find_shortest_path(graph, start_node, target_node = None):

    # graph is an adjacency list representation

    INF = float('inf')
    n = len(graph)

    distances = {node: INF for node in graph}
    distances[start_node] = 0

    previous_nodes = {node: None for node in graph}
    visited = set()

    min_heap = [(0, start_node)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        if current_node == target_node:
            break

        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(min_heap, (new_distance, neighbor))

    path = []
    if target_node is not None:
        curr = target_node
        if distances[target_node] != INF:
            while curr is not None:
                path.append(curr)
                curr = previous_nodes[curr]
            path.reverse()
        else:
            path = None

    return distances, path

test_graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 1)],
    'C': [('A', 5), ('D', 1)],
    'D': [('B', 1), ('C', 1)]
}

print(find_shortest_path(test_graph, 'A'))