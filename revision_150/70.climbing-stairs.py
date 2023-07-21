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

        prev1 = 1
        prev2 = 1

        for _ in range(2, n+1):
            prev1, prev2 = prev2, prev1 + prev2
            

        return prev2

        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]


        dp = {}
        def helper(index):

            if index in dp:
                return dp[index]

            if index == 0:
                return 1
            
            if index == 1:
                return 1
            
            if index < 0:
                return 0
            
            dp[index] = helper(index-1) + helper(index-2)
            return dp[index]
            

        
        return helper(n)




            



        
# @lc code=end
print(Solution().climbStairs(3))
