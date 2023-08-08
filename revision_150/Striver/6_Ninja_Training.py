from typing import *


def ninjaTraining(n: int, points: List[List[int]]):

    dp = {}

    def rec(day_index, index_2_avoid):

        if day_index < 0:
            return 0

        if (day_index, index_2_avoid) in dp:
            return dp[(day_index, index_2_avoid)]

        maxi = -1
        for index, activity in enumerate(points[day_index]):
            if index != index_2_avoid:
                maxi = max(maxi, activity + rec(day_index - 1, index))

        dp[(day_index, index_2_avoid)] = maxi
        return dp[(day_index, index_2_avoid)]

    # return rec(n-1, -1)

    dp = [[0]*4 for _ in range(n)]

    dp[0][0] = max(points[0][1], points[0][2])
    dp[0][1] = max(points[0][0], points[0][2])
    dp[0][2] = max(points[0][0], points[0][1])
    dp[0][3] = max(points[0])

    for day_index in range(1, n):
        for skip_index in range(4):
            maxi = -1
            for activity_index in range(3):
                if activity_index != skip_index:
                    res = points[day_index][activity_index] + \
                        dp[day_index-1][activity_index]
                    maxi = max(maxi, res)

            dp[day_index][skip_index] = maxi

    return dp[-1][-1]


print(ninjaTraining(2, [[19, 18, 6], [16, 36, 12]]))
# print(ninjaTraining(2, [[10, 50, 1], [5, 100, 11]]))
# print(ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
# print(ninjaTraining(3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
