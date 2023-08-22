#
# @lc app=leetcode id=647 lang=python
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dp = {}
        def rec(index, curr):

            if (index, curr) in dp:
                return dp[(index, curr)]

            if index == n:
                if curr and curr == curr[::-1]: 
                    print(curr)
                    return 1
                return 0
            
            dp[(index, curr)] = rec(index+1, s[index] + curr) + rec(index+1, curr)
            return dp[(index, curr)]


        n = len(s)
        rec(1, s[0])
        print(dp)
        
# @lc code=end
print(Solution().countSubstrings("aaa"))
