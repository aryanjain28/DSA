def lcs(str1: str, str2: str) -> int:

    def rec(i1, i2, count, maxi):
        if i2 < 0 or i1 < 0:
            return maxi
        
        if str1[i1] == str2[i2]:
            maxi = max(count, maxi)
            count += 1
        else:
            count = 0
        
        rec(i1, i2-1, count, maxi)
        rec(i1-1, i2, count, maxi)

        return maxi
        
    

    l1, l2 = len(str1), len(str2)
    return rec(l1-1, l2-1, 0, -float("inf"))


    # prev = [0] * (l2+1)
    # curr = [p for p in prev]

    # maxi = -float("inf")
    # for i in range(1, l1+1):
    #     for j in range(1, l2+1):
    #         if str1[i-1] == str2[j-1]:
    #             curr[j] = 1+prev[j-1]
    #             maxi = max(maxi, curr[j])
    #         else:
    #             curr[j] = 0

    #     prev = [c for c in curr]

    # return maxi



print(lcs("abac", "abc"))
print(lcs("wasdijkl", "wsdjkl"))