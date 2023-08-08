#
# @lc app=leetcode id=139 lang=python
#
# [139] Word Break
#



# @lc code=start
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        while s and wordDict:
            word = wordDict.pop(0)
            n = len(word)
            if s[:n] != word:
                return False
            s = s[n:]

        print(s, len(wordDict))
        if len(wordDict) > 0:
            return False
        return True



        
# @lc code=end
print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog"]))
