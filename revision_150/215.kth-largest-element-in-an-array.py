#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

from heapq import heappop, heappush
# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = []
        for n in nums:
            heappush(heap, -n)

        for _ in range(k-1):
            heappop(heap)

        return -heappop(heap)

        
# @lc code=end

