#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        i = 0
        j = len(nums) - 1

        min_index = -1
        minimum = float("inf")

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] < minimum:
                minimum = min(minimum, nums[mid])
                min_index = mid

            if nums[mid] < nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        if target == minimum:
            return min_index
        
        if target > nums[-1]:
            i = 0
            j = min_index - 1
        else:
            i = min_index 
            j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid - 1
            else:
                i = mid + 1

        return -1
        
# @lc code=end

# print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1,3], 3))