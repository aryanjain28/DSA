#
# @lc app=leetcode id=1319 lang=python
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start

class Union_Find:
    def __init__(self, n):
        self.rank = [-1] + ([0] * n)
        self.parent = [-1] + list(range(1, n+1))

    def find(self, n):

            while n != self.parent[n]:
                self.parent[n] = self.parent[self.parent[n]]
                n = self.parent[n]
            return n

        # if n == self.parent[n]:
        #     return n
        # return self.find(self.parent[n])

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return

        rank_pu, rank_pv = self.rank[pu], self.rank[pv]

        if rank_pu > rank_pv:
            self.parent[pv] = pu
        elif rank_pu < rank_pv:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1


class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        if len(connections) < n-1: return -1

        uf = Union_Find(n)
        for (u, v) in connections:
            uf.union(u, v)
                
        s = {uf.find(node) for node in uf.parent}
        return len(s) - 1





        
# @lc code=end
print(Solution().makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
print(Solution().makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(Solution().makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))
print(Solution().makeConnected(11, [[1,4],[0,3],[1,3],[3,7],[2,7],[0,1],[2,4],[3,6],[5,6],[6,7],[4,7],[0,7],[5,7]]))