#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashMap = {}
        for index, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [index, hashMap[diff]]            
            hashMap[n] = index


        
# @lc code=end

