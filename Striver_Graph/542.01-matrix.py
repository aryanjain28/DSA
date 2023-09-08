#
# @lc app=leetcode id=542 lang=python
#
# [542] 01 Matrix
#

# @lc code=start
class Solution(object):
    def updateMatrix(self, grid):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """

        m = len(grid)
        n = len(grid[0])

        def isOutOfBoundary(i, j):
            return i < 0 or j < 0 or i == m or j == n

        q = []    

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                else:
                    grid[i][j] = float("inf")

        
        while q:
            (i, j) = q.pop(0)

            for (x_dir, y_dir) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = i + x_dir
                nc = j + y_dir

                if not (isOutOfBoundary(nr, nc) or grid[nr][nc] == 0) and grid[nr][nc] > grid[i][j] + 1:
                    grid[nr][nc] = grid[i][j] + 1
                    q.append((nr, nc))


        return grid


        # visited = set()
        # def dfs(i, j):

        #     if isOutOfBoundary(i, j) or (i, j) in visited:
        #         return float("inf")
            
        #     if mat[i][j] == 0:
        #         return 0
            
        #     visited.add((i, j))
            
        #     top = dfs(i-1, j)
        #     bottom = dfs(i+1, j)
        #     left = dfs(i, j-1)
        #     right = dfs(i, j+1)

        #     visited.remove((i, j))

        #     mini = 1 + min(top, bottom, left, right)
        #     # mat[i][j] = 1 + mini
        #     return mini

        # for i in range(m):
        #     for j in range(n):
        #         if mat[i][j] > 0:
        #             mat[i][j] = dfs(i, j)
                    
        #             # print()
        #             # print(i,j)
        #             # for mt in mat:
        #             #     print(mt)
                    
        
        # return mat


# @lc code=end
# Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
Solution().updateMatrix([[0],[0],[0],[0],[0]])


# a = Solution().updateMatrix([
#     [1,0,1,1,0,0,1,0,0,1],
#     [0,1,1,0,1,0,1,0,1,1],
#     [0,0,1,0,1,0,0,1,0,0],
#     [1,0,1,0,1,1,1,1,1,1],
#     [0,1,0,1,1,0,0,0,0,1],
#     [0,0,1,0,1,1,1,0,1,0],
#     [0,1,0,1,0,1,0,0,1,1],
#     [1,0,0,0,1,1,1,1,0,1],
#     [1,1,1,1,1,1,1,0,1,0],
#     [1,1,1,1,0,1,0,0,1,1]
# ])

# for a in a:
#     print(a)

# print()


[
    [1,0,1,1,0,0,1,0,0,1],
    [0,1,1,0,1,0,1,0,1,1],
    [0,0,1,0,1,0,0,1,0,0],
    [1,0,1,0,1,1,1,1,1,1],
    [0,1,0,1,1,0,0,0,0,1],
    [0,0,1,0,1,1,1,0,1,0],
    [0,1,0,1,0,1,0,0,1,1],
    [1,0,0,0,1,3,1,1,0,1],
    [2,1,1,1,1,2,1,0,1,0],
    [3,4,2,1,0,1,0,0,1,1]
]

[
    [1,0,1,1,0,0,1,0,0,1],
    [0,1,1,0,1,0,1,0,1,1],
    [0,0,1,0,1,0,0,1,0,0],
    [1,0,1,0,1,1,1,1,1,1],
    [0,1,0,1,1,0,0,0,0,1],
    [0,0,1,0,1,1,1,0,1,0],
    [0,1,0,1,0,1,0,0,1,1],
    [1,0,0,0,1,2,1,1,0,1],
    [2,1,1,1,1,2,1,0,1,0],
    [3,2,2,1,0,1,0,0,1,1]
]
