#
# @lc app=leetcode id=695 lang=python
#
# [695] Max Area of Island
#

# @lc code=start
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROW = len(grid)
        COL = len(grid[0])
        
        def isOutOfBounds(r, c):
            return r < 0 or r >= ROW or c < 0 or c >= COL

        def dfs(r, c):

            if isOutOfBounds(r, c) or grid[r][c] < 1:
                return 0
            
            val = grid[r][c]
            grid[r][c] = -1
            
            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)
            
            return val + top + bottom + left + right


        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area


        
# @lc code=end

Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])