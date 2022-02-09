class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    # returns the indexth element of the linked list
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    # inserts an element at the indexth position in the linked list
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1
    
    # deletes the indexth element of the linked list
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

    # add a node at the end of the linked list
    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            self.size += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)
        self.size += 1

    # delete the last node of the linked list
    def deleteAtTail(self) -> None:
        if self.head is None:
            return
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        curr.next = None
        self.size -= 1

    # add a node at the beginning of the linked list
    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
