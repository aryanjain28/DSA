#
# @lc app=leetcode id=1092 lang=python
#
# [1092] Shortest Common Supersequence 
#

# @lc code=start
class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        n, m = len(str1), len(str2)
        prev = [""] * (m+1)
        curr = [p for p in prev]

        for index1 in range(1, n+1):
            for index2 in range(1, m+1):
                if str1[index1-1] == str2[index2-1]:
                    curr[index2] = prev[index2-1] + str2[index2-1]
                elif len(prev[index2]) > len(curr[index2-1]):
                    curr[index2] = prev[index2]
                else:
                    curr[index2] = curr[index2-1]
            
            prev = [c for c in curr]
    
        lcs = curr[-1]
        if len(lcs) == 0:
            return str1 + str2

        def convert(string, lcs):            
            index = 0
            while lcs:
                if string[index] == lcs[0]:
                    string = string[:index] + string[index:].replace(lcs[0], chr(ord(lcs[0])-32) ,1) 
                    lcs = lcs[1:]
                index += 1
            return string
        
        def merge(str1, str2, lcs):
            res = ""
            while lcs:
                c = lcs[0]

                index1 = str1.index(c)
                index2 = str2.index(c)

                res += str1[:index1] + str2[:index2] + str(c).lower()

                str1 = "" + str1[index1+1:]
                str2 = "" + str2[index2+1:]

                lcs = lcs[1:]
        
            return res + str1 + str2


        c_str1, c_str2 = convert(str1, lcs), convert(str2, lcs)

        return merge(c_str1, c_str2, lcs.upper())


            


        
# @lc code=end
# Solution().shortestCommonSupersequence("abac", "cab")
print(Solution().shortestCommonSupersequence("bbbaaaba", "bbababbb"))