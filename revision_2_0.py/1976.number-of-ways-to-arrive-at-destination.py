#
# @lc app=leetcode id=1976 lang=python
#
# [1976] Number of Ways to Arrive at Destination
#

import heapq
# @lc code=start
class Solution(object):
    def countPaths(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """

        adjList = {}
        for (u, v, wt) in roads:
            if u not in adjList:
                adjList[u] = []

            if v not in adjList:
                adjList[v] = []

            adjList[u].append((v, wt))
            adjList[v].append((u, wt))

        ways = [0] * n
        ways[0] = 1

        distance = [float("inf")] * n
        distance[0] = 0

        pq = [(0, 0)]
        while pq:
            d, node = heapq.heappop(pq)


            for (neighbor, wt) in (adjList[node] if node in adjList else []):
                if distance[neighbor] >= d + wt:
                    distance[neighbor] = d + wt
                    ways[neighbor] += 1

                    if distance[neighbor] > d + wt:
                        heapq.heappush(pq, (d + wt, neighbor))

        print(ways)

        # dp = {}
        # visited = set()
        # def dfs(node, d):

        #     if (node, d) in dp:
        #         return dp[(node, d)]

        #     if node == n-1 and d == mini:
        #         return 1

        #     if node in visited or d > mini:
        #         return 0
            
        #     visited.add(node)
            
        #     count = 0
        #     for (neighbor, wt) in (adjList[node] if node in adjList else []):
        #         count += dfs(neighbor, d + wt)

        #     visited.remove(node)

        #     dp[(node, d)] = count
        #     return dp[(node, d)]
        
        # dp = []

        # return dfs(0, 0) % ((10**9) + 7)
        




        
# @lc code=end
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
print(Solution().countPaths(7, roads))
roads = [[1,0,10]]
print(Solution().countPaths(2, roads))
