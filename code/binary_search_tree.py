class Node:
  def __init__(self,val):
    self.data = val
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self,val):
    new_node = Node(val)
    if self.root is None:
      self.root = new_node
    else:
      curr_node = self.root
      while True:
        if (val<curr_node.data):
          if(curr_node.left == None):
            curr_node.left = new_node
            break
          else:
            curr_node = curr_node.left
        elif (val>curr_node.data):
          if(curr_node.right == None):
            curr_node.right = new_node
            break
          else:
            curr_node = curr_node.right

  def lookup(self,val):
    curr_node = self.root
    while True:
      if curr_node is None:
        return False

      if curr_node.data == val:
        return True
      elif val < curr_node.data:
        curr_node = curr_node.left
      else:
        curr_node = curr_node.right

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
print(bst.print_tree())
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)

