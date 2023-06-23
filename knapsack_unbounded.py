

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


# knapsack_unbounded([4, 4, 7, 1], [5, 2, 3, 1], 8)


# True Dynamic Solution
def knapsack_unbounded_tabulation(profits: list[int], weights: list[int], capacity: int) -> int:

    M = len(profits)  # rows
    N = capacity  # columns
    T = [[0] * (capacity + 1) for _ in range(M+1)]

    for index in range(1, M+1):
        for currCap in range(1, N+1):
            exclude = T[index-1][currCap]
            currWt = weights[index-1]
            if currCap >= currWt:
                include = profits[index-1] + T[index][currCap-currWt]
                T[index][currCap] = max(include, exclude)
            else:
                T[index][currCap] = exclude

    print(T)
    return T[-1][-1]


# knapsack_unbounded_tabulation([4, 4, 7, 1], [5, 2, 3, 1], 8)


# True Dynamic Solution: Space Optimized -> Using two rows
def knapsack_unbounded_tabulation_space_op(profits: list[int], weights: list[int], capacity: int) -> int:

    M = len(profits)  # rows
    N = capacity  # columns
    T1 = [0] * (capacity + 1)
    T2 = T1[:]

    for index in range(1, M+1):
        for currCap in range(1, N+1):
            exclude = T1[currCap]
            currWt = weights[index-1]
            if currCap >= currWt:
                include = profits[index-1] + T2[currCap-currWt]
                T2[currCap] = max(include, exclude)
            else:
                T2[currCap] = exclude
        T1 = T2[:]

    print(T2)
    return T2[-1]


# knapsack_unbounded_tabulation_space_op([4, 4, 7, 1], [5, 2, 3, 1], 8)


# True Dynamic Solution: Space Optimized -> Using one row
def knapsack_unbounded_tabulation_space_op_2(profits: list[int], weights: list[int], capacity: int) -> int:

    M = len(profits)  # rows
    N = capacity  # columns
    T = [0] * (capacity + 1)

    for index in range(M+1):
        for currCap in range(N+1):
            if currCap >= weights[index-1]:
                include = profits[index-1] + T[currCap-weights[index-1]]
                T[currCap] = max(T[currCap], include)

    print(T)
    return T[-1]


knapsack_unbounded_tabulation_space_op_2([4, 4, 7, 1], [5, 2, 3, 1], 8)


# using loop recursively
def knapsack_unbounded_loop(profits: list[int], weights: list[int], capacity: int) -> int:

    LEN = len(profits)

    cache = {}  # Memoization

    def rec(index: int, currCap: int) -> int:

        if index == LEN:
            return 0

        if (index, currCap) in cache:
            return cache[index, currCap]

        maxProfit = -1
        for i, wt in enumerate(weights):
            if currCap >= wt:
                maxProfit = max(maxProfit, profits[index] + rec(i, currCap-wt))

        cache[(index, currCap)] = maxProfit
        return cache[(index, currCap)]

    res = rec(0, capacity)
    print("MAX: ", res)
    return res


# knapsack_unbounded_loop([4, 4, 7, 1], [5, 2, 3, 1], 8)
