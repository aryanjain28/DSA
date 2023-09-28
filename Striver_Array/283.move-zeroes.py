#
# @lc app=leetcode id=283 lang=python
#
# [283] Move Zeroes
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        firstZeroIndex = -1

        for index, n in enumerate(nums):
            if n == 0 and firstZeroIndex == -1:
                firstZeroIndex = index
            elif n != 0 and firstZeroIndex != -1:          
                nums[firstZeroIndex], nums[index] = nums[index], nums[firstZeroIndex]
                firstZeroIndex += 1
        
# @lc code=end
# print(Solution().moveZeroes([0, 1, 0, 3, 12]))
print(Solution().moveZeroes([1, 0, 1]))
