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

        mMap = {}
        for index, n in enumerate(nums):
            toFind = target - n
            if toFind in mMap:
                return [mMap[toFind], index]
            
            mMap[n] = index
        
# @lc code=end

