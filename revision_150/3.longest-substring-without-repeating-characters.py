#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0


        curr = s[0]
        index = 1
        maxim = 1
        while index < len(s):
            if s[index] not in curr:
                curr += s[index]
                index += 1
            else:
                curr = curr[1:]

            
            maxim = len(curr) if len(curr) > maxim else maxim 

        return maxim



        
# @lc code=end
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))

