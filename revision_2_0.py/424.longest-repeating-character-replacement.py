#
# @lc app=leetcode id=424 lang=python
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        maxi = 0

        counter = [0] * 26

        i = 0
        j = 0
        

        while j < len(s):
            curr_char = s[j]
            counter[ord(curr_char)-ord("A")] += 1
                
            curr_len = j - i + 1
            curr_max = max(counter)

            if curr_len - curr_max <= k:
                maxi = max(maxi, curr_len)
            else:
                counter[ord(s[i])-ord("A")] -= 1
                i += 1
                

            j += 1

        return maxi
            







        
# @lc code=end

Solution().characterReplacement("AABABBA", 1)
Solution().characterReplacement("ABAB", 2)