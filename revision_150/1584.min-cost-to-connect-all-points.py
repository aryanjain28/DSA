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

        def distance(p1_index, p2_index):
            p1, p2 = points[p1_index], points[p2_index]
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    
        src_index = 0
        visited = set()
        visited.add(src_index)

        heap = []
        for point_index in range(1, len(points)):
            heapq.heappush(heap, (distance(src_index, point_index), src_index, point_index))

        mst = 0
        while heap:
            (wt, point_1, point_2) = heapq.heappop(heap)
            
            if point_2 in visited:
                continue

            mst += wt
            visited.add(point_2)

            for point_index in range(len(points)):
                if point_index not in visited:
                    heapq.heappush(heap, (distance(point_2, point_index), point_2, point_index))
        

        # print(mst)
        return mst


        
# @lc code=end
Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]])
