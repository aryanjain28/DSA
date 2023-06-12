import heapq


def minSpanningTree(edges, n):
    adj = {}
    for i in range(1, n+1):
        adj[i] = []

    for src, dest, wt in edges:
        adj[src].append((dest, wt))
        adj[dest].append((src, wt))

    minHeap = []
    for node, wt in adj[1]:
        heapq.heappush(minHeap, (wt, 1, node))

    visited = set()
    visited.add(1)
    mst = []
    while minHeap:

        _, src, dest = heapq.heappop(minHeap)

        if dest in visited:
            continue

        visited.add(dest)
        mst.append((src, dest))

        for child, c in adj[dest]:
            if child not in visited:
                heapq.heappush(minHeap, (c, dest, child))

    print(mst)
    return mst


minSpanningTree([[1, 2, 10], [1, 3, 3], [2, 3, 4], [2, 4, 1],
                [3, 4, 4], [3, 5, 4], [4, 5, 2]], 5)
