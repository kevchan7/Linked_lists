
from tree_node import tree_node


def test_btrees():
    rooted = tree_node(1)
    rooted.left = tree_node(4)
    rooted.right = tree_node(2)
    rooted.right.right = tree_node(3)
    print(rooted.preorder_traversal(rooted))
    assert rooted.preorder_traversal(rooted) == [1, 4, 2, 3]
    print(rooted.postorder_traversal(rooted))
    assert rooted.postorder_traversal(rooted) == [4, 3, 2, 1]
    print(rooted.inorder_traversal(rooted))
    assert rooted.inorder_traversal(rooted) == [4, 1, 2, 3]
    rooted.level_order_traversal(rooted)
test_btrees()



#rooted.inorderiterative(rooted) given up for now


