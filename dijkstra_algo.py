def dijkstra_no_heap(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    

    unvisited = set(graph.keys())
    
    while unvisited:
        
        current_node = None
        for node in unvisited:
            if current_node is None:
                current_node = node
            elif distances[node] < distances[current_node]:
                current_node = node
                
        
        if distances[current_node] == float('inf'):
            break
            
     
        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    
    return distances


graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {},
    'E': {'D': 1}
}

shortest_distances = dijkstra_no_heap(graph, 'A')
print("Shortest distances from 'A':", shortest_distances)
