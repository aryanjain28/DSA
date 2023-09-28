#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        return (n*(n+1) / 2) - sum(nums)
        
# @lc code=end

print(Solution().missingNumber([3, 0, 1]))