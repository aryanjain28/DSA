#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxi = -float("inf")
        
        s = 0
        for n in nums:
            s = s + n if s >= 0 else n
            maxi = s if s > maxi else maxi
                
        return maxi

        
# @lc code=end

# print(Solution().maxSubArray([-2, 1, -3, 4]))
print(Solution().maxSubArray([-3, 4]))