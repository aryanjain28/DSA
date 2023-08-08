#
# @lc app=leetcode id=213 lang=python
#
# [213] House Robber II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        def rec(nums, index):
            if index in dp:
                return dp[index]
            
            if index < 0:
                return 0
            
            left = nums[index] + rec(nums, index-2)
            right = 0 + rec(nums, index-1)

            dp[index] = max(left, right)
            return dp[index]
        

        n = len(nums)
        if n <= 3:
            if n == 1:
                return nums[0]
            return max(*nums)


        dp = {}
        left = rec(nums[1:], n-2)
        dp = {}
        right = rec(nums[:-1], n-2)

        # return max(left, right )
    
        def tab(nums):
            n = len(nums)
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])
            curr = None

            for index in range(2, n):
            
                curr = max(nums[index] + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return curr


        return max(tab(nums[:-1]), tab(nums[1:]))



        
# @lc code=end
# print(Solution().rob([1,2,3]))
# print(Solution().rob([1]))

