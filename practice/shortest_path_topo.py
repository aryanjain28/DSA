

# 1. find topo sort [DFS or Kahn's]
# 2. Use that topo stack to find shortest distance

def topo_sort_bfs(adjList, nodes):
    
    indegree = [0] * nodes
    for node in range(nodes):
        for (neighbor, _) in adjList[node]:
            indegree[neighbor] += 1

    q = []
    for node, degree in enumerate(indegree):
        if degree == 0:
            q.append(node)

    res = []
    while q:
        node = q.pop()
        res.append(node)

        for neighbor, _ in adjList[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return res


def topo_sort_dfs(adjList, nodes):

    visited = set()
    stack = []

    def dfs(node):
        if node in visited: return
        visited.add(node)

        for (neighbor, _) in adjList[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in range(nodes):
        if node not in visited:
            dfs(node)

    return stack[::-1]

def shortestPath(edges, nodes, src):

    # create adjList 
    adjList = { n: [] for n in range(nodes) }
    for (u, v, wt) in edges:
        adjList[u].append((v, wt))

    distance = [float("inf")] * nodes
    distance[src] = 0

    stack = topo_sort_dfs(adjList, nodes)
    while stack:
        node = stack.pop(0)
        for neighbor, wt in adjList[node]:
            if distance[neighbor] > distance[node] + wt:
                distance[neighbor] = distance[node] + wt

    return distance





edges = [[0,4,2],[0,5,3],[5,4,1],[4,6,3],[4,2,1],[6,1,2],[2,3,3],[1,3,1]]
nodes = 7
src = 0
shortestPath(edges, nodes, src)