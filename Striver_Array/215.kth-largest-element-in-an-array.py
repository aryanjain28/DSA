#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

import heapq

# @lc code=start
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = []
        for n in nums:
            heapq.heappush(res, -n)


        while k > 0:
            if len(res) == 0:
                return -1
            
            n = heapq.heappop(res)
            k -= 1

        # print(n)
        return -n
      



        
# @lc code=end
Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20)
Solution().findKthLargest(nums = [3,2,3,1,2,4,5,5,6], k = 9)
Solution().findKthLargest(nums = [3,2,1,5,6,4], k = 2)
