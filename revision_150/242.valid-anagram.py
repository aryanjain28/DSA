#
# @lc app=leetcode id=242 lang=python
#
# [242] Valid Anagram
#

from collections import Counter

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        return Counter(s) == Counter(t)
        
        # return sorted(s) == sorted(t)









        
# @lc code=end

