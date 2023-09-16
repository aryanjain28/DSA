#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # using kahn's alog

        adjList = {}
        for node in range(numCourses):
            adjList[node] = set()

        indeg = [0] * numCourses
        
        for c1, c2 in prerequisites:
            adjList[c1].add(c2)
            indeg[c2] += 1


        q = []
        for node, deg in enumerate(indeg):
            if deg == 0:
                q.append(node)

        if not q: return []

        # print(indeg)
        # print(adjList)

        res = []
        while q:
            node = q.pop(0)
            res.append(node)

            # print(indeg)

            for neighbor in adjList[node]:
                indeg[neighbor] -= 1
                if indeg[neighbor] == 0:
                    q.append(neighbor)

        
        if len(res) != numCourses:
            return []
        
        return res[::-1]


        
# @lc code=end

# Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
Solution().findOrder(3, [[0,2],[1,2],[2,0]])
