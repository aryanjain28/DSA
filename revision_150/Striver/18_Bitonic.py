from typing import List

def longestBitonicSubsequence(arr, n):
    

    # def rec(index, last_index):
        
    #     if index == n:
    #         return 0
        
    #     n_select = 0 + rec(index+1, last_index)        
    #     select = 0
    #     if last_index == -1 or arr[index] > arr[last_index]:
    #         select = 1 + rec(index+1, index)

    #     # return max(select, n_select)
        


    def get_lis(arr):
        n = len(arr)

        dp = [[0] * (n+1) for _ in range(n+1)]

        for index in range(n-1, -1, -1):
            for last_index in range(index, -2, -1):
                
                n_select = 0 + dp[index+1][last_index+1]        
                select = 0
                if last_index == -1 or arr[index] > arr[last_index]:
                    select = 1 + dp[index+1][index+1]

                dp[index][last_index+1] = max(select, n_select)

        
        return dp[0]
        # return [p[0] for p in dp]

    inc = get_lis(arr)
    dec = get_lis(arr[::-1])

    print(inc)
    print(dec)
    

    maxi = -1
    for i in range(n):
        if inc[i]+dec[i]-1 > maxi:
            maxi = inc[i]+dec[i]-1

    return maxi



print(longestBitonicSubsequence([1,11,2,10,4,5,2,1], 8))
# print(longestBitonicSubsequence([1,2,1,2,1], 5))
# print(longestBitonicSubsequence([1,2,1,3,4], 5))