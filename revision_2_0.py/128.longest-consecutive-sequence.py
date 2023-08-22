#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        starters = []
        for n in nums:
            if n-1 not in nums_set:
                starters.append(n)

        maxi = 0
        for starter in starters:
            n = starter
            count = 0
            while n in nums_set:
                count += 1
                n += 1
            
            maxi = max(count, maxi)

        return maxi

        
# @lc code=end
Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
