#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        n = len(matrix[0])

        top = 0
        bottom = m-1

        right = n-1
        left = 0
    
        res = []
        while len(res) < m * n:

            i = top            
            for j in range(left, right+1):
                res.append(matrix[i][j])
            top += 1


            j = right
            for i in range(top, bottom+1):
                res.append(matrix[i][j])
            right -= 1


            i = bottom
            for j in range(right, left-1, -1):
                res.append(matrix[i][j])
            bottom -= 1


            j = left
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][j])
            left += 1

        return res[:m*n]
        


            
            





        
# @lc code=end
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Solution().spiralOrder(matrix)
