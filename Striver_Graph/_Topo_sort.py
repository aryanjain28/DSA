def topologicalSort(adj, V, E):
    # Write your code here

    adjList = {}
    for n in range(V):
        adjList[n] = set()

    for u, v in adj:
        adjList[u].add(v)


    visited = set()
    stack = []

    def dfs(node):
        
        if node in visited:
            return

        visited.add(node)

        for neighbor in adjList[node]:
            if neighbor not in visited: 
                dfs(neighbor)

        stack.append(node)


    for node in range(V):
        if node not in visited:
            dfs(node)

    return stack[::-1]




adj = [
    [0,2],
    [1,2],
    [3,1],
    [0,4],
]

print(topologicalSort(adj, 5, 4))