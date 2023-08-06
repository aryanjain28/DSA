
from heapq import heappush, heappop


class UnionFind:

    def __init__(self, n):
        self.parent = [-1] + (list(range(1, n+1)))

    def find(self, node):
        if node == self.parent[node]:
            return node
        return self.find(self.parent[node])

    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return False

        self.parent[parent_v] = parent_u
        return True


def minimum_spanning_tree(edges, n):

    uf = UnionFind(n)

    heap = []
    for (src, dest, wt) in edges:
        heappush(heap, (wt, src, dest))

    res = []
    while heap:
        (wt, src, dest) = heappop(heap)
        if uf.union(src, dest):
            res.append((src, dest, wt))

    print(res)
    return res


edges = [
    [1, 2, 10],
    [1, 3, 8],
    [2, 4, 4],
    [2, 3, 4],
    [3, 4, 4],
    [3, 5, 4],
    [4, 5, 2],
]
n = 5

minimum_spanning_tree(edges, n)


# edges = [
#     ["A", "C", 3],
#     ["A", "B", 10],
#     ["C", "B", 4],
#     ["C", "D", 4],
#     ["C", "E", 4],
#     ["B", "D", 1],
#     ["D", "E", 2]
# ]

# n = 3


# minimum_spanning_tree(edges, n)
