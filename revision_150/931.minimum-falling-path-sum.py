#
# @lc app=leetcode id=931 lang=python
#
# [931] Minimum Falling Path Sum
#

# @lc code=start
class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        # ROWS = len(matrix)

        # dp = {}
        # def rec(r, c):

        #     if (r, c) in dp:
        #         return dp[(r, c)]
            
        #     if r < 0 or c < 0 or r >= ROWS or c >= ROWS:
        #         return float("inf")
            
        #     if r == 0:
        #         return matrix[0][c]
            
        #     left = rec(r-1, c-1)
        #     center = rec(r-1, c)
        #     right = rec(r-1, c+1)

        #     dp[(r, c)] = matrix[r][c] + min(left, center, right)
        #     return dp[(r, c)]


        # mini = float("inf")
        # for i in range(ROWS):
        #     mini = min(rec(ROWS-1, i), mini)

        # return mini

        n = len(matrix)
        matrix = [[float("inf")] + row + [float("inf")] for row in matrix]
        matrix.append([0] * (n + 2))
        
        for i in range(n-1, -1, -1):
            for j in range(n , 0, -1):
                matrix[i][j] = matrix[i][j] + min(min(matrix[i+1][j+1],matrix[i+1][j-1]), matrix[i+1][j])

        return min(*matrix[0])
        

        
# @lc code=end
Solution().minFallingPathSum([[2,1,3], [6,5,4], [7,8,9]])

