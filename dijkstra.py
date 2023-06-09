from heapq import heapify, heappop, heappush


def shortestPath(edges, n, src):

    adjList = {i: [] for i in range(1, n+1)}
    for s, d, w in edges:
        if s not in adjList:
            adjList[s] = []
        adjList[s].append((d, w))

    shortest = {}
    shortestArr = [-1] * n
    minHeap = [(0, src)]

    while minHeap:
        nWeight, node = heappop(minHeap)

        if node not in shortest or shortestArr[node-1] == -1:
            shortest[node] = nWeight
            shortestArr[node-1] = nWeight
            for child, w in adjList[node]:
                heappush(minHeap, (w+nWeight, child))

    print(shortestArr)
    print(shortest)

    return shortest


edges = [
    (1, 2, 10),
    (1, 3, 3),
    (2, 4, 2),
    (3, 2, 4),
    (3, 4, 8),
    (3, 5, 2),
    (4, 5, 5),
]

n = 5

src = 1

shortestPath(edges, n, src)
