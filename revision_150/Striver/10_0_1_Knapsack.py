

def max_rob(n, weights, values, cap):

    dp = {}

    def rec(index, capacity):

        if (index, capacity) in dp:
            return dp[(index, capacity)]

        if index < 0 or capacity == 0:
            return 0

        nSelect = rec(index-1, capacity)

        select = 0
        if capacity >= weights[index]:
            select = values[index] + rec(index-1, capacity-weights[index])

        dp[(index, capacity)] = max(select, nSelect)
        return dp[(index, capacity)]

    # return rec(n-1, cap)

    prev = [0] * (cap+1)
    curr = [0] * (cap+1)

    for index in range(1, n+1):
        for capacity in range(1, cap+1):
            nSelect = prev[capacity]

            select = 0
            if capacity >= weights[index-1]:
                select = values[index-1] + prev[capacity-weights[index-1]]

            curr[capacity] = max(select, nSelect)

        prev = [c for c in curr]

    print(curr[-1])


print(max_rob(4, [1, 2, 4, 5], [5, 4, 8, 6], 5))
