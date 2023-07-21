#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

import heapq
# @lc code=start
class MinStack(object):

    def __init__(self):
        self.stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.stack[-1][1])))
    
    def pop(self):
        """
        :rtype: None
        """
        # print(self.stack)
        # print(self.minimum)

        return self.stack.pop()[0]
        

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


# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(4)
print(obj.getMin())
obj.pop()
obj.pop()
print(obj.top())
print(obj.getMin())
