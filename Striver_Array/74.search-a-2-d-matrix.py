#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        m = len(matrix)
        n = len(matrix[0]) 

        i = 0
        j = (m * n) - 1

        while i <= j:

            mid = (i + j) // 2
            mid_i, mid_j = divmod(mid, n)

            if matrix[mid_i][mid_j] < target:
                i = mid + 1
            elif matrix[mid_i][mid_j] > target:
                j = mid - 1
            else:
                return True
            
        return False


        







        
# @lc code=end
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
Solution().searchMatrix(matrix, target)