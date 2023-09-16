

def shortest_path_multisource(edges, nodes, t):

    cost_matrix = [[float("inf")]* nodes for _ in range(nodes)]

    for (u, v, wt) in edges:
        cost_matrix[u][v] = wt
        # cost_matrix[v][u] = wt    # if UG

    for n in range(nodes):
        cost_matrix[n][n] = 0

    for via in range(nodes):
        for i in range(nodes):
            if i == via: continue
            for j in range(nodes):
                if i == j or j == via: continue
                cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][via] + cost_matrix[via][j])


    




edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
nodes = 4

edges = [[0,1,2],[1,0,1],[1,2,3],[3,1,5],[3,0,3],[3,2,4]]
nodes = 4

print(shortest_path_multisource(edges, nodes))