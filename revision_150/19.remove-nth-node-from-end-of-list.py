#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next 


        count -= n
        curr = head
        while count > 1:
            curr = curr.next
            count -= 1

        curr.next = curr.next.next
        return head

        

        
# @lc code=end

