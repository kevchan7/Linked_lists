from datastructures import *


class tree_node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def preorder_traversal(self, root) -> object:
        res = []
        if root:
            res.append(root.val)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def postorder_traversal(self, root) -> object:
        res = []
        if root:
            res = res + self.postorder_traversal(root.left)
            res = res + self.postorder_traversal(root.right)
            res.append(root.val)
        return res

    def inorder_traversal(self, root) -> object:
        res = []
        if root:
            res = res + self.inorder_traversal(root.left)
            res.append(root.val)
            res = res + self.inorder_traversal(root.right)
        return res

    def level_order_traversal(self, root) -> object:
        print("Level order list:")
        print([root.val])
        rootlist = [root.left, root.right]
        while rootlist:
            newrootlist = []
            levellist = []
            for x in rootlist:
                if x:
                    newrootlist = newrootlist + [x.left, x.right]
                    levellist = levellist + [x.val]
            print(levellist)
            rootlist = newrootlist

    def inorderiterative(self, root) -> object:
        print("Inorder traversal, iterative approach")
        rootlist = Stack([root])
        i = 10
        while i > 0:
            i = i - 1
            x = rootlist.read()
            if x.left:
                rootlist.stacking(x.left)
                continue
            print(x.val)
            if x.right:
                rootlist.stacking(x.right)
                continue

    def binarysearchtreesearch(self, root, target):
        x = root
        path = []
        while x.val != target:
            if x.val > target:
                x = x.left
                path = path + ["left",]
                continue
            if x.val < target:
                x = x.right
                path = path + ["right",]
            if x.left == None:
                break
            if x.right == None:
                break
        if x.val == target:
            print(target, " found through path:", path)
        if x.val != target:
            print(target, " was not found within list")
