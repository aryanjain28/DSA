#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = len(nums)-1

        while i <= j:
            if i + 1 == j:
                return nums[i] if nums[i] < nums[j] else nums[j]

            first = nums[i]
            last = nums[j]

            mid = (i + j) // 2

            if first > last: 
                if first < nums[mid]:
                    i = mid                    
                else:
                    j = mid
            else:                
                j = mid - 1

        return nums[mid]





        
# @lc code=end
print(Solution().findMin(nums = [5,1,2]))
print(Solution().findMin(nums = [3,4,5,1,2]))
print(Solution().findMin(nums = [4,5,1,2,3]))
print(Solution().findMin(nums = [1,2,3]))
print(Solution().findMin(nums = [2,3,4,5,1]))

