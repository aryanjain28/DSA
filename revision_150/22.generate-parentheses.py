#
# @lc app=leetcode id=22 lang=python
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        res = []
        def rec(left, right, curr):
            if left + right == n*2:
                res.append(curr)
                return

            if left < n:            
                rec(left + 1, right, curr + "(")

            if right < left:
                rec(left, right + 1, curr + ")")
        
        rec(0, 0, "")
        return res





        
# @lc code=end
Solution().generateParenthesis(3)

