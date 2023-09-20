from heapq import heappop, heappush


class UnionFind:

    def __init__(self, nodes) -> None:
        self.parent = [-1] + nodes

    def find(self, x):
        if x == self.parent[x]:
            return x
        return self.find(self.parent[x])

    def union(self, v1, v2):
        self.parent[self.find(v2)] = self.find(v1)


# Kruskal's uses union find datastructure

def minimumSpanningTree(edges, n):
    uf = UnionFind(list(range(1, n+1)))

    minHeap = []
    for (n1, n2, wt) in edges:
        heappush(minHeap, (wt, n1, n2))

    mst = []
    mst_sum = 0
    while minHeap:
        wt, n1, n2 = heappop(minHeap)

        if uf.find(n1) == uf.find(n2):
            continue

        uf.union(n1, n2)
        mst.append((n1, n2))
        mst_sum += wt

    print(mst_sum)
    print(mst)


edges = [
    [1, 2, 10],
    [1, 3, 8],
    [2, 4, 4],
    [2, 3, 4],
    [3, 4, 4],
    [3, 5, 4],
    [4, 5, 2],
]
minimumSpanningTree(edges, 5)
