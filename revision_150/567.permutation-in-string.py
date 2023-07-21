#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

from collections import Counter
# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """


        matches = 0
        l = len(s1) 

        count1 = [0] * 26
        for c in s1:
            count1[ord(c)-97] += 1

        count2 = [0] * 26        
        for c in s2[:l]:
            count2[ord(c)-97] += 1

        for index in range(26):
            if count1[index] == count2[index]:
                matches += 1    

        if matches == 26:
            return True

        i = 1 
        while i <= len(s2)-l:

            prev_c = ord(s2[i-1])-97
            next_c = ord(s2[i+l-1])-97
            
            count2[prev_c] -= 1
            if count1[prev_c] == count2[prev_c]:
                matches += 1
            elif count1[prev_c] == count2[prev_c] + 1:
                matches -= 1


            count2[next_c] += 1
            if count1[next_c] == count2[next_c]:
                matches += 1
            elif count1[next_c] == count2[next_c] - 1:
                matches -= 1

            if matches == 26:
                return True
            

            i += 1

        return False
            

        
# @lc code=end
print(Solution().checkInclusion("ab", "eidboaooo"))
# print(Solution().checkInclusion("a", "ab"))
# print(Solution().checkInclusion("adc", "dcda"))
# print(Solution().checkInclusion("abc", "bbbca"))
