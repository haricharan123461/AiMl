
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

visited = []
dfs(graph, 'A', visited)
