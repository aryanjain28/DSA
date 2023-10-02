#
# @lc app=leetcode id=118 lang=python
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1], [1, 1]]

        res = [[1], [1, 1]]
        for rowNumber in range(3, numRows+1):
            temp = [1] * rowNumber
            for index in range(1, rowNumber-1):
                temp[index] = res[rowNumber-2][index-1] + res[rowNumber-2][index]

            res.append(temp)

        return res
                


        
# @lc code=end
Solution().generate(7)
