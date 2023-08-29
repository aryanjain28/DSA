#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_s = set()
        for n in nums:
            if n in nums_s:
                return True
            nums_s.add(n)
            
        return False
        
# @lc code=end

