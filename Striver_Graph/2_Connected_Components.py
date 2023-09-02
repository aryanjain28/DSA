from typing import List



class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [-1] + list(range(1, n+1))
        self.rank = [-1] + [0] * n

    def find(self, u):
        if self.parent[u] == u:
            return self.parent[u]
        return self.find(self.parent[u])

    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)

        if p1 != p2:

            if self.rank[p1] > self.rank[p2]:
                self.parent[v] = p1

            elif self.rank[p1] < self.rank[p2]:
                self.parent[u] = p2
            
            else:
                self.parent[v] = p1
                self.rank[p1] += 1

        
class Node:
    def __init__(self) -> None:
        self.val = -1
        self.neighbors = []

def findNumOfProvinces(roads: List[List[int]], n: int) -> int:

    uf = UnionFind()

    for n1 in range(1, n+1):
        for n2 in range(1, n+1):
            if n1 != n2 and roads[n1-1][n2-1] == 1:
                uf.union(n1, n2)

    return len(set(uf.parent))


    


roads = [
    [1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
]


def getIntArr(string):
    return list(map(int, string.split(" ")))


strs = ["1 0 0 1 0 1 0 0 1 0",
"0 1 0 0 1 1 1 0 0 1",
"0 0 1 0 1 1 0 0 0 0",
"1 0 0 1 1 1 0 1 0 0",
"0 1 1 1 1 0 1 1 0 0",
"1 1 1 1 0 1 1 0 1 0",
"0 1 0 0 1 1 1 0 0 0",
"0 0 0 1 1 0 0 1 1 0",
"1 0 0 0 0 1 0 1 1 1",
"0 1 0 0 0 0 0 0 1 1",
]

roads = []

for s in strs:
    roads.append(getIntArr(s))

# print(roads)

findNumOfProvinces(roads, len(roads))