def prims_algorithm(graph):

    n = len(graph)
    selected = [False] * n
    mst_edges = []
    total_cost = 0

    selected[0] = True  

    for _ in range(n - 1):
        min_edge = (None, None, float('inf'))

        
        for u in range(n):
            if selected[u]:
                for v in range(n):
                    if not selected[v] and graph[u][v] != 0:
                        if graph[u][v] < min_edge[2]:
                            min_edge = (u, v, graph[u][v])

        u, v, weight = min_edge
        mst_edges.append((u, v, weight))
        total_cost += weight
        selected[v] = True

    return mst_edges, total_cost


graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst, cost = prims_algorithm(graph)
print("MST edges:", mst)
print("Total cost:", cost)
