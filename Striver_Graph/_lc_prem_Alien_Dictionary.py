
indegree = {}
adjList = {}

def compare(s1, s2):
    
    c1 = s1[0]
    c2 = s2[0]

    index = 0
    while c1 == c2:
        
        c1 = s1[index]
        c2 = s2[index]

        if c1 not in indegree:
            indegree[c1] = 0

        if c2 not in indegree:
            indegree[c2] = 0

        if c2 not in adjList:
            adjList[c2] = set()

        if c1 not in adjList:   
            adjList[c1] = set()

        index += 1


    if c2 not in adjList:
        adjList[c2] = set()

    if c1 not in adjList:   
        adjList[c1] = set()

    if c1 not in indegree:
        indegree[c1] = 0

    if c2 not in indegree:
        indegree[c2] = 0

    adjList[c1].add(c2)
    indegree[c2] += 1


def AlienDictionary(strings):

    index = 0
    while index < len(strings)-1:
        compare(strings[index], strings[index+1])
        index += 1

    q = []

    for node, ind in indegree.items():
        if ind == 0:
            q.append(node)

    if not q: 
        return ""

    res = []
    while q:
        node = q.pop(0)
        res.append(node)

        for neighbor in adjList[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                q.append(neighbor)

    return "".join(res)






strings = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

# strings = [
#   "baa",
#   "abcd",
#   "abca",
#   "cab",
#   "cad"
# ]


# strings =  [ "z", "x", "z" ]

print(AlienDictionary(strings))