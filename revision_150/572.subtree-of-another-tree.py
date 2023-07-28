#
# @lc app=leetcode id=572 lang=python
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def isSameTree(n1, n2):

            if not n1 and not n2:
                return True
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            l = isSameTree(n1.left, n2.left)
            r = isSameTree(n1.right, n2.right)

            return l and r
            

        def dfs(node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2:
                return False

            if isSameTree(node1, node2):
               return True
            
            l = dfs(node1.left, node2)
            r = dfs(node1.right, node2)

            return l or r
  
        
        return dfs(root, subRoot)

        
# @lc code=end

