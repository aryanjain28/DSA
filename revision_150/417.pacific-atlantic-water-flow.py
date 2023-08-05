#
# @lc app=leetcode id=417 lang=python
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []


        ROW = len(heights)
        COL = len(heights[0])

        atl = set()
        pac = set()

        def isOutOfBounds(r, c):
            return r < 0 or r >= ROW or c < 0 or c >= COL
        
        def dfs(r, c, visited, parent_height):

            if (r,c) in visited or isOutOfBounds(r, c) or heights[r][c] < parent_height:
                return
            
            visited.add((r,c))

            dfs(r-1, c, visited, heights[r][c])
            dfs(r+1, c, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])

            return


        # top row: pac
        for c in range(COL):
            dfs(0, c, pac, heights[0][c])

        # bottom row: atl
        for c in range(COL):
            dfs(ROW-1, c, atl, heights[ROW-1][c])

        # left col: pac
        for r in range(ROW):
            dfs(r, 0, pac, heights[r][0])

        # right col: atl
        for r in range(ROW):
            dfs(r, COL-1, atl, heights[r][COL-1])

        
        res = []
        for (r,c) in pac:
            if (r,c) in atl:
                res.append((r,c))

        print(res)
        return res
        


        # mDict = {}



        # def dfs(r, c, parent_ht):

        #     if isBorder(r, c):
        #         return True
                    
        #     curr_ht = heights[r][c]
        #     if curr_ht > parent_ht:
        #         return False
            
        #     pacific_1 = dfs(r-1, c, curr_ht)
        #     pacific_2 = dfs(r, c-1, curr_ht)

        #     atlantic_1 = dfs(r+1, c, curr_ht)
        #     atlantic_2 = dfs(r, c+1, curr_ht)

        #     return (pacific_1 or pacific_2) and (atlantic_1 or atlantic_2)
            
        
        # for r in range(ROW):
        #     for c in range(COL):
        #         if heights[r][c] >= 0 and dfs(r, c, float("inf")):
        #             res.append([r,c])


        # for k, v in mDict.items():
        #     print(k, v)

        # print(heights)
        # print(res)
        # return res

        
# @lc code=end
Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
