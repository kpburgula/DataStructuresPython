class BinaryTree:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def pre_order(self):
        print(self.item)
        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.item)
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.item)


class BinarySearchTree:
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None

    def insert(value,root):
        if root is None:
            return root

        if root.left > value:
            return 


bt = BinaryTree('a')
bt.left = BinaryTree('b')
bt.right = BinaryTree('c')
bt.left.left = BinaryTree('d')
bt.left.right = BinaryTree('e')
bt.right.left = BinaryTree('f')

bt.pre_order()
print('%' * 20)
bt.in_order()
print('%' * 20)
bt.post_order()
