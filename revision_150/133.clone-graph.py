#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, root: Node):
        """
        :type node: Node
        :rtype: Node
        """


        def dfs(node):

            if not node:
                return None

            if node.val in newNodes:
                return newNodes[node.val]

            newNodes[node.val] = newNodes.get(node.val, Node(node.val))

            for neighbor in node.neighbors:
                newNodes[node.val].neighbors.append(dfs(neighbor))

            return newNodes[node.val]


        newNodes = {}
        return dfs(root)





        
# @lc code=end

