#
# @lc app=leetcode id=1334 lang=python
#
# [1334] Find the City With the Smallest Number of Neighbors at a Threshold Distance
#

# @lc code=start
class Solution(object):
    def findTheCity(self, nodes, edges, t):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """


        cost_matrix = [[float("inf")]* nodes for _ in range(nodes)]

        for (u, v, wt) in edges:
            cost_matrix[u][v] = wt
            cost_matrix[v][u] = wt

        for n in range(nodes):
            cost_matrix[n][n] = 0

        for via in range(nodes):
            for i in range(nodes):
                if i == via: continue
                for j in range(nodes):
                    if i == j or j == via: continue
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][via] + cost_matrix[via][j])


        node = None
        mini = float("inf")
        for i in range(nodes):
            count = 0
            for j in range(nodes):
                if i != j and cost_matrix[i][j] <= t:
                    count += 1
            
            if count <= mini:
                mini = count
                node = i

        return node
                    

        


        
# # @lc code=end
# print(Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
# print(Solution().findTheCity(6, [[0,1,10],[0,2,1],[2,3,1],[1,3,1],[1,4,1],[4,5,10]], 20))

print(Solution().findTheCity(
    5,
    [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],
    2
))