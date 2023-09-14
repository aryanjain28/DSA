

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, n, edges, src):

        distance = [100000000] * n
        distance[src] = 0

        for _ in range(n-1):
            for u, v, wt in edges:
                distance[v] = min(distance[v], distance[u] + wt)

        for u, v, wt in edges:
            if distance[v] > distance[u] + wt:
                return [-1]

        return distance
        


S = 2
V = 3
edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
Solution().bellman_ford(V, edges, S)



edges = [
[0, 1, 2],
[0, 2, -2],
[0, 3, -1],
[0, 4, -6],
[0, 6, 2],
[1, 0, -2],
[1, 2, 4],
[1, 4, -7],
[1, 6, 10],
[2, 0, -8],
[2, 1, 10],
[2, 6, -8],
[3, 1, -1],
[3, 4, 4],
[4, 1, -11],
[4, 2, -10],
[4, 3, -4],
[5, 0, 1],
[5, 2, 8],
[5, 3, -3],
[5, 4, 3],
[5, 6, 6],
[6, 0, 9],
[6, 1, 1],
[6, 3, -11],]