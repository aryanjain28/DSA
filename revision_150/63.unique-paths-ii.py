#
# @lc app=leetcode id=63 lang=python
#
# [63] Unique Paths II
#

# @lc code=start
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

#         if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
#             return 0

#         dp = {}
#         def rec(r, c):
            
#             if (r, c) in dp:
#                 return dp[(r, c)]

#             if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
#                 return 0
            
#             if r == 0 and c == 0:
#                 return 1
                    
#             right = rec(r, c-1)
#             bottom = rec(r-1, c)

#             dp[(r, c)] = right + bottom
#             return dp[(r, c)]

#         # return rec(ROWS-1, COLS-1)
# #
# # @lc app=leetcode id=63 lang=python
# #
# # [63] Unique Paths II
# #

# # @lc code=start
# class Solution(object):
#     def uniquePathsWithObstacles(self, obstacleGrid):
#         """
#         :type obstacleGrid: List[List[int]]
#         :rtype: int
#         """

        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[ROWS-1][COLS-1] == 1:
            return 0

#         dp = {}
#         def rec(r, c):
            
#             if (r, c) in dp:
#                 return dp[(r, c)]

#             if r < 0 or c < 0 or obstacleGrid[r][c] == 1:
#                 return 0
            
#             if r == 0 and c == 0:
#                 return 1
                    
#             right = rec(r, c-1)
#             bottom = rec(r-1, c)

#             dp[(r, c)] = right + bottom
#             return dp[(r, c)]

#         # return rec(ROWS-1, COLS-1)

        prev = [0] * (COLS+1)
        curr = [0] * (COLS+1)
        prev[1] = 1  

        for i in range(1, ROWS+1):
            for j in range(1, COLS+1):
                if obstacleGrid[i-1][j-1] == 0:
                    curr[j] = curr[j-1] + prev[j]
                    continue
                
                curr[j] = 0
            prev = curr
        
        # print(curr)
        return curr[-1]







        
# @lc code=end
Solution().uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]])
# Solution().uniquePathsWithObstacles([[0,1],[0,0]])
# Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
