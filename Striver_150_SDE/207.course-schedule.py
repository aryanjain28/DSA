#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        adjList = {}
        for (a, b) in prerequisites:
            if b not in adjList:
                adjList[b] = []

            adjList[b].append(a)

    

        dp = {}
        visit = set()
        def detect(node):

            if node in dp:
                return dp[node]
        
            if node in visit:
                return False
            
            visit.add(node)

            for neighbor in (adjList.get(node, [])):
                if not detect(neighbor):
                    dp[neighbor] = False
                    return False

            visit.remove(node)
            dp[node] = True
            return True
    

        for node in range(numCourses):
            if not detect(node):
                return False
            
        return True
        
# @lc code=end

print(Solution().canFinish(2, [[1,0]]))
# print(Solution().canFinish(3, [[1,0],[2,0],[1,2]]))