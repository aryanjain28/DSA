#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        LEN = len(nums)
        arr = [-1] * LEN

        fromIndex = 0
    
        for fromIndex in range(LEN):        
            arr[(fromIndex + k) % LEN] = nums[fromIndex]


        for i in range(LEN):
            nums[i] = arr[i]
        

# @lc code=end

# Solution().rotate([1,2,3,4,5,6,7], 3)
Solution().rotate([-1,-100,3,99], 2)
