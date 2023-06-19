

def knapSackMax(profit: list[int], weight: list[int], capacity: int) -> int:

    cache = {}

    def track(index: int, cap: int) -> int:

        if index == len(profit):
            return 0

        if (index, cap) in cache:
            return cache[(index, cap)]

        # skip
        p1 = track(index+1, cap)

        # include
        p2 = p1
        if cap-weight[index] >= 0:
            p2 = profit[index] + track(index+1, cap-weight[index])

        cache[(index, cap)] = p1 if p1 > p2 else p2
        return cache[(index, cap)]

    return track(0, capacity)


print(knapSackMax(
    [4, 4, 7, 1],
    [5, 2, 3, 1],
    8
)
)


# True dp

def knapSack(profit: list[int], weight: list[int], capacity: int) -> int:

    N = len(profit)
    M = capacity

    matrix = [[0] * (M + 1) for _ in range(N)]

    for index, _ in enumerate(matrix[0]):
        if index >= weight[0]:
            matrix[0][index] = profit[0]

    for item in range(1, N):
        for cap in range(1, M+1):
            included = profit[item] + matrix[item-1][cap-weight[item]] if cap >= weight[item] else 0
            matrix[item][cap] = max(matrix[item-1][cap], included)

    print(matrix)
    return matrix[-1][-1]


knapSack([4, 4, 7, 1], [5, 2, 3, 1], 8)
