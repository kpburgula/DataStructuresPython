class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def is_empty(self):
        return len(self._data) == 0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self._data.pop(0)

    def show(self):
        return self._data


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self._data = [None] * self.size
        self.head = -1
        self.tail = -1

    def is_full(self):
        return (self.tail + 1) % self.size == self.head

    def is_empty(self):
        return self.head == -1

    def show_queue(self):
        return self._data

    def enqueue(self, item):
        if self.is_full():
            return "Circular queue is full"

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self._data[self.tail] = item

        else:
            self.tail = (self.tail + 1) % self.size
            self._data[self.tail] = item

    def dequeue(self):
        if self.is_empty():
            return "Circular queue is empty. No items to delete"
        elif self.head == self.tail:
            ele = self._data[self.head]
            self._data[self.head] = None
            self.head = -1
            self.tail = -1
            return ele
        else:
            ele = self._data[self.head]
            self._data[self.head] = None
            self.head = (self.head + 1) % self.size
            return ele


class Dequeue:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add_front(self, item):
        self._data.insert(0, item)

    def add_rear(self, item):
        self._data.append(item)

    def remove_front(self):
        return self._data.pop(0)

    def remove_rear(self):
        return self._data.pop()

    def show(self):
        return self._data


q = Queue()
print(q.dequeue())
q.enqueue('item1')
q.enqueue('item2')
q.enqueue('item3')
print(q.show())
q.dequeue()
print(q.show())

cq = CircularQueue(size=3)
print(cq.dequeue())
cq.enqueue('item1')
cq.enqueue('item2')
cq.enqueue('item3')
print(cq.show_queue())
print(cq.enqueue('item4'))
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.dequeue())
print(cq.enqueue('item4'))
print(cq.show_queue())

de = Dequeue()
print(len(de))
de.add_front('item1')
de.add_front('item2')
de.add_rear('item3')
print(de.show(), len(de))
print(de.remove_front())
print(de.show(), len(de))
