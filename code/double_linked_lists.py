class Node:
  def __init__(self,val):
    self.data = val
    self.next = None
    self.prev = None
  
class DoublyLinkedlist:
  def __init__(self):
    self.head = None
    self.prev = None
    self.next = None
    self.tail = None
    self.length = 0

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      new_node.prev = None
      self.head = new_node
      self.tail = self.head
      self.length = self.length + 1
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
      self.length = self.length + 1
    
    return self.print_list()

  def prepend(self,value):
    new_node = Node(value)
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
    self.length = self.length + 1
    return self.print_list()

  def print_list(self):
    arr = []
    current_node = self.head
    while (current_node!= None):
      arr.append(current_node.data)
      current_node = current_node.next
    return arr

  def insert(self, index, value):
    if index == 0:
      self.prepend(value)
    elif index>=self.length:
      self.append(value)
    else:
      curr_node = self.head
      new_node = Node(value)
      for i in range(1, index+1):
        prev_node = curr_node
        curr_node = curr_node.next
        if i == index:
          prev_node.next = new_node
          new_node.next = curr_node
          new_node.prev = prev_node
          curr_node.prev = new_node
          self.length = self.length + 1
          break
    return self.print_list()

  def remove(self,index):
    if index == 0:
      self.head = self.head.next
      self.length = self.length - 1
      return None
    elif index>=self.length:
      return "Index out of bounds"
    else:
      curr_node = self.head
      for i in range(1,index+1):
        prev_node = curr_node
        curr_node = curr_node.next
        if i == index:
          print(prev_node.data,curr_node.data)
          prev_node.next = curr_node.next
          curr_node.prev = prev_node
          self.length = self.length - 1
          break
      return self.print_list()



l = DoublyLinkedlist()
print(l.append(5))
l.append(8)
l.append(19)
# l.prepend(100)
# print(l.prepend(200))
# print(l.insert(1,'inserted'))
print(l.print_list())
print(l.remove(3))


