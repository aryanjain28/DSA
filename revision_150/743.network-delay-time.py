#
# @lc app=leetcode id=743 lang=python
#
# [743] Network Delay Time
#



import heapq
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] + list(range(1, n+1))

    def find(self, n):
        if self.parent[n] == n:
            return n
        return self.find(self.parent[n])
    
    def union(self, u, v):
        parent_u, parent_v = self.parent[u], self.parent[v]
        if parent_u == parent_v:
            return False
        self.parent[v] = parent_u
        return True

# @lc code=start

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """

        mMap = {}
        for node in range(1, n+1):
            mMap[node] = []

        for (src, dest, wt) in times:
            mMap[src].append((wt, dest))
        
        heap = []
        for (wt, dest) in mMap[k]:
            heapq.heappush(heap, (wt, k, dest))

        visited = set()
        visited.add(k)


        res = []
        while heap:
            (wt, src, dest) = heapq.heappop(heap)

            if dest in visited:
                continue

            print(wt, src, "->", dest)

            visited.add(dest)
            res.append(wt)

            for (cost, node) in mMap[dest]:
                if node not in visited:
                    heapq.heappush(heap, (cost+wt, dest, node))


        print(res)



        
# @lc code=end
Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)

