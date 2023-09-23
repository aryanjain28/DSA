#
# @lc app=leetcode id=1905 lang=python
#
# [1905] Count Sub Islands
#

# @lc code=start
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """

        r, c = len(grid1), len(grid1[0])

        def isOutofBounds(i, j):
            return i < 0 or j < 0 or i >= r or j >= c

        def dfs(i, j, grid1, grid2):
            
            if isOutofBounds(i, j) or grid2[i][j] != 1:
                return True
            
            if grid1[i][j] != 1:
                return False
            
            val = grid2[i][j]
            grid2[i][j] = "#"

            top = dfs(i-1, j, grid1, grid2)
            bottom = dfs(i+1, j, grid1, grid2)
            left = dfs(i, j-1, grid1, grid2)
            right = dfs(i, j+1, grid1, grid2)
            
            return top and bottom and left and right
            

        n = 0
        for i in range(r):
            for j in range(c):
                if grid1[i][j] == 1 and grid2[i][j] == 1 and dfs(i, j, grid1, grid2):
                    n += 1
        
        return n

        
# @lc code=end

grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
print(Solution().countSubIslands(grid1, grid2))

grid1 = [[1,1,1,1,0,0],[1,1,0,1,0,0],[1,0,0,1,1,1],[1,1,1,0,0,1],[1,1,1,1,1,0],[1,0,1,0,1,0],[0,1,1,1,0,1],[1,0,0,0,1,1],[1,0,0,0,1,0],[1,1,1,1,1,0]]
grid2 = [[1,1,1,1,0,1],[0,0,1,0,1,0],[1,1,1,1,1,1],[0,1,1,1,1,1],[1,1,1,0,1,0],[0,1,1,1,1,1],[1,1,0,1,1,1],[1,0,0,1,0,1],[1,1,1,1,1,1],[1,0,0,1,0,0]]
print(Solution().countSubIslands(grid1, grid2))