

# Recursive approach
def knapsack_unbounded(profits: list[int], weights: list[int], capacity: int) -> int:

    LEN = len(weights)

    cache = {}  # Memoized

    def rec(index: int, currCap: int):

        # base cases
        if index == LEN:
            return 0

        if (index, currCap) in cache:
            return cache[(index, currCap)]

        exclude = rec(index+1, currCap)
        include = 0
        if currCap >= weights[index]:
            include = profits[index] + rec(index, currCap-weights[index])

        cache[(index, currCap)] = max(include, exclude)
        return cache[(index, currCap)]

    res = rec(0, capacity)
    print(res)
    return res


knapsack_unbounded([4, 4, 7, 1], [5, 2, 3, 1], 8)
