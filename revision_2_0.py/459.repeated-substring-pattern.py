#
# @lc app=leetcode id=459 lang=python
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        LEN = len(s)
        
        index = 1
        while index <= LEN // 2:

            if LEN % index == 0:
                s_ = s[:index] * (LEN // index)
                if s ==  s_: return True
        
            index += 1

        return False


        
# @lc code=end

print(Solution().repeatedSubstringPattern("babbabbabbabbab"))