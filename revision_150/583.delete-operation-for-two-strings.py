#
# @lc app=leetcode id=583 lang=python
#
# [583] Delete Operation for Two Strings
#

# @lc code=start
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = {}
        def rec(index1, index2):
            if (index1, index2) in dp:
                return dp[(index1, index2)]

            if index1 < 0 or index2 < 0:
                return 0
            
            if word1[index1] == word2[index2]:
                res = 1 + rec(index1-1, index2-1)
            else:
                r1 = rec(index1-1, index2)
                r2 = rec(index1, index2-1)
                res = max(r1, r2)

            dp[(index1, index2)] = res
            return res

        n, m = len(word1), len(word2)
        # r = rec(n-1, m-1)

        prev = [0] * (m+1)
        curr = [p for p in prev]

        for index1 in range(1, n+1):
            for index2 in range(1, m+1):

                if word1[index1-1] == word2[index2-1]:
                    curr[index2] = 1 + prev[index2-1]
                else:
                    r1 = prev[index2]
                    r2 = curr[index2-1]
                    curr[index2] = max(r1, r2)

            prev = [c for c in curr]

        r = curr[-1]
        
        s = 0
        if n >= r:
            s += (n-r)
        if m >= r:
            s += (m-r)

        return s

        
# @lc code=end
print(Solution().minDistance("leetcode", "etco"))