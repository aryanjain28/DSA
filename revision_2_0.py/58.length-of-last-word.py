#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        return len(s.split()[-1])

        # for s in s.split(" "):
        #     if len(s) <= 0: continue
        #     l = len(s)
            
        # return l




        
# @lc code=end
Solution().lengthOfLastWord("   fly me   to   the moon  ")
