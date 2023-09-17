#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#

import heapq

# @lc code=start
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        adjList = {}
        for (u, v, wt) in times:
            if u not in adjList:
                adjList[u] = []
            adjList[u].append((v, wt))

        distance = [float("inf")] * n
        distance[k-1] = 0

        pq = [(0, k)]
        while pq:
            (d, node) = heapq.heappop(pq)

            for neighbor, wt in (adjList[node] if node in adjList else []):
                if distance[neighbor-1] > wt + d:
                    distance[neighbor-1] = wt + d
                    heapq.heappush(pq, (wt + d, neighbor))

        m = max(distance)
        return -1 if m >= float("inf") else m
            



        
# @lc code=end
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

print(Solution().networkDelayTime(times, n, k))


