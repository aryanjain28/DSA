#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        ROW = len(board)
        COL = len(board[0])
        

        def isOutOfBounds(row, col):
            return ( row < 0 or row >= ROW ) or ( col < 0 or col >= COL )



        def find(row, col, c_index):

            if isOutOfBounds(row, col) or board[row][col] != word[c_index]:
                return False

            if c_index == len(word) - 1:
                return True
            
            board[row][col] = None

            # top
            t = find(row-1, col, c_index+1)

            # left
            l = find(row, col-1, c_index+1)

            # right
            r = find(row, col+1, c_index+1)

            # bottom
            b = find(row+1, col, c_index+1)

            board[row][col] = word[c_index]

            return t or l or r or b


        for i in range(ROW):
            for j in range(COL):
                if word[0] == board[i][j] and find(i, j, 0):
                    return True                
        
        return False


        
# @lc code=end
print(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
