#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        mStack = []
        for c in tokens:
            try:
                mStack.append(int(c))
            except:
                n2 = mStack.pop()
                n1 = mStack.pop()
                if c == "+":
                    num = n1 + n2
                elif c == "-":
                    num = n1 - n2
                elif c == "*":
                    num = n1 * n2
                else:
                    num = int(n1 / n2)
                mStack.append(num)

        return mStack.pop()



        
# @lc code=end
print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))




