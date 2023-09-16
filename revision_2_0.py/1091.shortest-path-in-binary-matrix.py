#
# @lc app=leetcode id=1091 lang=python
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start

import heapq

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)
        
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        
        def isOutOfBouds(i, j):
            return  i < 0 or j < 0 or i == n or j == n

        directions = [[-1,0], [1,0], [0,-1], [0, 1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

        adjList = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    for (x, y) in directions:
                        if not isOutOfBouds(i+x, j+y) and grid[i+x][j+y] == 0:
                            if (i, j) not in adjList:
                                adjList[(i, j)] = []

                            adjList[(i, j)].append((i+x, j+y))

        src = (0, 0)
        dest = (n-1, n-1)

        distance = {k: float("inf") for k in adjList.keys()}
        distance[src] = 0

        visited = set()
        visited.add(src)

        pq = [(0, src)]
        while pq:
            d, node = heapq.heappop(pq)
            visited.add(node)

            if node not in adjList:
                continue

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    if distance[neighbor] > d + 1:
                        distance[neighbor] = d + 1
                        heapq.heappush(pq, (d+1, neighbor))


        if dest not in distance or distance[dest] >= float("inf"):
            return -1
        return distance[dest] + 1

            


        
# @lc code=end

# Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
# Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,1]])
Solution().shortestPathBinaryMatrix([[0,0,0,0,1],[1,0,0,0,0],[0,1,0,1,0],[0,0,0,1,1],[0,0,0,1,0]])