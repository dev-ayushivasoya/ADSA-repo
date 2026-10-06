def floyd_warshall(graph):
  
    n = len(graph)
    
    dist = [list(row) for row in graph]
    
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist



if __name__ == "__main__":
    
    INF = float('inf')
  
    example_graph = [
        [0,   3,   INF, 7],
        [8,   0,   2,   INF],
        [5,   INF, 0,   1],
        [2,   INF, INF, 0]
    ]
    
    print("Initial Adjacency Matrix:")
    for row in example_graph:
        print([x if x != INF else "INF" for x in row])
        
  
    shortest_paths = floyd_warshall(example_graph)
    
    print("\nFinal Shortest Distance Matrix:")
    for row in shortest_paths:
        print([x if x != INF else "INF" for x in row])
