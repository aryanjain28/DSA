

def findWays(arr, k: int) -> int:

    n = len(arr)

    dp = {}

    def rec(index, target):

        if (index, target) in dp:
            return dp[(index, target)]

        if target == 0:
            return 1

        if index < 0:
            return 0

        nSelect = rec(index-1, target)
        select = 0
        if target >= arr[index]:
            select = rec(index-1, target-arr[index])

        dp[(index, target)] = nSelect + select
        return nSelect + select

    # return rec(n-1, k)

    # tabulation

    prev = [0 for _ in range(k+1)]
    prev[0] = 1
    curr = [p for p in prev]

    for index in range(1, n+1):
        curr[0] = 1
        for target in range(1, k+1):
            nSelect = prev[target]
            select = 0
            if target >= arr[index-1]:
                select = prev[target-arr[index-1]]

            curr[target] = nSelect + select

        prev = curr.copy()

    return curr[-1]


print(findWays([1, 4, 4, 5], 5))


arr = []
string = "7 7 7 9 1 4 4 7 8 2 10 3 9 8 1 9 7 1 2 8 7 3 5 3 9 8 9 7 8 3 2 4 2 6 10 1 6 4 10 5 3 7 1 6 5 6 1 8 6 7 5 1 2 3 5 2 9 10 3 1 2 10 5 7 10 2 7 9 3 4 2 8 10 5"
for n in string.split(" "):
    arr.append(int(n))


print((findWays(arr, 53)) % (10**9+7))
