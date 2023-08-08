#
# @lc app=leetcode id=62 lang=python
#
# [62] Unique Paths
#

# @lc code=start
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # dp = {}
        # def rec(r, c):
        #     if (r, c) in dp:
        #         return dp[(r,c)]
            
        #     if r < 0 or c < 0:
        #         return 0

        #     if r == 0 or c == 0:
        #         return 1
            
        #     right = rec(r, c-1)
        #     bottom = rec(r-1, c)

        #     dp[(r,c)] = right + bottom
        #     return dp[(r,c)]


        # return rec(m-1, n-1) 
    
        # dp = [([1] * n) for _ in range(m+1)]
        # dp[0] = [0] * n

        # for r in range(1, m+1):
        #     for c in range(1, n):
        #         dp[r][c] = dp[r-1][c] + dp[r][c-1]

        # return dp[-1][-1]

        prev = [0] * n
        curr = [1] * n

        for _ in range(m):
            curr = [1] * n
            for i in range(1, n):        
                curr[i] = curr[i-1] + prev[i]
            prev = curr
                
        
        
        return curr[-1]

        # for r in range(1, m+1):
        #     for c in range(1, n):
        #         dp[r][c] = dp[r-1][c] + dp[r][c-1]

        # return dp[-1][-1]

        


        
# @lc code=end
print(Solution().uniquePaths(2, 2))
print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(3, 7))
print(Solution().uniquePaths(1, 1))
