#Stacks implemented using Linked Lists and Arrays

class Node:
  def __init__(self,val):
    self.data = val
    self.next = None

class Stacks:
  def __init__(self):
    self.top = None
    self.bottom =None
    self.length = 0

  def __repr__(self):
    return str(self._prints())

  def peek(self):
    return self.top.data

  def push(self,val):
    new_node = Node(val)
    if self.bottom is None:
      self.top = new_node
      self.bottom = new_node
      self.length+=1
    else:
      new_node.next = self.top
      self.top = new_node
      self.length+=1
      print(self.top.data)


  def pop(self):
    last_item = self.top
    if last_item is not None:
      self.top = self.top.next
      self.length-=1
      return last_item.data
    return last_item

  def _prints(self):
    arr = []
    curr_node = self.top
    while (curr_node!=None):
      arr.append(curr_node.data)
      curr_node = curr_node.next

    return arr

  def is_empty(self):
    if (self.top == None) and (self.bottom == None):
      return True
    else:
      return False


class StackArrays:
  def __init__(self):
    self.data = []
    self.length = 0
  
  def __repr__(self):
    return str(self.data)

  def peek(self):
    return self.data[self.length-1]

  def push(self,val):
    self.data.append(val)
    self.length+=1

  def pop(self):
    last_item = self.data[self.length-1]
    del self.data[self.length-1]
    self.length-=1
    return last_item

  def is_empty(self):
    if self.length == 0:
      return True
    else:
      return False
  

# s = Stacks()
s = StackArrays()
print(s.is_empty())
s.push('first item')
s.push('second item')
s.push('third item')
print(s)
print(s.pop())
print(s.pop())
print(s)
print(s.is_empty())

