#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        i = 0
        j = len(nums)-1
        k = 0

        while i <= j and k >= i and  k <= j:

            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i += 1
                k += 1
            elif nums[k] == 2:
                nums[j], nums[k] = nums[k], nums[j]
                j -= 1
            else:
                k += 1



        # freq = {}
        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1

        # index = 0
        # for N in set(nums):
        #     for n in range(freq[N]):
        #         nums[index] = N
        #         index += 1

        
        
# @lc code=end
Solution().sortColors([2,0,2,1,1,0])
