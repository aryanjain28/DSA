#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        i = 0
        j = len(numbers) - 1

        while True:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1, j+1]
            



        # def bin_search(n, nums):

        #     i = 0
        #     j = len(nums) - 1

        #     while i <= j:
        #         mid = (i + j) // 2
        #         if nums[mid] == n:
        #             return mid
        #         elif nums[mid] < n:
        #             i = mid + 1
        #         else:
        #             j = mid - 1

        #     return -1

        # i = 0        
        # while i < len(numbers) - 1:

        #     j = bin_search(target - numbers[i], numbers[i+1:])
        #     if j != -1:
        #         return [i+1, j+i+2]
                
        #     i += 1

        
# @lc code=end
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 3, 4], 6))
print(Solution().twoSum([-1, 0], -1))
print(Solution().twoSum([5, 25, 75], 100))

