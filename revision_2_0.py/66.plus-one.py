#
# @lc app=leetcode id=66 lang=python
#
# [66] Plus One
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """


        last = 1
        index = len(digits) - 1
        while index >= 0:
        
            digits[index] += last
            last = 0

            if digits[index] > 9:
                digits[index] = digits[index] % 10
                last = 1

            index -= 1

        return [last] + digits if last > 0 else digits 

        
# @lc code=end

print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([9,9]))