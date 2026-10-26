def hamiltonian(graph, path, pos, n):
    if pos == n:
        return graph[path[pos - 1]][path[0]] == 1

    for v in range(1, n):
        if v not in path and graph[path[pos - 1]][v] == 1:
            path[pos] = v

            if hamiltonian(graph, path, pos + 1, n):
                return True

            path[pos] = -1

    return False


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

n = len(graph)
path = [0] * n
path[0] = 0

if hamiltonian(graph, path, 1, n):
    print("Hamiltonian Cycle:")
    print([v + 1 for v in path] + [1])
else:
    print("No Hamiltonian Cycle")
