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

# Reverse a string

def reverse_string(sentence):
  return ''.join(reversed(sentence))
  
def merged_sorted_array(a,b):
  if len(a) == 0 or len(b) == 0:
    return a+b

  else:
    i=0
    j=0
    myarray = []
    while len(a)>i and len(b)>j:
      if a[i]>=b[j]:
        myarray.append(b[j])
        j+=1
      elif a[i]<=b[j]:
        myarray.append(a[i])
        i+=1

    return myarray + a[i:] + b[j:]

a=[1,3,4,6,20]
b=[2,3,4,5,6,9,11,76]
x=merged_sorted_array(a,b)
print(a)
print(b)
print(x)

