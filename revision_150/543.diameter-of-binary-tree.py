#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.mx = 0
        def dfs(node):

            if not node:
                return 0
            
            if not node.left and not node.right:
                return 1
            
            l = 1 + dfs(node.left)
            r = 1 + dfs(node.right)

            self.mx = max(self.mx, l+r-2)
            return max(l, r)
        
        
        dfs(root)
        return self.mx
        
# @lc code=end
Solution().diameterOfBinaryTree([1])
