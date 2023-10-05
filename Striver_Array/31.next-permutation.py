#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#

import math
# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # find break point
        index = len(nums)-2
        while index >= 0 and nums[index] >= nums[index+1]:
            index -= 1
        
        if index < 0:
            nums.reverse()
            return

        # print(nums)
        # print(index)

        maxi = float("inf")
        maxi_index = None
        for i, n in enumerate(nums[index+1:]):            
            if nums[index] < n < maxi:
                maxi = n
                maxi_index = index + 1 + i

        # print(maxi)
        # print(maxi_index)
        

        nums[index], nums[maxi_index] = nums[maxi_index], nums[index]

        # print(nums)

        s = sorted(nums[index+1:])
        j = 0
        for i in range(index+1, len(nums)):
            nums[i] = s[j]
            j += 1

        

        


# @lc code=end

# print(Solution().nextPermutation([1,2,3]))
# print(Solution().nextPermutation([2,3,1]))
# print(Solution().nextPermutation([3,1,2]))
print(Solution().nextPermutation([3,2,1]))
# print(Solution().nextPermutation([1,1,5]))
# print(Solution().nextPermutation([1,2,4,3]))