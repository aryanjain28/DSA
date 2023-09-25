#
# @lc app=leetcode id=1752 lang=python
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1

        if count == 0:
            return True
        elif count == 1:
            return nums[0] >= nums[-1]

        return False
        


        # point = -1
        # n = len(nums)
        # index = 0
        # while index < n-1:
        #     if nums[index] > nums[index+1]:
        #         point = index
        #         break
        #     index += 1


        # if point == -1:
        #     return True
        
        # nums = nums[point+1:] + nums[:point+1]
        # index = 0
        # while index < n-1:
        #     if nums[index] > nums[index+1]:
        #         return False
        #     index += 1

        # return True
        
# @lc code=end

print(Solution().check([2,1,3,4]))
print(Solution().check([3,4,5,1,2]))
print(Solution().check([1]))
print(Solution().check([1,2,3]))