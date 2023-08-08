from typing import *


def ninjaTraining(n: int, points: List[List[int]]):

    dp = {}

    def rec(day_index, index_2_avoid):

        if day_index >= n:
            return 0

        if (day_index, index_2_avoid) in dp:
            return dp[(day_index, index_2_avoid)]

        temp = []
        for index, activity in enumerate(points[day_index]):
            if index != index_2_avoid:
                temp.append(activity + rec(day_index + 1, index))

        dp[(day_index, index_2_avoid)] = max(temp)
        return dp[(day_index, index_2_avoid)]

    return rec(0, -1)


print(ninjaTraining(2, [[10, 50, 1], [5, 100, 11]]))
print(ninjaTraining(3, [[1, 2, 5], [3, 1, 1], [3, 3, 3]]))
print(ninjaTraining(3, [[10, 40, 70], [20, 50, 80], [30, 60, 90]]))
