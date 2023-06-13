
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
print(memoization(10, {}))
