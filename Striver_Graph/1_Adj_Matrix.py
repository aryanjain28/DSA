
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

matrix = [[0] * (n+1) for _ in range(n+1)]

for n1, n2 in nodes:
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1

for m in matrix:
    print(m)

