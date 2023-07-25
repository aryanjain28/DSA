#
# @lc app=leetcode id=143 lang=python
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head.next:
            return head

        dummy = ListNode(0, head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        first, second = head, slow.next
        slow.next = None

        # reverse the scond one
        curr = second
        last = None
        while curr:
            next = curr.next
            curr.next = last
            last = curr
            curr = next



        # merging
        first, second = head, last
        while first:
            first_next = first.next
            second_next = second.next

            first.next = second
            if not first_next:
                break

            second.next = first_next

            first = first_next
            second = second_next


        




            




# @lc code=end

