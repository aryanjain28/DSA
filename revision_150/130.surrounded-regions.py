#
# @lc app=leetcode id=130 lang=python
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])
        

        def isOutOfBounds(r, c):
            return r < 0 or r >= ROWS or c < 0 or c >= COLS


        # def dfs(r, c):
            
        #     if isOutOfBounds(r, c):
        #         return False
            
        #     if board[r][c] == "#" or board[r][c] == "X":
        #         return True
                        
        #     board[r][c] = "#"

        #     top = dfs(r-1, c)
        #     bottom = dfs(r+1, c)
        #     left = dfs(r, c-1)
        #     right = dfs(r, c+1)

        #     print(r, c, "top: ", top)
        #     print(r, c, "bottom: ", bottom)
        #     print(r, c, "left:", left)
        #     print(r, c, "right:", right)
            

            
            # if top and bottom and left and right:
            #     board[r][c] = "X"
            #     return True

            # board[r][c] = "O"        
            # return False


        

        def dfs(r, c):
            if isOutOfBounds(r, c) or board[r][c] != "O":
                return
            
            board[r][c] = "#"

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

                        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
        
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"                


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "#":
                    board[r][c] = "O"






        
# @lc code=end
# Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
# Solution().solve([["O","O","O"],["O","O","O"],["O","O","O"]])

Solution().solve([["X","O","X"],["O","X","O"],["X","O","X"]])


