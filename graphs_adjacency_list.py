

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


def bfs(src, dest):

    length = 0
    queue = []
    queue.append(src)
    visit = set()

    while queue:

        for _ in range(len(queue)):
            node = queue.pop(0)

            if node == dest:
                return length

            for n in adjList[node]:
                if n not in visit:
                    queue.append(n)
                    visit.add(node)

        length += 1

    return length


adjList["A"] += ["D"]
print(bfs("A", "D"))
