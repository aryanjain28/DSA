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

        count = [0] * 26
        maximum = 0

        i, j = 0, 0
        while j < len(s) and j >= i:

            count[ord(s[j])-65] += 1

            window_size = j - i + 1
            most_freq = max(count)

            if window_size - most_freq <= k:
                maximum = max(window_size, maximum)
                j += 1
            else:
                count[ord(s[i])-65] -= 1
                count[ord(s[j])-65] -= 1
                i += 1


        print(maximum)
        return maximum




        
# @lc code=end
Solution().characterReplacement("AABABBA", k=1)
