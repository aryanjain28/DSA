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

        mMap = {}
        for c in range(numCourses):
            mMap[c] = set()

        for a, b in prerequisites:
            mMap[a].add(b)


        res = []
        already_complete = set()

        def dfs(node, visited):

            if node in already_complete:
                return True

            if node in visited:
                return False
            
            visited.add(node)

            for nd in mMap[node]:
                if not dfs(nd, visited):
                    return False

            visited.remove(node)
            res.append(node)
            already_complete.add(node)

            return True


        for node in range(numCourses):
            if not dfs(node, set()):
                return []
            
        return res



            


        
# @lc code=end
# print(Solution().findOrder(4,[[1,0],[2,0],[3,1],[3,2]]))
# print(Solution().findOrder(2,[[1,0]]))
# print(Solution().findOrder(2,[]))
# print(Solution().findOrder(2,[[0,1],[1,0]]))
# print(Solution().findOrder(3,[[1,0]]))
# print(Solution().findOrder(3, [[0,2],[1,2],[2,0]]))
