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

        def dfs(node1, node2):

            if not node1 and not node2:
                return True
            
            if not node1 or not node2 or node1.val != node2.val:
                return False

            l = dfs(node1.left, node2.left)
            r = dfs(node1.right, node2.right)

            return l and r
        
        return dfs(p, q)
            





        # if not p and not q:
        #     return True
        
        # if (p and not q) or (not p and q):
        #     return False

        # q1 = [p]
        # q2 = [q]

        # while q1 and q2:

        #     node1, node2 = q1.pop(0), q2.pop(0) 

        #     if (node1 and not node2) or (not node1 and node2):
        #         return False
            
        #     if not node1 and not node2:
        #         continue
    
        #     if node1.val != node2.val:
        #         return False
      
        #     q1.append(node1.left)
        #     q1.append(node1.right)
 
        #     q2.append(node2.left)
        #     q2.append(node2.right)
            

        # return True



        
# @lc code=end

