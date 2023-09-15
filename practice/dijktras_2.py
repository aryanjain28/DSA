

import heapq 

def dijkstras_algorithm(graph, src):

    n = len(graph)

    # Create adjList
    adjList = {}
    for node in range(n):
        for neighbor in range(n):
            if node != neighbor and graph[node][neighbor] != 0:
                if node not in adjList:
                    adjList[node] = []

                adjList[node].append((neighbor, graph[node][neighbor]))


    distance = [float("inf")] * n
    distance[src] = 0

    pq = [(0, src)] # (wt, node)

    while pq:
        d, node = heapq.heappop(pq)

        for neighbor, wt in adjList[node]:
            if distance[neighbor] > d + wt:
                distance[neighbor] = d + wt
                heapq.heappush(pq, (d + wt, neighbor))

    return distance



graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]
src = 0

dijkstras_algorithm(graph, src)