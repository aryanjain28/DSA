#
# @lc app=leetcode id=1631 lang=python
#
# [1631] Path With Minimum Effort
#

import heapq

# @lc code=start
class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """

        n = len(heights)
        m = len(heights[0])

        src = (0, 0)
        dest = (n-1, m-1)

        distance = {}
        pq =  [(0, src)]

        def isOutOfBounds(i, j):
            return i < 0 or j < 0 or i == n or j == m

        while pq:
            d, node = heapq.heappop(pq) 

            if node == dest:
                return d

            (i, j) = node
            for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if not isOutOfBounds(x+i, y+j):
                    wt = abs(heights[x+i][y+j] - heights[i][j])

                    if (x+i, y+j) not in distance or distance[(x+i, y+j)] > max(wt, d):
                        distance[(x+i, y+j)] = max(wt, d)
                        heapq.heappush(pq, (max(wt, d), (x+i, y+j)))






# @lc code=end
# print(Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))
# print(Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
