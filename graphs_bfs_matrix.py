

grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]

queue = [(0, 0)]
visit = set((0, 0))


def helper(r, c):

    if r < 0 or\
            c < 0 or\
            r >= len(grid) or\
            c >= len(grid[0]) or\
            grid[r][c] == 1 or\
            (r, c) is visit:
        return False
    return True


def bfs():

    length = 0
    while queue:

        for _ in range(len(queue)):

            rq, cq = queue.pop(0)
            if rq == len(grid) - 1 and cq == len(grid[0]) - 1:
                return length + 1
            for (rDir, cDir) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:

                if helper(rq+rDir, cq+cDir):
                    queue.append((rq+rDir, cq+cDir))
                    visit.add((rq+rDir, cq+cDir))

        length += 1


print(bfs())
