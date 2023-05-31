

adjList = {}
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]


for nodeTo, nodeFrom in edges:
    adjList[nodeTo] = adjList.get(nodeTo, []) + [nodeFrom]
    adjList[nodeFrom] = adjList.get(nodeFrom, [])


print(adjList)
