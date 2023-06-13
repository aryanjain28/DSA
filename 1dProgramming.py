
# Fibonacci

def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n-1) + bruteForce(n-2)


# print(bruteForce(0))
# print(bruteForce(1))
# print(bruteForce(2))
# print(bruteForce(3))

# print(bruteForce(9))
# print(bruteForce(10))

# Memoization

# Top Down Approach
def memoization(n, cache):

    if n <= 1:
        return n

    if n in cache:
        return cache[n]

    cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
    return cache[n]


# print(memoization(0, {}))
# print(memoization(1, {}))
# print(memoization(2, {}))
# print(memoization(3, {}))
# print(memoization(9, {}))
# print(memoization(10, {}))


# Bottom Up Approach: True DP

def dp(n):

    fn1, fn2 = 0, 1
    for _ in range(2, n+1):
        fn1, fn2 = fn2, fn1 + fn2

    return fn2


print(dp(1))
print(dp(2))
print(dp(3))
print(dp(4))
print(dp(5))
print(dp(6))
