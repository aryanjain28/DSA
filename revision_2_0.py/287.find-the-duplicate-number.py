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

        slowPointer = 0
        fastPointer = 0

        slowPointer = nums[slowPointer]
        fastPointer = nums[nums[fastPointer]]

        while slowPointer != fastPointer:
            slowPointer = nums[slowPointer]
            fastPointer = nums[nums[fastPointer]]


        curr = 0
        while curr != slowPointer:
            curr = nums[curr]
            slowPointer = nums[slowPointer]

        return slowPointer



        
# @lc code=end

print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))