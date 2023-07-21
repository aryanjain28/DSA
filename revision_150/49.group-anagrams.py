#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        

        freq = {}
        for s in strs:
            s_str = "".join(sorted(s))            
            freq[s_str] = freq.get(s_str, [])
            freq[s_str].append(s)


        return freq.values()
            
        
# @lc code=end
Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
