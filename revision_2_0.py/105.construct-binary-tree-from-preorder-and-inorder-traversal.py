#
# @lc app=leetcode id=105 lang=python
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
class TreeNode(object):
    def __init__(self, v=0, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # LEN = len(inorder)

        # mDict = {}
        # for i, v in enumerate(inorder):
        #     mDict[v] = i


        # def dfs():

        #     val = preorder.pop(0)
        #     node = TreeNode(val)
        #     index = mDict[val]
        #     inorder[index] = None

        #     # left
        #     if index > 0 and inorder[index-1] != None:
        #         node.left = dfs()

        #     # right
        #     if index < LEN-1 and inorder[index+1] != None:
        #         node.right = dfs()

        #     return node
        
        # return dfs()

        LEN = len(inorder)
        in_ = {}
        for index in range(len(inorder)):
            in_[inorder[index]] =  index

        def rec():

            v = preorder.pop(0)
            node = TreeNode(v)
            index = in_[v]
            inorder[index] = None

            if index > 0 and inorder[index-1] != None:
                node.left = rec()

            if index < LEN-1 and inorder[index+1] != None:
                node.right = rec()

            return node
        
        return rec()



        
        
# @lc code=end
Solution().buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
