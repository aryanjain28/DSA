#
# @lc app=leetcode id=26 lang=python
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        

        # last_index = 0
        # index = 0
        # while index < len(nums):
        #     if index == 0 or nums[index-1] != nums[index]:
        #         nums[last_index] = nums[index]
        #         last_index += 1

        #     index += 1

        # return last_index
        
# @lc code=end

Solution().removeDuplicates([1,1,2])
Solution().removeDuplicates([1,2,3])
Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])