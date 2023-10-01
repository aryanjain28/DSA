#
# @lc app=leetcode id=2149 lang=python
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        

        pos = []
        neg = []

        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)


        n = len(nums)

        nums = []
        index = 0
        while index < n // 2:
            nums.append(pos[index])
            nums.append(neg[index])
            index += 1

        
        return nums


        
# @lc code=end

Solution().rearrangeArray([3, 1, -2, -5, 2, -4])