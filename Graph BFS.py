graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start_node):
    visited = set()  
    queue = [start_node]  

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)


bfs(graph, 'A')  
