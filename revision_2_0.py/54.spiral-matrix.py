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

        res = []
        
        left = 0
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)

        ROW = 0
        COL = -1

        start = left
        end = right

        while True:

            i = start
            while i < end:

                if ROW < 0:
                    res.append(matrix[i][COL])
                else:
                    res.append(matrix[i][ROW])
                
                i += 1


            if ROW > 0:
                start = 
                end = 
                right -= 1
                ROW = -1
            else:
                COL = -1
            
            pass

        return res




# @lc code=end
# Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
