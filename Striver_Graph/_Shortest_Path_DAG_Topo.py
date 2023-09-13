

# Steps:
# 1. Find Topo Sort.
# 2. Define dist arr and start relaxing.


class Solution:

    def shortestPath(self, edges, vertices):

        adjList = {}
        for u, v, wt in edges:
            if u not in adjList:
                adjList[u] = set()

            adjList[u].add((v, wt))

        distance = [float("inf")] * vertices
        topoStack = []
        
        visited = set()
        # 1. find topo sort
        def topo(node):

            if node in visited:
                return
            
            visited.add(node)

            for (neighbor, _) in adjList.get(node, set()):
                if neighbor not in visited:
                    topo(neighbor)

            topoStack.append(node)


        for node in range(vertices):
            topo(node)

        while topoStack[-1] != 0:
            distance[topoStack.pop()] = -1
        
        distance[topoStack[-1]] = 0

        # 2. distance fill
        while topoStack:
            node = topoStack.pop()
            d = distance[node]

            for neighbor, wt in adjList.get(node, []):
                distance[neighbor] = min(d + wt, distance[neighbor])


        return distance










N = 6
edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
print(Solution().shortestPath(edges, N))

N = 4
edges = [[0,1,2],[0,2,1]]
print(Solution().shortestPath(edges, N))


