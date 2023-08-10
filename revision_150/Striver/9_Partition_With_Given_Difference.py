

def countPartitions(n: int, d: int, nums: list) -> int:

    arr = []
    zero_count = 0
    for a in nums:
        if a != 0:
            arr.append(a)
            continue
        zero_count += 1

    total = sum(arr)
    if (total + d) % 2:
        return 0

    k = (total + d) / 2
    n = len(arr)

    dp = {}

    def rec(index: int, target: int):

        if (index, target) in dp:
            return dp[(index, target)]

        # base
        if target == 0:
            return 1

        if index < 0:
            return 0

        nSelect = rec(index-1, target)

        select = 0
        if target >= arr[index]:
            select = rec(index-1, target-arr[index])

        dp[(index, target)] = select + nSelect
        return select + nSelect

    prev = [0 for i in range(int(k)+1)]
    prev[0] = 1
    curr = [p for p in prev]

    for index in range(1, n+1):
        for target in range(1, int(k)+1):

            nSelect = prev[target]
            select = 0
            if target >= arr[index-1]:
                select = prev[target-arr[index-1]]

            curr[target] = select + nSelect
        prev = [c for c in curr]

    res = curr[-1]
    # res = rec(n-1, k)
    # print(k)

    # print(zero_count)
    return (res*(2**zero_count)) % (10**9+7)
    # print(get_mod(curr[-1]), get_mod(rec(n-1, k)))


# print(countPartitions(4, 3, [5, 2, 6, 4]))
# print(countPartitions(4, 0, [1, 1, 1, 1]))
# print(countPartitions(3, 1, [4, 6, 3]))
# print(countPartitions(6, 17, [1, 0, 8, 5, 1, 4]))
# print(countPartitions(6, 10, [0, 0, 3, 6]))
