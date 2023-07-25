#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, head1, head2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head1 and  not head2:
            return None
        
        if not head1 or not head2:
            return head2 if head2 else head1        

        curr, next = None, None
        if head1.val <= head2.val:
            curr = head1
            next = head2
        else:
            curr = head2
            next = head1
        
        head = curr

        while curr.next and next:
            if curr.next.val < next.val:
                curr = curr.next
            else:
                temp = curr.next
                curr.next = next
                curr = next
                next = temp

        curr.next = next
        
        return head

        




        




        
# @lc code=end

