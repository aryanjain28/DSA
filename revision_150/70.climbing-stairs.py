#
# @lc app=leetcode id=70 lang=python
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        prev2 = 1

        for _ in range(2, n+1):
            prev, prev2 = prev2 + prev, prev

        return prev


        
# @lc code=end
print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))
