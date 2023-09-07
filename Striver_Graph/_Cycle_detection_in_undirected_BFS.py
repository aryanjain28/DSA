

def isCycle(V, adj):
    
    adjList = {}
    
    for index, neighbors in enumerate(adj):
        adjList[index] = set(neighbors)


    visited = set()

    for n in range(V):

        if n in visited: 
            continue


        q = [(n, -1)]
        visited.add(n)

        while q:
            (node, parent) = q.pop(0)
            
            for neighbor in adjList[node]:
                if neighbor != parent:
                    
                    if neighbor in visited: return 1
                    
                    visited.add(neighbor)
                    q.append((neighbor, node))
        
    return 0




