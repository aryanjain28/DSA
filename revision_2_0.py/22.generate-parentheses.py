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
        stack = []

        def rec(curr, n, stack):

            if n == 0:
                for c in stack:
                    curr += c
                res.append(curr)
                return

            rec(curr + "(", n-1, stack + [")"])

            if stack:
                rec(curr + stack.pop(-1), n, stack)


        rec("", n, stack)
        return res


        
# @lc code=end
print(Solution().generateParenthesis(8))
