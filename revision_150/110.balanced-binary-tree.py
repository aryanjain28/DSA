#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(node):

            if not node:
                return 0, True

            if not node.left and not node.right:
                return 1, True
            
            h_l, bal_l = dfs(node.left)
            h_r, bal_r =  dfs(node.right)

            cond = bal_l and bal_r and abs(h_l - h_r) <= 1

            return max(h_l + 1, h_r + 1), cond

        return dfs(root)[1]



            
        
# @lc code=end

