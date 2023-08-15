

def printingLongestIncreasingSubsequence(arr, n):
    

    dp = {}
    def rec(index, prev_index):
        
        if (index, prev_index) in dp:
            return dp[(index, prev_index)]

        if index == n:
            return []
        
        select = []
        if prev_index == -1 or arr[index] > arr[prev_index]:
            select = [arr[index]] + rec(index+1, index)

        nSelect = rec(index+1, prev_index)

        dp[(index, prev_index)] = select if len(select) > len(nSelect) else nSelect
        return dp[(index, prev_index)]
    
    # return rec(0, -1)

    dp = [[[]] * (n+1) for _ in range(n+1)]

    for index in range(n-1, -1, -1):
        for prev_index in range(index, -2, -1):

            select = []
            if prev_index == -1 or arr[index] > arr[prev_index]:
                select = [arr[index]] + dp[index+1][index+1]

            nSelect = dp[index+1][prev_index+1]
            dp[index][prev_index+1] = select if len(select) > len(nSelect) else nSelect


    return dp[0][0]




print(printingLongestIncreasingSubsequence([5,6,3,4,7,6], 6))
print(printingLongestIncreasingSubsequence([1,2,3,4,5], 5))