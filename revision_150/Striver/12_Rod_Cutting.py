
def cutRod(price, n):

    dp = {}

    def rec(index, target):

        if (index, target) in dp:
            return dp[(index, target)]

        if index == 0:
            return (target // weights[0]) * price[0]

        not_select = rec(index-1, target)
        select = -float("inf")

        if target >= weights[index]:
            select = price[index] + rec(index, target-weights[index])

        dp[(index, target)] = max(select, not_select)
        return dp[(index, target)]

    weights = [n for n in range(1, n+1)]
    # return rec(n-1, n)

    prev = [(w * price[0]) for w in range(n+1)]
    curr = [c for c in prev]

    for index in range(1, n+1):
        for target in range(1, n+1):
            not_select = prev[target]
            select = -float("inf")

            if target >= weights[index-1]:
                select = price[index-1] + curr[target-weights[index-1]]

            curr[target] = max(select, not_select)

        prev = [c for c in curr]

    return curr[-1]


print(cutRod([2, 5, 7, 8, 10], 5))
