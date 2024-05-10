graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 2, 'E': 4},
    'C': {'A': 2, 'F': 7},
    'D': {'B': 2},
    'E': {'B': 4, 'F': 1},
    'F': {'C': 7, 'E': 1}
}

import heapq

def dijkstra(graph, start_node):
    distances = {node: float('inf') for node in graph}  
    distances[start_node] = 0
    visited = set()
    priority_queue = [(0, start_node)]  

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

distances = dijkstra(graph, 'A')
print(distances)  
