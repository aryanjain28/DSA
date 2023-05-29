# Matrix representation - a way to represent a graph.
# Graph - DFS


grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
]
visit = set()


def helper(r, c):
    # check top
    if r < 0 or\
            c < 0 or\
            r == len(grid) or\
            c == len(grid[0]) or\
            grid[r][c] == 1 or\
            (r, c) in visit:
        return True
    return False

# count the unique # of ways to reach the end


def dfs(r, c):

    # stopping condition.
    if helper(r, c):
        return 0

    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    grid[r][c] = 1

    count = 0
    count += dfs(r-1, c)  # top
    count += dfs(r+1, c)  # bottom
    count += dfs(r, c+1)  # right
    count += dfs(r, c-1)  # left

    grid[r][c] = 0

    return count


print(dfs(0, 0))
