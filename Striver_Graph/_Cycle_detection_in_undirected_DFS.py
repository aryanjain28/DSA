from typing import List

def isCycle(V: int, adj: List[List[int]]) -> bool:
    
    
    adjList = {}
    
    for index, neighbors in enumerate(adj):
        adjList[index] = set(neighbors)

    
    visited = set()
    
    def dfs(node, parent):
        
        visited.add(node)
    
        for neighbor in adjList[node]:
            if neighbor != parent:
                
                if neighbor in visited or dfs(neighbor, node):
                    return True

        return False

    for n in range(V):
    
        if n in visited:
            continue

        if dfs(n, -1): return True
        
    return False
    
    
