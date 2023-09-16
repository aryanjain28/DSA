#
# @lc app=leetcode id=802 lang=python
#
# [802] Find Eventual Safe States
#

# @lc code=start
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
 
        """

        indegree = list(map(len, graph))
        q = []
        # reversing
        adjList = { n: set() for n in range(len(graph)) }
        for node, neighbors in enumerate(graph):
            if len(neighbors) == 0:
                q.append(node)

            for neighbor in neighbors:
                adjList[neighbor].add(node)

        res = []
        # BFS
        while q:
            node = q.pop()
            res.append(node)

            for neighbor in adjList[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)


        res.sort()
        return res

        # DFS

        # safe_nodes = {}
        # def dfs(node):

        #     if node in safe_nodes:
        #         return safe_nodes[node]
    
        #     safe_nodes[node] = False
        #     for neighbor in graph[node]:
        #         if not dfs(neighbor):
        #             return False
    
        #     safe_nodes[node] = True
        #     return safe_nodes[node]
        
        # res = []
        # for node in range(len(graph)):
        #     if dfs(node):
        #         res.append(node)
                        
        # return res

        

# @lc code=end

print(Solution().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
print(Solution().eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))