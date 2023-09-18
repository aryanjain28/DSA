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


        distance = [float("inf")] * n
        distance[0] = 0

        ways = [0] * n
        ways[0] = 1

        pq = [(0,0)]
        while pq:
            d, node = heapq.heappop(pq)
        
            for (neighbor, wt) in ([] if node not in adjList else adjList[node]):
                
                if distance[neighbor] >= wt + d:
                    if distance[neighbor] > wt + d:
                        heapq.heappush(pq, (d + wt, neighbor))
                        distance[neighbor] = wt + d
                        ways[neighbor] = ways[node]
                        continue
                
                    ways[neighbor] += ways[node]
                    
        return ways[n - 1] % (10**9 + 7)




        
# @lc code=end
n = 7 
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]

Solution().countPaths(n, roads)
