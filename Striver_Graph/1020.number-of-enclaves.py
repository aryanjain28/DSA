#
# @lc app=leetcode id=1020 lang=python
#
# [1020] Number of Enclaves
#

# @lc code=start
class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        m = len(grid[0])
        

        def inOutOfBoundary(i, j):
            if i < 0 or j < 0 or i == n or j == m:
                return True
            
        def dfs(i, j):

            if inOutOfBoundary(i, j) or grid[i][j] == 0:
                return
            
            grid[i][j] = 0
    
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(m):
            dfs(0, i)
            dfs(n-1, i)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

    
        count = 0
        for i in range(n):
            for j in range(m):
                count = count + (1 if grid[i][j] == 1 else 0)

        return count
        






        
# @lc code=end

print(Solution().numEnclaves([[0], [1], [1], [0], [0]]))
print(Solution().numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(Solution().numEnclaves([[0,1,1,0],[0,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(Solution().numEnclaves([[1,0,0],[1,1,1],[1,0,0]]))

print(Solution().numEnclaves(
[
    [0,0,0,1,1,1,0,1,0,0],
    [1,1,0,0,0,1,0,1,1,1],
    [0,0,0,1,1,1,0,1,0,0],
    [0,1,1,0,0,0,1,0,1,0],
    [0,1,1,1,1,1,0,0,1,0],
    [0,0,1,0,1,1,1,1,0,1],
    [0,1,1,0,0,0,1,1,1,1],
    [0,0,1,0,0,1,0,1,0,1],
    [1,0,1,0,1,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,1]
]
))