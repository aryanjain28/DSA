

def frogJump(n, heights):

    # signifies: what is the min energy required to
    # jump from n to 0:
    def rec(index):

        if index <= 0:
            return 0

        left = abs(heights[index] - heights[index-1]) + rec(index-1)
        if index-2 < 0:
            return left

        right = abs(heights[index] - heights[index-2]) + rec(index-2)

        return min(left, right)

    # return rec(n-1)

    dp = [0] * (n)
    dp[1] = abs(heights[0] - heights[1])

    for i in range(2, n):
        left = abs(heights[i] - heights[i-1]) + dp[i-1]
        if i-2 < 0:
            dp[i] = left
            continue
        right = abs(heights[i] - heights[i-2]) + dp[i-2]
        dp[i] = min(left, right)

    return dp[-1]


frogJump(4, [10, 20, 30, 10])
