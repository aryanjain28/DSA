class Node:

    def __init__(self, val = 0) -> None:
        
        self.left = None
        self.right = None
        self.val = val

class TreeNode:

    def __init__(self, val) -> None:
        
        self.root = Node(val)


root = TreeNode(3)