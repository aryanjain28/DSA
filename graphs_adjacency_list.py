

adjList = {}
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]


for nodeTo, nodeFrom in edges:
    adjList[nodeTo] = adjList.get(nodeTo, []) + [nodeFrom]
    adjList[nodeFrom] = adjList.get(nodeFrom, [])


print(adjList)


visit = set()


def dfs(src, dest):

    if src in visit:
        return 0
    if src == dest:
        return 1

    count = 0
    visit.add(src)
    for nodeTo in adjList.get(src, []):
        count += dfs(nodeTo, dest)
    visit.remove(src)

    return count


print(dfs("A", "E"))
