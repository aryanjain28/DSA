from os import *
from sys import *
from collections import *
from math import *


def subsetSumToK(n, k, arr):

    dp = {}

    def rec(index, target):

        if (index, target) in dp:
            return dp[(index, target)]

        if target == 0:
            return True

        if index < 0 or target < 0:
            return False

        # not select
        right = rec(index-1, target)
        # select
        left = False
        if target >= arr[index]:
            left = rec(index-1, target-arr[index])

        dp[(index, target)] = left or right
        return dp[(index, target)]

    return rec(n-1, k)


arr = [int(n.strip())
       for n in "8 59 58 79 44 7 65 69 60 51".split(" ")]


print(subsetSumToK(4, 4, [6, 1, 2, 1]))
# print(subsetSumToK(4, 4, [1, 2, 3, 4]))
print(subsetSumToK(len(arr), 172, arr))
