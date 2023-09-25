#
# @lc app=leetcode id=1466 lang=python
#
# [1466] Reorder Routes to Make All Paths Lead to the City Zero
#

# @lc code=start
class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        isReaching = [False] * (n)
        isReaching[0] = True

        adjList = {node: set() for node in range(n) }
        for a, b in connections:
            if b == 0: isReaching[a] = True
            adjList[a].add(b)

        count = 0
        def dfs(node):
            nonlocal count
            if isReaching[node]:
                return
            
            isReaching[node] = True
            for child in adjList[node]:
                if not isReaching[child]:
                    dfs(child)
                    count += 1


        for node in range(n):
            dfs(node)
        
        return count 


        


            
            


        
# @lc code=end
# print(Solution().minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
# print(Solution().minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
# print(Solution().minReorder(n = 3, connections = [[1,0],[2,0]]))
print(Solution().minReorder(7, [[0,6],[6,3],[1,3],[2,1],[4,0],[4,5]]))
