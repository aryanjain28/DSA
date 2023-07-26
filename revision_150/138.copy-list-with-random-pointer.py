#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head:
            return None

        index = 0
        nodes = []
        curr = head
        while curr:
            nodes.append(Node(curr.val))
            curr.val = (curr.val, index)
            curr = curr.next
            index += 1

        index = 0
        curr = head
        while curr:
            if curr.random:
                nodes[index].random = nodes[curr.random.val[1]]

            nodes[index].next = nodes[index + 1] if index + 1 < len(nodes) else None
            
            index += 1
            curr = curr.next

        return nodes[0]

        
# @lc code=end

