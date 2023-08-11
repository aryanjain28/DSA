#
# @lc app=leetcode id=516 lang=python
#
# [516] Longest Palindromic Subsequence
#

# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # dp = {}
        # def rec(index1, index2):

        #     if (index1, index2) in dp:
        #         return dp[(index1, index2)]

        #     if index1 < 0 or index2 < 0:
        #         return 0
            
        #     if s1[index1] == s2[index2]: 
        #         dp[(index1, index2)] = 1 + rec(index1-1, index2-1)
        #     else:
        #         r1 = 0 + rec(index1-1, index2)
        #         r2 = 0 + rec(index1, index2-1)                
        #         dp[(index1, index2)] = max(r1, r2)
            
        #     return dp[(index1, index2)]

        n = len(s)
        s1, s2 = s, s[::-1]
        if s1 == s2:
            return n
        # return rec(n-1, n-1)

        prev = [0 for _ in  range(n+1)]
        curr = [p for p in prev]

        for index1 in range(1, n+1):
            for index2 in range(1, n+1):

                if s1[index1-1] == s2[index2-1]:
                    curr[index2] = 1 + prev[index2-1]
                else:
                    r1 = 0 + curr[index2-1]
                    r2 = 0 + prev[index2]
                    curr[index2] = max(r1, r2)

            prev = [c for c in curr]
        
        return curr[-1]

        
# @lc code=end
print(Solution().longestPalindromeSubseq("bbbab"))
print(Solution().longestPalindromeSubseq("cbbd"))
print(Solution().longestPalindromeSubseq("aryan"))
