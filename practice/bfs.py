import trees

bst = trees.BST(4)
root = bst.root


bst.add(root, 3)
bst.add(root, 6)
bst.add(root, 2)
bst.add(root, 5)
bst.add(root, 7)

# print("DFS: ")
# bst.inorder_t(root)

bst.bfs(root)




