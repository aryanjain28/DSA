#
# @lc app=leetcode id=733 lang=python
#
# [733] Flood Fill
#

# @lc code=start
class Solution(object):
    def floodFill(self, grid, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        n = len(grid)
        m = len(grid[0])

        def isOutOfB(i, j):
            return i < 0 or j < 0 or i == n or j == m

        visited = set()

        def dfs(i, j, parent):
            
            if isOutOfB(i, j) or (i, j) in visited or grid[i][j] != parent: 
                return
            
            visited.add((i, j))

            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(i+x, j+y, parent)

            grid[i][j] = color

        dfs(sr, sc, grid[sr][sc])
        return grid

        
# @lc code=end
Solution().floodFill([[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
