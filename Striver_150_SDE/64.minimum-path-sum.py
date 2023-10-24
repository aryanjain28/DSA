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

        m = len(grid)
        n = len(grid[0])

        def isOutOfBoundary(row, col):
            return (row < 0 or col < 0 or row >= m or col >= n)
                

        dp = {}
        def dfs(row, col):

            if (row, col) in dp:
                return dp[(row, col)]
            
            if isOutOfBoundary(row, col):
                return float("inf")

            right = dfs(row, col + 1)
            down = dfs(row + 1, col) 

            mini = min(right, down)
            ans = (0 if mini >= float("inf") else mini) + grid[row][col]

            dp[(row, col)] = ans
            return dp[(row, col)]


        res = dfs(0, 0)
        # print(dp)
        return res
        
# @lc code=end

grid = [[1,3,1],[1,5,1],[4,2,1]]
# grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid))
