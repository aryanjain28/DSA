#
# @lc app=leetcode id=230 lang=python
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import heapq
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        heap = []
        def dfs(node):

            if not node:
                return 
            
            heapq.heappush(heap, node.val)

            dfs(node.left)            
            dfs(node.right)            


        dfs(root)
        while k > 0 + 1:
            heapq.heappop(heap)            
            k -= 1

        return heapq.heappop(heap)            




        
# @lc code=end

Solution().kthSmallest()