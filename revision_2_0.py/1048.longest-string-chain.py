#
# @lc app=leetcode id=1048 lang=python
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def isPred(index1, index2):
            w1, w2 = words[index1], words[index2]
            if len(w2) + 1 != len(w1): return False

            for i, c in enumerate(w1):
                if w1[:i] + w1[i+1:] == w2:
                    return True

            return False
                
        # dp = {}
        # def rec(index1, index2):
            

        #     if (index1, index2) in dp:
        #         return dp[(index1, index2)]

        #     if index1 == n:
        #         return 0
                        
        #     not_select = 0 + rec(index1+1, index2)

        #     select = 0
        #     if index2 == -1 or isPred(index1, index2):
        #         select = 1 + rec(index1+1, index1)


        #     dp[(index1, index2)] = max(select, not_select)
        #     return dp[(index1, index2)]
            
        words = sorted(words, key=len)
        n = len(words)
        # # return 1 if n == 1 else rec(0, -1)
        if n == 1:
            return 1

        prev = [0] * (n+1)
        curr = [0] * (n+1)
        
        
        for index1 in range(n-1, -1, -1):
            for index2 in range(index1, -2, -1):
                                        
                not_select = 0 + prev[index2+1]

                select = 0
                if index2 == -1 or isPred(index1, index2):
                    select = 1 + prev[index1+1]

                curr[index2+1] = max(select, not_select)

            prev = [c for c in curr]

        return curr[0]
        # return dp[0][0]



        
# @lc code=end
# print(Solution().longestStrChain(["ba","bca"]))
# print(Solution().longestStrChain(["a","ab", "abc"]))
# print(Solution().longestStrChain(["xbc","pcxbcf","xb","cxbc","pcxbc"]))
print(Solution().longestStrChain(["abcd","abxcd"]))
