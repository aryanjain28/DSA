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
    def __init__(self, val) -> None:
        self.root = Node(val)

    def preorder_t(self, current):

        if not current:
            return

        # visit left right
        print(current.val, ", ", end="")
        self.preorder_t(current.left)
        self.preorder_t(current.right)

    # Ascending Order.
    def inorder_t(self, current):

        if not current:
            return

        #  left visit right
        self.inorder_t(current.left)
        print(current.val, ", ", end="")
        self.inorder_t(current.right)

    # Descending Order.
    def postorder_t(self, current):

        if not current:
            return

        #  right visit left
        self.postorder_t(current.right)
        print(current.val, ", ", end="")
        self.postorder_t(current.left)

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

    def search(self, current, target):

        if not current:
            return False

        def find(current, target):
            if current.val > target:
                return self.search(current.left, target)
            elif current.val < target:
                return self.search(current.right, target)

            return True

        return find(current, target)

    def minimum(self, current):

        if current == None:
            return "Invalid"

        if current.left == None:
            return current.val

        return self.minimum(current.left)
    
    def minimum(self, current):

        if current == None:
            return "Invalid"

        if current.left == None:
            return current.val

        return self.minimum(current.left)
    
    def maximum(self, current):

        if current == None:
            return "Invalid"
        
        if current.right == None:
            return current.val
        
        return self.maximum(current.right)


bst = BST(7)
root = bst.root

bst.add(root, 5)
bst.add(root, 3)
bst.add(root, 6)
bst.add(root, 4)
bst.add(root, 12)
bst.add(root, 8)
bst.add(root, 13)

# bst.preorder_t(root)
# bst.inorder_t(root)
bst.postorder_t(root)

print(bst.search(None, 5))

print(bst.minimum(root))
print(bst.maximum(root))
