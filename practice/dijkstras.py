import heapq


def shortestPath(edges, n, src):

    mMap = {}
    for (s, d, wt) in edges:
        if s not in mMap:
            mMap[s] = set()

        mMap[s].add((d, wt))

    total = 0
    index = 0
    heap = [(0, src)]
    while index < n:
        distance, node = heapq.heappop(heap)
        print(distance)

        if node in mMap:
            for (neighbor, cost) in mMap[node]:
                heapq.heappush(heap, (distance + cost, neighbor))

        index += 1

    print(total)


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
