#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])
        
        # dp = {}
        # def rec(r, c):
        #     if (r, c) in dp:
        #         return dp[(r, c)]
            
        #     if r < 0 or c < 0:
        #         return float("inf")
            
        #     if r == 0 and c == 0:
        #         return grid[r][c]
            
        #     right = rec(r, c-1)
        #     bottom = rec(r-1, c)

        #     dp[(r, c)] = grid[r][c] + min(right, bottom)
        #     return dp[(r, c)]

        # return rec(ROWS-1, COLS-1)

        # dp = [[float("inf")] * (COLS + 1) for _ in range(ROWS+1)]
        # dp[0][1] = 0


        # for i in range(1, ROWS+1):
        #     for j in range(1, COLS+1):
        #         dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        # return dp[-1][-1]

        prev = [float("inf")] * (COLS + 1)
        curr = [float("inf")] * (COLS + 1)
        prev[1] = 0

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                curr[j] = min(curr[j-1], prev[j]) + grid[i-1][j-1]
            prev = curr

        return prev[-1]



        


        
# @lc code=end

print(Solution().minPathSum([[1,3,1], [1,5,1], [4,2,1]]))
print(Solution().minPathSum([[1,2,3], [4,5,6]]))
print(Solution().minPathSum([[2,3], [4,5]]))