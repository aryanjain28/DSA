#
# @lc app=leetcode id=200 lang=python
#
# [200] Number of Islands
#

# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        ROW = len(grid)
        COL = len(grid[0])

        def isOutOfBounds(r, c):
            return r < 0 or r >= ROW or c < 0 or c >= COL
                

        def dfs(r, c):
            if isOutOfBounds(r, c) or grid[r][c] != "1":
                return False
            
            # current node is 1
            grid[r][c] = "#"

            top = dfs(r-1, c)
            bottom = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)
        
            return top or bottom or left or right




        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1

        return count
            
        
        
# @lc code=end

Solution().numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
