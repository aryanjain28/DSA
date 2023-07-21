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

        maximum = 0
        mSet = set(nums)
        for n in mSet:
            curr = 1
            if n - 1 not in mSet:
                i = n + 1
                while i in mSet:
                    curr += 1
                    i += 1
            maximum = curr if curr > maximum else maximum

        return maximum






        
# @lc code=end
Solution().longestConsecutive([100, 4, 200, 3, 2, 1])
Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])

