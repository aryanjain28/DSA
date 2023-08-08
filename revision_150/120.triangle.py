#
# @lc app=leetcode id=120 lang=python
#
# [120] Triangle
#

# @lc code=start
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        ROWS = len(triangle)

        # dp = {}
        # def rec(r, index):
            
        #     if (r, index) in dp:
        #         return dp[(r, index)]

        #     if r == ROWS-1:
        #         return triangle[r][index]
            
        #     bottom = rec(r+1, index)
        #     bottomRight = rec(r+1, index+1)

        #     dp[(r, index)] = triangle[r][index] + min(bottom, bottomRight)
        #     return dp[(r, index)]

        # return rec(0, 0)

        # dp = [[float("inf")] * (ROWS + 1) for _ in range(ROWS + 1)]
        # dp[0][1] = 0

        # for i in range(1, ROWS+1):
        #     for j in range(1, ROWS+1):
        #         if j > i:
        #             dp[i][j] = dp[i][j-1]
        #             continue
        #         dp[i][j] = triangle[i-1][j-1] + min(dp[i-1][j], dp[i-1][j-1])
                
        # return min(dp[i])


        prev = [0] * (ROWS + 1)
        triangle.append(prev)

        for i in range(ROWS-1, -1, -1):
            for j in range(i, -1, -1):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j+1], triangle[i+1][j])


        return triangle[0][0]
            


        
# @lc code=end
print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
# print(Solution().minimumTotal([[-1],[2,3],[1,-1,-3]]))
