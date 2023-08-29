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

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:

                    matrix[i][j] = "#"

                    # row
                    for c in range(len(matrix[0])):
                        if matrix[i][c] != 0:
                            matrix[i][c] = "#"

                    # col
                    for r in range(len(matrix)):
                        if matrix[r][j] != 0:
                            matrix[r][j] = "#"

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "#":
                    matrix[i][j] = 0

        


                    


        
# @lc code=end
Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
