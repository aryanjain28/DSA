

dp = {}


def dfs(n):

    if n in dp:
        return dp[n]
    if n <= 1:
        return n

    dp[n] = dfs(n-1) + dfs(n-2)
    return dp[n]


print(dfs(8))
print(dp)


def tab(n):
    dp = list(range(n + 1))
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[-1]


print(tab(5))
print(tab(6))
print(tab(7))
