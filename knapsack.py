

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
