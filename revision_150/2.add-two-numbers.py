#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        extra = 0
        curr1 = l1
        curr2 = l2

        dummy = ListNode(-1)
        last = dummy
        while curr1 or curr2:

            v1 = curr1.val if curr1 else 0
            v2 = curr2.val if curr2 else 0

            new_val = v1 + v2 + extra
            last.next = ListNode(new_val % 10)
            last = last.next

            extra = new_val // 10
            
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2
            
        if extra > 0:
            last.next = ListNode(extra)

        return dummy.next
            

        


        
# @lc code=end

