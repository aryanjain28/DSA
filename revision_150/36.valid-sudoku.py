#
# @lc app=leetcode id=36 lang=python
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        """

        for i in range(9):
            currRow, currCol = set(), set()

            if i == 0 or i == 3 or i == 6:
                box1, box2, box3 = set(), set(), set()

        
            for j in range(9):

                if board[i][j] != ".":

                    if j < 3:
                        if board[i][j] in box1:
                            return False
                        box1.add(board[i][j])
                    elif j < 6:
                        if board[i][j] in box2:
                            return False
                        box2.add(board[i][j])
                    else:
                        if board[i][j] in box3:
                            return False
                        box3.add(board[i][j])

                # row                
                if board[i][j] in currRow:
                    return False

                # col
                if board[j][i] in currCol:
                    return False
                
                if board[i][j] != ".":
                    currRow.add(board[i][j])
                if board[j][i] != ".":
                    currCol.add(board[j][i])


        return True




        
# @lc code=end
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))