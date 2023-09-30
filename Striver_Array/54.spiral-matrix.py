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

        res = []

        def iterate(min_row, max_row, min_col, max_col):
            temp = []
            for i in range(min_row, max_row + 1, (-1 if min_row > max_row else 1)):
                for j in range(min_col, max_col + 1, (-1 if min_col > max_col else 1)):
                    temp.append(matrix[i][j])

            return temp


        direction = 0
        while len(res) < m * n:

            d = direction % n
            if d == 0:
                min_row, max_row = 
                min_col, max_col = 
            elif d == 1:
                min_row, max_row = min_row + 1, 
                min_col, max_col = 
            elif d == 2:
                pass
            else:
                pass



            
            res.extend(iterate(min_row, max_row, min_col, max_col))

            direction += 1

        



        
# @lc code=end
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Solution().spiralOrder(matrix)
