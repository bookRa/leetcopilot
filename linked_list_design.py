# a class that represents a linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def add_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def add_node_at_index(self, index, node):
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            prev = self.get_node_at_index(index - 1)
            node.next = prev.next
            prev.next = node
        self.length += 1
    
    def get_node_at_index(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr
    
    def get_tail(self):
        return self.tail