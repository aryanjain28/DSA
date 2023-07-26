#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        dummy = ListNode(-1)
        dummy.next = head
        
        slow, fast = dummy, head 
        while fast and fast.next:

            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False
        
# @lc code=end

