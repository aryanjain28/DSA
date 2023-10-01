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

        n = len(nums)
        s = 0
        maxi = -float("inf")

        for n in nums:
            if s >= 0:
                s += n
            else:
                s = n

            maxi = max(maxi, s)

        return maxi
        
        # i = 0
        # maxi = -float("inf")

        # while i < n:    
        #     s = nums[i]
        #     maxi = max(s, maxi)

        #     j = i + 1
        #     while j < n:
        #         s += nums[j]
        #         maxi = max(s, maxi)
        #         j += 1
        #     i += 1

        # return maxi



        
# @lc code=end

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([1]))