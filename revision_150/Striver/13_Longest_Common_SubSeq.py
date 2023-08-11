


def lcs(string1: str, string2: str):
    

    dp = {}
    def rec(index1, index2):
        
        if (index1, index2) in dp:
            return dp[(index1, index2)]

        if (index1 < 0) or (index2 < 0):
            return 0
        

        if string1[index1] == string2[index2]:
            dp[(index1, index2)] = 1 + rec(index1-1, index2-1)
            return dp[(index1, index2)]

        dp[(index1, index2)] = 0 + max(rec(index1-1, index2), rec(index1, index2-1))
        return dp[(index1, index2)]
    
    res = rec(len(string1)-1, len(string2)-1)
    return res


print(lcs("acd", "ced"))



