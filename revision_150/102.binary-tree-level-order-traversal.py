#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        q = [[root]]

        while 1:
            children = []
            for n in q[-1]:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)

            if not children:
                break

            q.append(children)

        
        return [[n.val for n in nodes] for nodes in q]
        
# @lc code=end

