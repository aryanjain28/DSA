#
# @lc app=leetcode id=741 lang=python
#
# [741] Cherry Pickup
#

# @lc code=start
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)


        path_sum = {}
        def rec(r, c, path):

            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] == -1:
                return 0

            if r == 0 and c == 0:
                return grid[0][0]                
            
            right = rec(r, c-1, path)
                    
            # init state
            if r == n-1 and c == n-1:
                path_sum[grid[r][c] + right] = path
                path = []

            bottom = rec(r-1, c, path)        

            # init state
            if r == n-1 and c == n-1:
                path_sum[grid[r][c] + bottom] = path

            path.append((r, c))            
            return grid[r][c] + max(right, bottom)


        
        rec(n-1, n-1, [])
        max1 = max(path_sum.keys())
        max_path = path_sum[max1]

        if grid[0][0] == 1:
            max_path.append((0, 0))

        for (i, j) in max_path:
            grid[i][j] = 0

        print(path_sum)
        max2 = rec(n-1, n-1, [])

        return max1 + max2




        
# @lc code=end
# Solution().cherryPickup([[1,1],[1,1]])
# print(Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))
print(Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]]))