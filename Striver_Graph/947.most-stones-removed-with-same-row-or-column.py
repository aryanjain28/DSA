#
# @lc app=leetcode id=947 lang=python
#
# [947] Most Stones Removed with Same Row or Column
#

# @lc code=start

class UnionFind:

    def __init__(self):
        self.parent = {}

    def find(self, n):
        if n not in self.parent:
           self.parent[n] = n 
        
        if n == self.parent[n]:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        self.parent[pv] = pu

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """

        uf = UnionFind()
        for i, j in stones:
            uf.union(i, ~j)

        for key, val in uf.parent.items():
            uf.parent[key] = uf.find(val)

        return len(stones) - len(set(uf.parent.values()))




        
# @lc code=end
Solution().removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])
