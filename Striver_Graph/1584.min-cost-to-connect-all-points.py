#
# @lc app=leetcode id=1584 lang=python
#
# [1584] Min Cost to Connect All Points
#


import heapq
# @lc code=start
class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def d(index1, index2):
            (x1, y1) = points[index1]
            (x2, y2) = points[index2]

            return abs(x1 - x2) + abs(y1 - y2)

        # using prims 

        sum_ = 0
        pq = []
        for i, point in enumerate(points[1:]):
            heapq.heappush(pq, (d(0, i+1), 0, i+1))

        visited = set()
        visited.add(0)

        while pq:
            wt, src, dest =  heapq.heappop(pq)
            if dest in visited: continue

            visited.add(dest)
            sum_ += wt

            for i in range(len(points)):
                if i != dest and i not in visited:
                    heapq.heappush(pq, (d(dest, i), dest, i))
                    


        return sum_






        
# @lc code=end
Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
