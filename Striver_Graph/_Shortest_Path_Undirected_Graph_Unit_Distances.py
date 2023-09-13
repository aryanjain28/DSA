


class Solution:
    def shortestPath(self, edges, n, m, src):
        

        adjList = {v:set() for v in range(n)}
        for u, v in edges:
            adjList[u].add(v)
            adjList[v].add(u)

        distances = [float("inf")] * (n)
        distances[src] = 0
        q = [(src, 0)]

        while q:
            node, wt = q.pop()

            for neighbor in adjList[node]:
                if distances[neighbor] > wt + 1:
                    distances[neighbor] = wt + 1
                    q.append((neighbor, distances[neighbor]))

        return [(-1 if d >= float("inf") else d) for d in distances]





n = 9
m = 10
edges=[[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src=0
Solution().shortestPath(edges, n, m, src)
