#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if len(s1) > len(s2):
            return False
        
        def get_n(char):
            return ord(char) - ord("a")
        
        matches_s1 = [0] * 26
        matches_s2 = [0] * 26

        for index in range(len(s1)):
            matches_s1[get_n(s1[index])] += 1
            matches_s2[get_n(s2[index])] += 1



        i = 0
        j = len(s1) - 1
        while j < len(s2):

            # print(i, j, matches_s2)

            if matches_s1 == matches_s2:
                return True
                
            matches_s2[get_n(s2[i])] -= 1

            i += 1
            j += 1

            if j < len(s2):
                matches_s2[get_n(s2[j])] += 1

        
        return False





        
        # window_size = len(s1)
        # i = 0
        # j = window_size - 1

        # sorted_s1 = sorted(s1)

        # while j < len(s2):

        #     if sorted_s1 == sorted(s2[i:j+1]):
        #         return True


        #     i += 1
        #     j += 1
        

        # return False


        
# @lc code=end

Solution().checkInclusion("ab", "eidbaooo")