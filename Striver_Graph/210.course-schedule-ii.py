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

        if len(prerequisites) == 0:
            return list(range(numCourses))

        adjList = {}
        for n in range(numCourses):
            adjList[n] = set()

        for c1, c2 in prerequisites:
            adjList[c1].add(c2)


        already_visited = set()
        visited = set()
        res = []
        
        def dfs(node):
            if node in already_visited:
                return True
            
            if node in visited:
                return False
            
            visited.add(node)

            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            visited.remove(node)
            
            already_visited.add(node)
            res.append(node)

            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
            
        return res




        
# @lc code=end

