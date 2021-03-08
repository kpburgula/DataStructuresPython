class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def add_after(self, node, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = node.next
            node.next = new_node

    def delete(self, position):

        if self.head is None:
            return "No node"
        if position == 0:
            temp = self.head.item
            self.head = self.head.next
            return temp
        temp_node = self.head
        for i in range(position - 1):
            temp_node = temp_node.next
            if (temp_node is None) or (temp_node.next is None):
                return

        next_node = temp_node.next.next
        temp_node.next = next_node

    def print_list(self):
        temp_node = self.head
        while temp_node:
            print(str(temp_node.item) + " ", end="")
            temp_node = temp_node.next


ll = LinkedList()
ll.add_beginning('item1')
ll.add_beginning('item2')
ll.add_end('item3')
ll.add_after(ll.head.next, 'item4')
ll.print_list()
