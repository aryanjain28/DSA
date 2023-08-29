#
# @lc app=leetcode id=33 lang=python
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

        while i <= j:
            mid = (i + j) // 2

            if target > nums[mid]:
                if target > nums[j] and nums[i] > nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif target < nums[mid]:
                if target < nums[i] and nums[j] < nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                return mid
            
        return -1




        
# @lc code=end
# print(Solution().search([1,2,3,4,5], 1))
# print(Solution().search([4,5,1,2,3], 11))
# print(Solution().search([4,5,6,7,8,1,2,3], 8))
print(Solution().search([4,5,6,7,0,1,2], 0))
