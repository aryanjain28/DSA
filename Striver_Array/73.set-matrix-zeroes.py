#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])

        print(m ,n )

        def dfs(r, c):
            
            for i in range(n):
                if matrix[r][i] != 0:
                    matrix[r][i] = "#"

            for i in range(m):
                if matrix[i][c] != 0:
                    matrix[i][c] = "#"

            matrix[r][c] = "#"

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dfs(i, j)


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0


# @lc code=end

Solution().setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])
Solution().setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])