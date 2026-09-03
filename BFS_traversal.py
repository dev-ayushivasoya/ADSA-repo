def bfs(graph, start):
    visited = []      
    queue=[]
    queue.append(start)
    visited.append(start)
    
    front = 0  

    while front < len(queue):
        node = queue[front]
        front += 1
        print(node, end=" ")

    
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

    print()  
graph = {
    'D': ['B', 'F'],
    'B': ['D', 'A', 'C'],
    'F': ['D', 'E'],
    'A': ['B'],
    'C': ['B', 'E'],
    'E': ['F', 'C']
}

print("BFS Traversal starting from 'D':")
bfs(graph, 'D')
