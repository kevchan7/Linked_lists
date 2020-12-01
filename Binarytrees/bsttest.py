from tree_node import tree_node
# Setting up a bst
bst = tree_node(8, tree_node(4), tree_node(12))
bst.left.left = tree_node(2, tree_node(1), tree_node(3))
bst.left.right = tree_node(6, tree_node(5), tree_node(7))
bst.right.left = tree_node(10, tree_node(9), tree_node(11))
bst.right.right = tree_node(14, tree_node(13), tree_node(15))
bst.level_order_traversal(bst)
# trying out my bsts
bst.binarysearchtreesearch(bst, 3)