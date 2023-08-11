
def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    
    dp = {}
    def rec(index1, index2):
        
        if (index1, index2) in dp:
            return dp[(index1, index2)]

        if index1 < 0 or index2 < 0:
            return ""
        
        if s1[index1] == s2[index2]:
            res = rec(index1-1, index2-1) + s1[index1]
        else:
            r1 = rec(index1, index2-1)
            r2 = rec(index1-1, index2)
           
            l1, l2 = len(r1), len(r2)

            res = r1 if l1 > l2 else r2
        
        dp[(index1, index2)] = res
        return res


    # res = rec(n-1, m-1)
    # return res 

    prev = [""] * (m+1)
    curr = [p for p in prev]

    for index1 in range(1, n+1):
        for index2 in range(1, m+1):

            if s1[index1-1] == s2[index2-1]:
                curr[index2] = prev[index2-1] + s1[index1-1]
            elif len(curr[index2-1]) > len(prev[index2]):
                curr[index2] = curr[index2-1]
            else:
                curr[index2] = prev[index2]
        
        prev = [c for c in curr]

    return curr[-1]







print(findLCS(5, 4, "abcab", "cbab"))
print(findLCS(11, 11, "ldxgoohkumo", "cqyxwraowfz"))
