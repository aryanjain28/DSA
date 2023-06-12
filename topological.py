

def dfs(src: int, adj: dict[int: [int]], visit: set[int], topSort: list[int]):

    if src in visit:
        return

    for childNode in adj[src]:
        dfs(childNode, adj, visit, topSort)

    visit.add(src)
    topSort.append(src)


def topologicaOrder(edges: list[(int, int)], n: int):

    adjList = {i: [] for i in range(1, n+1)}
    for src, dest in edges:
        adjList[src].append(dest)

    visit = set()
    topSort = []
    for node in range(1, n+1):
        dfs(node, adjList, visit, topSort)

    topSort.reverse()
    return topSort


edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4, 6),
    (5, 6),
    (7, 8)
]
print(topologicaOrder(edges, 8))
