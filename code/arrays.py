class Array:

  def __init__(self):
    self.data = {}
    self.length = 0

  def __repr__(self):
    return str(self.data)

  def push(self,item):
    self.data[self.length] = item
    self.length+=1

  def pop(self):
    last_item = self.data[self.length - 1]
    del self.data[self.length - 1]
    self.length-=1
    return last_item

  def get(self,index):
    return self.data[index]

  def delete(self,index):
    item = self.data[index]
    for i in range(index, self.length-1):
      self.data[i] = self.data[i+1]
    self.length-=1
    del self.data[self.length-1]
    return item

  
  

a = Array()
a.push('first item')
a.push('second item')
a.push('third item')
a.push('fourth item')
# print(a)
# a.pop()
print(a.delete(2))
print(a)
  

