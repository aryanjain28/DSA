from heapq import heappop, heappush


def minimum_spanning_tree(edges, n):

    mMap = {}
    for (src, dest, wt) in edges:
        if src not in mMap:
            mMap[src] = []
        mMap[src].append((dest, wt))

        if dest not in mMap:
            mMap[dest] = []
        mMap[dest].append((src, wt))

    src = "A"
    heap = []
    for (node, wt) in mMap[src]:
        heappush(heap, (wt, src, node))

    visited = set()
    visited.add(src)

    res = []
    while heap:
        (wt, src, dest) = heappop(heap)

        if dest in visited:
            continue

        visited.add(dest)
        res.append((src, dest, wt))

        for (neighbor, wt) in mMap[dest]:
            if neighbor not in visited:
                heappush(heap, (wt, dest, neighbor))

    cost = 0
    for (_, _, wt) in res:
        cost += wt

    print(res, cost)


edges = [["A", "B", 10], ["B", "C", 12], ["C", "A", 13]]
n = 3

edges = [
    ["A", "C", 3],
    ["A", "B", 10],
    ["C", "B", 4],
    ["C", "D", 4],
    ["C", "E", 4],
    ["B", "D", 1],
    ["D", "E", 2]
]

n = 3

minimum_spanning_tree(edges, n)
