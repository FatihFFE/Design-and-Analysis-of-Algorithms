def count_connected_components(graph):
    def dfs(node, visited):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)

    visited_nodes = set()
    connected_components_count = 0

    for node in graph:
        if node not in visited_nodes:
            dfs(node, visited_nodes)
            connected_components_count += 1
            
    return connected_components_count

# Example usage:
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3],
    6: [7],
    7: [6]
}

print(count_connected_components(graph))
