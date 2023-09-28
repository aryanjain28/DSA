#
# @lc app=leetcode id=485 lang=python
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maxi = 0
        count = 0

        for n in nums:
            if n == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0


        return maxi        
# @lc code=end

