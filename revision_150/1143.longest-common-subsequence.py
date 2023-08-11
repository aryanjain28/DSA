#
# @lc app=leetcode id=1143 lang=python
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        dp = {}
        def rec(index1, index2):
            
            if (index1, index2) in dp:
                return dp[(index1, index2)]
            
            if index1 < 0 or index2 < 0:
                return 0
            
            if text1[index1] == text2[index2]:
                dp[(index1, index2)] = 1 + rec(index1-1, index2-1)
            else:
                dp[(index1, index2)] = 0 + max(rec(index1-1, index2), rec(index1, index2-1))

            return dp[(index1, index2)]

        # return rec(len(text1)-1, len(text2)-1)

        n, m = len(text1), len(text2) 

        prev = [0] * (m+1)
        curr = [0] * (m+1)

        for index1 in range(1, n+1):
            for index2 in range(1, m+1):
                if text1[index1-1] == text2[index2-1]:
                    curr[index2] = 1 + prev[index2-1]
                else:
                    curr[index2] = 0 + max(prev[index2], curr[index2-1])

            prev = [c for c in curr]

        return curr[-1]

        
# @lc code=end
Solution().longestCommonSubsequence("acd", "ced")
Solution().longestCommonSubsequence("abcde", "ace")
