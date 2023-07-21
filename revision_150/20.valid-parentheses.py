#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 != 0:
            return False
        
        mStack = []
        for c in s:
            if c == "{":
                mStack.append("}")
            elif c == "[":
                mStack.append("]")
            elif c == "(":
                mStack.append(")")
            else:
                if mStack and c == mStack.pop():
                    continue
                return False
            
        if len(mStack) > 0:
            return False
        
        return True
                    

        
# @lc code=end
print(Solution().isValid("()[]{)"))
