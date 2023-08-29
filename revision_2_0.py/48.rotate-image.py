#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]

        for i in range(n):
            for j in range(n):
                if i < j:
                    matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]


        


        
# @lc code=end

Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])