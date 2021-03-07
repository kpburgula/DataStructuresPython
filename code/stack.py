class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self,item):
        self.stack.append(item)
        return self.stack

    def pop(self):
        if self.is_empty():
            return 'Stack is empty'
        self.stack.pop()
        return self.stack


s = Stack()
print(s.stack)
print(s.push('item 1'))
print(s.push('item 2'))
print(s.push('item 3'))
print(s.pop())
