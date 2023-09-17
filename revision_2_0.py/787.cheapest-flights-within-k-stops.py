#
# @lc app=leetcode id=787 lang=python
#
# [787] Cheapest Flights Within K Stops
#

# @lc code=start

import heapq

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """

        adjList = {}
        for (u, v, wt) in flights:
            if u not in adjList:
                adjList[u] = []

            adjList[u].append((v, wt))

        distance = [float("inf")] * n
        distance[src] = 0

        k += 1

        pq = [(-k, 0, src)]
        while pq:
            # print(pq)
            (k, d, node) = heapq.heappop(pq)            

            if k == 0: 
                continue
            
            for (neighbor, wt) in (adjList[node] if node in adjList else []):
                if distance[neighbor] > wt + d:
                    distance[neighbor] = wt + d
                    heapq.heappush(pq, (k + 1, d + wt, neighbor))

        # print(distance)
        if distance[dst] >= float("inf"):
            return -1
        return distance[dst]


        
# @lc code=end
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]] 
src = 0
dst = 3 
k = 1

# n = 3
# flights = [[0,1,2],[1,2,1],[2,0,10]]
# src = 1
# dst = 2 
# k = 1

# n = 5
# flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
# src = 0
# dst = 2
# k = 2

print(Solution().findCheapestPrice(n, flights, src, dst, k))



