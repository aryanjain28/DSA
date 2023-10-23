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
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not list1 or not list2:
            return list1 if list1 else list2
        
        
        if list1.val <= list2.val:
            node = list1
            other = list2
        else:
            node = list2
            other = list1


        head = node
        next = node.next
        while next and other:

            if next.val > other.val:
                node.next = other
                other = next
            
            node = node.next
            next = node.next    


        node.next = other
        return head


            


        


# @lc code=end

