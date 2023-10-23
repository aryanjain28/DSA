#
# @lc app=leetcode id=653 lang=python
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        visited = set()

        def dfs(node):
            if not node:
                return False
            
            if (k - node.val) in visited:
                return True
            
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)




        
# @lc code=end

