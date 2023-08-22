#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if len(self.stack) == 0:
            self.stack.append((val, val))
            return


        if val < self.stack[-1][1]:
            self.stack.append((val, val))
        else:
            self.stack.append((val, self.stack[-1][1]))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.stack)


param_4 = obj.getMin()
print(param_4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_4)
print(param_3)



# @lc code=end

