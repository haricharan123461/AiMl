
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start, target):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == target:
                print("\nTarget Found!")
                return

            queue.extend(graph[node])

    print("\nTarget Not Found!")

bfs('A', 'E')
