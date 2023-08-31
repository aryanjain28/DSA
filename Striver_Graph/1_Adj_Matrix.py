
n = 5
m = 6

nodes = [
    [1, 2],
    [1, 3],
    [2, 4],
    [3, 4],
    [2, 5],
    [4, 5],
]

# Adj Matrix
matrix = [[0] * (n+1) for _ in range(n+1)]

for n1, n2 in nodes:
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

# for m in matrix:
#     print(m)


# Adj List
adjList = {}
for n1, n2 in nodes:
    adjList[n1] = adjList.get(n1, set())
    adjList[n2] = adjList.get(n2, set())

    adjList[n1].add(n2)
    adjList[n2].add(n1)


print(adjList)
