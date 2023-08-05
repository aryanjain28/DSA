#
# @lc app=leetcode id=994 lang=python
#
# [994] Rotting Oranges
#

# @lc code=start
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ROWS = len(grid)
        COLS = len(grid[0])


        
        visited = {}

        def isOutBounds(r, c):
            return r < 0 or r > ROWS-1 or c < 0 or c > COLS-1


        # def dfs(r, c, time):

        #     if isOutBounds(r, c) or grid[r][c] == 0:
        #         return
            
        #     if (r, c) in visited and visited[(r, c)] <= time:
        #         return
            
        #     time = 0 if grid[r][c] == 2 else time
        #     visited[(r, c)] = time

        #     dfs(r-1, c, time+1)
        #     dfs(r+1, c, time+1)
        #     dfs(r, c-1, time+1)
        #     dfs(r, c+1, time+1)
            


        q = []
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append(((r, c), 0))
                

        if not q:
            if fresh > 0:
                return -1
            return 0

        def check(r, c):
            if isOutBounds(r, c) or grid[r][c] != 1:
                return False
            return True


        # bfs
        while q:
            (r, c), time = q.pop(0)
            for (d1, d2) in  [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if check(r+d1, c+d2):
                    q.append(((r+d1, c+d2), time+1))
                    
                    if grid[r][c] == 1:
                        fresh -= 1

                    grid[r][c] = 2
                    

        print(fresh)
        if fresh <= 0:
            return time
        
        return -1
                    

        # total = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] != 0:
        #             total += 1

        #         if grid[r][c] == 2:
        #             dfs(r, c, 0)


        # if total == 0:
        #     return 0

        # if total - len(visited) > 0:
        #     return -1
        
        # return max(visited.values())

        # return self.time_max if len(visited) >= count else -1
            
        
        
# @lc code=end
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
# print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
# print(Solution().orangesRotting([[0]]))
# print(Solution().orangesRotting([[1]]))
# print(Solution().orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))
# print(Solution().orangesRotting([[2,2,2,1,1]]))

