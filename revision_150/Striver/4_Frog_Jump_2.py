
import sys
n, k = map(int, input().split())
heights = list(map(int, input().split()))

if k > n:
    print(0)


def height(i, j):
    return abs(heights[i] - heights[j])


dp = [0] * (n)

for index in range(1, k+1):
    dp[index] = height(0, index)

for index in range(1, n):

    mini = float("inf")
    for i in range(index-1, max(-1, (index-k)-1), -1):
        mini = min(height(index, i) + dp[i], mini)

    dp[index] = mini

print(dp[-1])

# print(frogJump2(5, 3, [10, 30, 40, 50, 20]))
# print(frogJump2(3, 1, [10, 20, 10]))
# print(frogJump2(10, 4, [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]))
# print(frogJump2(2, 100, [10, 10]))
