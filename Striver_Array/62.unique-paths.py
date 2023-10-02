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

        def isOutOfBounds(i, j):
            return i < 0 or j < 0 or i >= m or j >= n

        mMap = {}

        def dfs(r, c):

            if (r, c) in mMap:
                return mMap[(r, c)]

            if isOutOfBounds(r, c):
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            
            right = dfs(r, c+1)
            bottom = dfs(r+1, c)

            mMap[(r, c)] = right + bottom
            return mMap[(r, c)]
        
        # return dfs(0, 0)
    
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[1][1] = 1


        for i in range(1, m+1):
            for j in range(1, n+1):
                right = dp[i][j-1]
                bottom = dp[i-1][j]
                dp[i][j] = max(right + bottom, dp[i][j])

        return dp[-1][-1]
    


        
        
# @lc code=end

print(Solution().uniquePaths(3, 7))