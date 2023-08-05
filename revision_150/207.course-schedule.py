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

        mMap = {}
        for a, b in prerequisites:

            if a == b:
                return False

            if a not in mMap:
                mMap[a] = set()
            
            mMap[a].add(b)


        def dfs(node, visited):

            if node in visited:
                return False
            
            if node not in mMap:
                return True
            
            visited.add(node)
            for prereq in mMap[node]:
                if not dfs(prereq, visited):
                    return False
                
            visited.remove(node)
            mMap[node] = set()
            return True

        
        for node in range(numCourses):
            if not dfs(node, set()):
                return False

        return True        

        
# @lc code=end
print(Solution().canFinish(1, [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]))
# print(Solution().canFinish(2, [[]]))
# print(Solution().canFinish(2, [[1,0]]))
# print(Solution().canFinish(2, [[1,0], [0,1]]))
# print(Solution().canFinish(2, [[1,0], [0,5], [5,6], [5,4], [6,4]]))
# print(Solution().canFinish(2, [[1,0], [0,5], [5,6], [4,5], [6,4]]))


