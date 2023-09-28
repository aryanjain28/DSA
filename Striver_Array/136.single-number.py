#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        index = 1
        while index < len(nums):
            nums[index] ^= nums[index-1] 
            index += 1

        return nums[-1]
        
# @lc code=end

Solution().singleNumber([4,1,2,1,2])