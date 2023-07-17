import heapq


def minSpanningTree(edges, n):

    mSet = set()
    for src, dest, wt in edges:
        mSet.add(src)
        mSet.add(dest)

    adj = {}
    for c in mSet:
        adj[c] = []

    for src, dest, wt in edges:
        adj[src].append((dest, wt))
        adj[dest].append((src, wt))

    minHeap = []
    for node, wt in adj['A']:
        heapq.heappush(minHeap, (wt, 'A', node))

    visited = set()
    visited.add("A")
    mst = []
    mst_val = 0
    while minHeap:

        cost, src, dest = heapq.heappop(minHeap)

        if dest in visited:
            continue

        visited.add(dest)
        mst.append((src, dest))
        mst_val += cost

        for child, c in adj[dest]:
            if child not in visited:
                heapq.heappush(minHeap, (c, dest, child))

    print("ORDER: ", mst)
    print("COST: ", mst_val)
    return mst


minSpanningTree(
    [
        ('A', 'B', 3),
        ('A', 'D', 6),
        ('A', 'E', 9),
        ('B', 'C', 2),
        ('B', 'D', 4),
        ('B', 'E', 9),
        ('B', 'F', 9),
        ('C', 'D', 2),
        ('C', 'F', 8),
        ('C', 'G', 9),
        ('D', 'G', 9),
        ('E', 'F', 8),
        ('E', 'J', 18),
        ('F', 'G', 7),
        ('F', 'I', 9),
        ('F', 'J', 10),
        ('G', 'H', 4),
        ('G', 'I', 5),
        ('I', 'H', 1),
        ('I', 'J', 3),
        ('H', 'J', 4)],
    10
)
