#
# @lc app=leetcode id=463 lang=python
#
# [463] Island Perimeter
#

# @lc code=start
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])

        def isOutOfBoundary(i, j):
            return i < 0 or j < 0 or i == n or j == m
                

        visited = set()

        def dfs(i, j):

            if (i, j) in visited:
                return 0

            if isOutOfBoundary(i, j) or grid[i][j] == 0:
                return 1
            
            visited.add((i, j))
            
            top = dfs(i-1, j)
            bottom = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)

            return top + bottom + left + right

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)

        


        
# @lc code=end

(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))