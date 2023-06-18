
from time import time

# Brute force way!


def countPaths(row: int = 0, col: int = 0) -> int:

    if row >= n or col >= n:
        return 0

    if row == n - 1 and col == n - 1:
        return 1

    return countPaths(row + 1, col) + countPaths(row, col + 1)


start_time = time()
n = 4
countPaths()
diff1 = time() - start_time
print("Time taken without cache: ", diff1)


# Memoization
# Top Down Approach

cache = {}


def countPaths2(row: int = 0, col: int = 0) -> int:

    if (row, col) in cache:
        return cache[(row, col)]

    if row >= n or col >= n:
        return 0

    if row == n - 1 and col == n - 1:
        return 1

    cache[(row, col)] = countPaths2(row + 1, col) + countPaths2(row, col + 1)
    return cache[(row, col)]


start_time = time()
n = 4
countPaths2()
diff2 = time() - start_time
print("Time taken with cache: ", diff2)

print(cache)
