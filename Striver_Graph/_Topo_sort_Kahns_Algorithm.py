def topologicalSort(adj, V):


    adjList = {}
    for node in range(V):
        adjList[node] = set()

    indegree = [0] * V

    for u, v in adj:
        adjList[u].add(v)
        indegree[v] += 1

    q = []
    for index, ind in enumerate(indegree):
        if ind == 0:
            q.append(index)
        

    res = []
    while q:
        node = q.pop(0)
        res.append(node)

        for neighbor in adjList[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return res




adj = [
    [5, 0],
    [4, 0],
    [5, 2],
    [2, 3],
    [3, 1],
    [4, 1],
]

print(topologicalSort(adj, 6))