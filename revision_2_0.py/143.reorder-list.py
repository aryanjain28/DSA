#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        dummy = ListNode(-1, head)
        slowPointer = dummy
        fastPointer = dummy

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next

        curr = slowPointer.next
        slowPointer.next = None

        # reversing
        last = None
        while curr:
            next = curr.next
            curr.next = last
            last = curr
            curr = next


        # merging
        curr1 = head
        curr2 = last

        while curr1:
            n1 = curr1.next
            curr1.next = curr2

            curr1 = curr2
            curr2 = n1



        






        
# @lc code=end

