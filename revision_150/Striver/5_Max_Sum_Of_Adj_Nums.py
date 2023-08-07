
def maximumNonAdjacentSum(nums):
    # Write your code here.

    # dp = {}

    # def rec(index):

    #     if index in dp:
    #         return dp[index]

    #     if index < 0:
    #         return 0

    #     left = nums[index] + rec(index - 2)
    #     right = 0 + rec(index - 1)

    #     dp[index] = max(left, right)
    #     return dp[index]

    # res = rec(len(nums)-1)
    # # return res

    n = len(nums)
    if n == 1:
        return nums[0]

    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for index in range(2, n):
        right = 0 + dp[index-1]
        left = nums[index] + dp[index-2]
        dp[index] = max(left, right)

    dp[-1]


print(maximumNonAdjacentSum([2, 1, 4, 9]))
