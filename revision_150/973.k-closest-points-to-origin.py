#
# @lc app=leetcode id=973 lang=python
#
# [973] K Closest Points to Origin
#

from heapq import heappush, heappop
# @lc code=start
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        heap = []
        for (x, y) in points:
            heappush(heap, ((x**2 + y**2), (x, y)))

        res = []
        while len(res) < k:
            res.append(heappop(heap)[1])

        return res
        
# @lc code=end

