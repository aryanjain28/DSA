from typing import List


def unboundedKnapsack(n: int, w: int, profit: List[int], weight: List[int]) -> int:

    dp = {}

    def rec(index, target):

        if (index, target) in dp:
            return dp[(index, target)]

        if index == 0:
            return (target // weight[0]) * profit[0]

        not_select = rec(index-1, target)
        select = -float("inf")
        if target >= weight[index]:
            select = profit[index] + rec(index, target-weight[index])

        dp[(index, target)] = max(not_select, select)
        return dp[(index, target)]

    # return rec(n-1, w)

    prev = [(t // weight[0])*profit[0] for t in range(w+1)]
    curr = [p for p in prev]

    for index in range(1, n+1):
        for target in range(1, w+1):
            not_select = prev[target]
            select = -float("inf")
            if target >= weight[index-1]:
                select = profit[index-1] + curr[target-weight[index-1]]

            curr[target] = max(select, not_select)

        prev = [c for c in curr]

    return curr[-1]


print(unboundedKnapsack(3, 10, [5, 11, 13], [2, 4, 6]))
