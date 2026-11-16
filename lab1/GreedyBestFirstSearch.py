
graph = {
    'A': ['B', 'F'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D', 'I', 'J'],
    'F': ['A', 'G', 'H'],
    'G': ['F', 'I'],
    'H': ['F', 'I'],
    'I': ['E', 'G', 'H', 'J'],
    'J': ['E', 'I']
}

h = {
    'A': 10, 'B': 8, 'C': 5,
    'D': 7, 'E': 3, 'F': 6,
    'G': 5, 'H': 3, 'I': 1,
    'J': 0
}

edge_cost = {
    ('A', 'B'): 6,
    ('A', 'F'): 3,
    ('B', 'C'): 3,
    ('B', 'D'): 2,
    ('C', 'D'): 1,
    ('C', 'E'): 5,
    ('D', 'E'): 8,
    ('E', 'I'): 5,
    ('E', 'J'): 5,
    ('F', 'G'): 1,
    ('F', 'H'): 7,
    ('G', 'I'): 3,
    ('H', 'I'): 2,
    ('I', 'J'): 3
}

def get_edge_cost(node, neighbor):
    return edge_cost.get(
        (node, neighbor),
        edge_cost.get((neighbor, node))
    )

def greedy(graph, start, goal):
    visited = []
    queue = [start]
    cost = {start: 0}

    while queue:
        node = min(queue, key=lambda x: h[x])
        queue.remove(node)

        if node not in visited:
            print(node, end=" ")
            visited.append(node)

            if node == goal:
                print("\nTotal Cost:", cost[node])
                break

            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in cost:
                    cost[neighbor] = (
                        cost[node] + get_edge_cost(node, neighbor)
                    )
                    queue.append(neighbor)

print("Greedy Search:")
greedy(graph, 'A', 'H')
