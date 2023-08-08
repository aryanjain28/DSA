#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start

class Union_find:
    def __init__(self, n):
        self.rank = [-1] + ([0] * n)
        self.parent = [-1] + list(range(1, n+1))
        
    def find(self, n):
        if n == self.parent[n]:
            return n
        self.parent[n] = self.find(self.parent[n]) # path compression
        return self.parent[n]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

    def isConnected(self, u, v):
        return self.find(u) == self.find(v)


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        uf = Union_find(len(edges))
        for (e1, e2) in edges:
            if not uf.isConnected(e1, e2):
                uf.union(e1, e2)
                continue

            return [e1, e2]
        








        
# @lc code=end
print(Solution().findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]]))
# print(Solution().findRedundantConnection([[1,2],[1,3],[2,3],[2,4],[4,3]]))
# print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
# print(Solution().findRedundantConnection([[2,7],[7,8],[3,6],[2,5],[6,8],[4,8],[2,8],[1,8],[7,10],[3,9]]))
# print(Solution().findRedundantConnection([[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]))