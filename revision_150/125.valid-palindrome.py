#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

import re
# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # mStr = ""
        # for c in s:
        #     if str.isalnum(str(c)):
        #         mStr += str.lower(str(c))

        s = re.sub(r'[\W_]+', '', s)

        return s == s[::-1]

        # for i in range(len(mStr) // 2):
        #     if mStr[i] != mStr[~i]:
        #         return False
        # return True


        
# @lc code=end
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
