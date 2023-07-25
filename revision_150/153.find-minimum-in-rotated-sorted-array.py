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
        j = len(nums) - 1

        mini = float("inf")

        while i <= j:
            mid = (i + j) // 2

            mini = min(mini, nums[mid])

            if nums[mid] < nums[j]:
                j = mid - 1
            else:
                i = mid + 1

        return mini




# @lc code=end
print(Solution().findMin([2,3,4,5,1]))
print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([4,5,1,2,3]))
print(Solution().findMin([5,1,2,3,4]))
