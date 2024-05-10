graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def dfs(graph, start_node):
    visited = set()  
    stack = [start_node]  

    while stack:
        node = stack.pop()  
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            neighbors = graph[node]
            for neighbor in reversed(neighbors):  
                if neighbor not in visited:
                    stack.append(neighbor)

dfs(graph, 'A')  
