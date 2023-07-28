#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        p_val = min(p.val, q.val)
        q_val = max(p.val, q.val)

        self.minimum = root.val

        def search(node):

            if p_val <= node.val <= q_val:
                return node

            elif q_val < node.val:
                return search(node.left)
            
            else:
                return search(node.right)
            
        res = search(root)
        return res
            


        
        
# @lc code=end

