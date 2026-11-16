
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def dfs(node, target, visited):
    if node in visited:
        return False

    print(node, end=" ")
    visited.append(node)

    if node == target:
        print("\nTarget Found!")
        return True

    for neighbour in graph[node]:
        if dfs(neighbour, target, visited):
            return True

    return False

visited = []
if not dfs('A', 'E', visited):
    print("\nTarget Not Found!")
