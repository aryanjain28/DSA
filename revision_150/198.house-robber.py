#
# @lc app=leetcode id=198 lang=python
#
# [198] House Robber
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        if n <= 2:
            if n == 2:
                return max(*nums)
            return nums[0]
                
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        curr = None

        for i in range(2, n):
            curr = nums[i] + prev2 if nums[i] + prev2 > prev1 else prev1
            prev2, prev1 = prev1, curr

        return curr

        

        
# @lc code=end
print(Solution().rob([1,2,3,1]))
# print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([2,1,1,2]))
