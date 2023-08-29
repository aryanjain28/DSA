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

        # def sametree(n1, n2):

        #     q1 = [n1]
        #     q2 = [n2]

        #     while q1 and q2:

        #         node1 = q1.pop(0)
        #         node2 = q2.pop(0)

        #         if not node1 and not node2:
        #             return True
                
        #         if (not node1 and node2) or (node1 and not node2):
        #             return False
                
        #         if node1.val != node2.val:
        #             return False
                
        #         if node1.left:
        #             q1.append(node1.left)
        #         if node2.left:
        #             q2.append(node2.left)
                
                
        #         if len(q1) != len(q2):
        #             return False

        #         if node1.right:
        #             q1.append(node1.right)
        #         if node2.right:
        #             q2.append(node2.right)


        #         if len(q1) != len(q2):
        #             return False

                

        #     if len(q1) == len(q2):               
        #         return True
            
        #     return False


        def isSameTree(p, q):

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


        q = [root]

        while q:
            node = q.pop(0)
            
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return False



        
# @lc code=end

