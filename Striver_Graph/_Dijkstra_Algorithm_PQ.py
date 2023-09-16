

import heapq 

class Solution:
    
    def dijkstra(self, nodes, adj, src):

        adjList = {}
        for parent, neighbors in enumerate(adj):
            for node, wt in neighbors:
                if parent not in adjList:
                    adjList[parent] = []

                adjList[parent].append((node, wt))


        distance = [float("inf")] * nodes
        distance[src] = 0

        heap = [(0, src)]

        while heap:
            d, node = heapq.heappop(heap)
            
            for (neighbor, wt) in adjList[node]:
                if distance[neighbor] > d + wt:
                    distance[neighbor] = d + wt
                    heapq.heappush(heap, (distance[neighbor], neighbor))
            
        
        return distance


adj = [[(1, 1), (2, 6)], [(2, 3), (0, 1)], [(1, 3), (0, 6)]]
Solution().dijkstra(3, adj, 2)