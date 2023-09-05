

#
# @lc app=leetcode id=547 lang=python
#
# [547] Number of Provinces
#

# @lc code=start

class UnionFind:
    def __init__(self, n):
        self.parent =  [-1] + list(range(1, n+1))

    def find(self, n):
        if self.parent[n] == n:
            return n 
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]
        
    
    def union(self, u, v):
        p1, p2 = self.find(u), self.find(v)
        if p1 != p2:
            self.parent[p2] = p1


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        adjMat = {i: set() for i in range(1, n+1) }

        for n1 in range(1, n+1):
            for n2 in range(1, n+1):
                if n1 != n2 and isConnected[n1-1][n2-1] == 1:
                    if n1 not in adjMat:
                        adjMat[n1] = set()
                    adjMat[n1].add(n2)

                    if n2 not in adjMat:
                        adjMat[n2] = set()
                    adjMat[n2].add(n1)
        

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)

            for n in adjMat[node]:
                if n not in visited:
                    dfs(n)


        visited = set()
        count = 0

        for node in range(1, n+1):
            if node not in visited:
                dfs(node)
                count += 1


        return count

        # n = len(isConnected)
        # uf = UnionFind(n)

        # for n1 in range(1, n+1):
        #     for n2 in range(1, n+1):
        #         if isConnected[n1-1][n2-1] == 1:
        #             uf.union(n1, n2)


        # return len(set([uf.find(i) for i in range(1, n+1)]))

    
        
# @lc code=end
print(Solution().findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
print(Solution().findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))
print(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))