# Searching
# Travesing
# Min
# Max
# Inserting
# Deleting

class Node:
    def __init__(self, val) -> None:

        self.left = None
        self.right = None
        self.val = val


class BST:
    def __init__(self) -> None:

        self.root = None

    def add(self, current, val):

        # Root
        if not self.root:
            self.root = Node(val)
        else:
            if current.val < val:
                if not current.right:
                    current.right = Node(val)
                else:                
                    self.add(current.right, val)
            else:
                if not current.left:
                    current.left = Node(val)
                else:
                    self.add(current.left, val)




