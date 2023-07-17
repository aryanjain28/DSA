#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#


from collections import Counter
# @lc code=start
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        """

        return len(set(nums)) != len(nums)

        # nums_s = set()
        # for n in nums:
        #     if n in nums_s:
        #         return True

        #     nums_s.add(n)

        # return False



        
# @lc code=end
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([3,3]))

