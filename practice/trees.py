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
        self.queue = []

    def preorder_t(self, current):

        if not current:
            return

        # visit left right
        print(current.val, end="-")
        self.preorder_t(current.left)
        self.preorder_t(current.right)

    # Ascending Order.
    def inorder_t(self, current):

        if not current:
            return

        #  left visit right
        self.inorder_t(current.left)
        print(current.val, end="-")
        self.inorder_t(current.right)

    # Descending Order.
    def postorder_t(self, current):

        if not current:
            return

        #  right visit left
        self.postorder_t(current.right)
        print(current.val, end="-")
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

    def minimum_non_recursive(self):
        if not self.root:
            return

        current = self.root
        while current.left:
            current = current.left

        return current.val

    def maxiumu_non_recursive(self):

        if not self.root:
            return

        current = self.root
        while current.right:
            current = current.right

        return current.val

    # case 1: node-to-remove has 0 or 1 child
    # case 2: node-to-remove has 2 children

    def remove(self, current, target):
        if not current:
            return current

        if target > current.val:
            current.right = self.remove(current.right, target)
        elif target < current.val:
            current.left = self.remove(current.left, target)
        else:
            if current.left and current.right:      # 2 child

                leftChild = current.left
                rightChild = current.right

                current = rightChild
                while current.left:
                    current = current.left
                current.left = leftChild

                return rightChild

            elif current.left or current.right:     # 1 child
                return current.left if current.left else current.right
            else:                                   # 0 child
                return None

        return current
    
    def bfs(self, current):

        if current == None:
            return

        print(current.val, end="-")
        if current.left:
            self.queue.append(current.left)
        if current.right:
            self.queue.append(current.right)

        # print([a.val for a in self.queue])

        if self.queue.__len__() < 1:
            return

        current = self.queue[0]
        self.queue = self.queue[1:]
        self.bfs(current)
            
        

        


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
# bst.postorder_t(root)

# print(bst.search(None, 5))

# print(bst.minimum(root))
# print(bst.minimum_non_recursive())

# print(bst.maximum(root))
# print(bst.maxiumu_non_recursive())

# bst = BST(3)
# root = bst.root

# bst.add(root, 1)
# bst.add(root, 4)
# bst.add(root, 0)
# bst.add(root, 2)
# bst.add(root, 5)

# bst.inorder_t(root)

# bst.remove(root, 1)
# print()

# bst.inorder_t(root)



# bst.remove(root, 4)
# bst.remove(root, 5)
# bst.remove(root, 0)
# bst.remove(root, 2)
# bst.remove(root, 1)

