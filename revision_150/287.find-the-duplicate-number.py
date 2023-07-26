#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        """

        slow, fast = 0, 0
        
        slow = nums[slow]
        fast = nums[nums[fast]]

        # cycle detection
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Floyd's Algorithm
        curr = 0
        while slow != curr:            
            curr = nums[curr]
            slow = nums[slow]

        return slow


        
Solution().findDuplicate([1,3,4,2,2])


        
        
        
# @lc code=end

