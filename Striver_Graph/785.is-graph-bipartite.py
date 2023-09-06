#
# @lc app=leetcode id=785 lang=python
#
# [785] Is Graph Bipartite?
#

# @lc code=start
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """

        n = len(graph)

        adjMap = {}
        for node, neighbors in enumerate(graph):
            adjMap[node] = set(neighbors)

        arr = [-1] * n

        def dfs(node, color):
            
            if arr[node] != -1:
                return color == arr[node]                    

            arr[node] = color

            for neighbor in adjMap[node]:
                if not dfs(neighbor, abs(color - 1)):
                    return False
                
            return True

        for n in range(len(graph)):
            if arr[n] == -1 and not dfs(n, 1):
                return False
                
            
        return True


    
        # setA = set()
        # setB = set()

        # visited = set()

        # def dfs(node, parentSet):

        #     if node in visited:
        #         return node not in parentSet
            
        #     if node in (setA if parentSet == 0 else setB):
        #         return False

        #     visited.add(node)
        #     (setB if parentSet == 0 else setA).add(node)

        #     for neighbor in adjMap[node]:
        #         if neighbor not in visited:
        #             if not dfs(neighbor, abs(parentSet-1)):
        #                 return False

        #     visited.remove(node)
        #     return True
                
        # for n in range(len(graph)):
        #     if len(adjMap[n]) > 0:
        #         return dfs(n, 1)

        # return True





        
# @lc code=end

print(Solution().isBipartite([[1,3],[0,2], [1,3], [0,2]]))
print(Solution().isBipartite([[4], [], [4], [4], [0,2,3]]))