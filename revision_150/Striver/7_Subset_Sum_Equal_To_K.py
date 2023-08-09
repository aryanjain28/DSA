from os import *
from sys import *
from collections import *
from math import *


def subsetSumToK(n, k, arr):

    dp = {}

    def rec(index, target):

        if (index, target) in dp:
            return dp[(index, target)]

        if index < 0 or target < 0:
            return False

        if target == 0:
            return True

        nSelect = rec(index-1, target)
        select = False
        if target-arr[index] >= 0:
            select = rec(index-1, target-arr[index])

        dp[(index, target)] = select or nSelect
        return dp[(index, target)]

    # return rec(n-1, k)

    # taulation
    dp = [[False for _ in range(k+2)] for _ in range(n+1)]
    for i in range(len(dp)):
        dp[i][1] = True

    for i in range(1, n+1):
        for target in range(2, k+2):

            nSelect = dp[i-1][target]
            select = False
            if target-arr[i-1] >= 0:
                select = dp[i-1][target-arr[i-1]]

            dp[i][target] = select or nSelect

    return dp[-1][-1]


print(subsetSumToK(4, 4, [6, 1, 2, 1]))
print(subsetSumToK(3, 4, [6, 1, 2]))
