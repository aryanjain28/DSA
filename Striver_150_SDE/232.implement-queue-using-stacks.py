#
# @lc app=leetcode id=232 lang=python
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.start = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: int
        """
        # if self.start < 0:
        #     return None
                
        val = self.stack[self.start]
        self.start += 1
        return val
    

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[self.start]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) <= self.start
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

