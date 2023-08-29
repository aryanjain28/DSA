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
            return [[1], [1,1]]
        
        rows = [[1], [1,1], [1,2,1]]

        for n in range(4, numRows+1):
            lastRow = rows[-1]
            newRow = [1]
            for j in range(len(lastRow) // 2):
                newRow.append(lastRow[j] + lastRow[j+1])
            
            newRow += newRow[::-1] if (n) % 2 == 0 else newRow[::-1][1:]
            rows.append(newRow)


        return rows





        
        
# @lc code=end

# Solution().generate(5)
# Solution().generate(6)
Solution().generate(7)