#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        q1 = [p]
        q2 = [q]

        while q1 and q2:
            node1 = q1.pop()
            node2 = q2.pop()

            if not node1 and not node2:
                continue

            if (node1 and not node2) or (not node1 and node2):
                return False

            if node1.val != node2.val:
                return False
            
            q1.append(node1.left)
            q1.append(node1.right)

            q2.append(node2.left)
            q2.append(node2.right)

            
        return True




        
# @lc code=end

