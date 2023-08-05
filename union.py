class Union_Find:
    def __init__(self, n):
        self.rank = [-1] + ([0] * n)
        self.parent = [-1] + list(range(1, n+1))

    def find(self, n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        rank_pu, rank_pv = self.rank[pu], self.rank[pv]

        if rank_pu > rank_pv:
            self.parent[v] = pu
        elif rank_pu < rank_pv:
            self.parent[u] = pv
        else:
            self.parent[v] = pu
            self.rank[pu] += 1

    def isConnected(self, u, v):
        return self.parent[u] == self.parent[v]


def print_helper(uf_):
    print(uf_.parent[1:])
    print(uf_.rank[1:])
    print()


uf = Union_Find(3)
print_helper(uf)

uf.union(1, 2)
print_helper(uf)

uf.union(2, 3)
print_helper(uf)


# uf = Union_Find(5)
# print_helper(uf)

# uf.union(1, 2)
# print_helper(uf)

# uf.union(3, 4)
# print_helper(uf)

# uf.union(4, 5)
# print_helper(uf)

# uf.union(2, 5)
# print_helper(uf)
