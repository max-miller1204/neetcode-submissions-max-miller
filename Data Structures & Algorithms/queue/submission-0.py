# Doubly Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # Dummy Nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        # Create new Node
        newNode = Node(value)
        curr = self.tail.prev

        # Set tail links to newNode
        self.tail.prev = newNode
        newNode.next = self.tail

        # Set previous node to newNode
        curr.next = newNode
        newNode.prev = curr

    def appendleft(self, value: int) -> None:
        # Create new Node
        newNode = Node(value)
        curr = self.head.next

        # Set head links to newNode
        self.head.next = newNode
        newNode.prev = self.head

        # Set previous node to newNode
        curr.prev = newNode
        newNode.next = curr

    def pop(self) -> int:
        # If queue is empty
        if self.isEmpty():
            return -1
        # assign variables to node being removed and node before
        curr = self.tail.prev
        value = curr.value
        before_cur = curr.prev

        # Set next of previous node to tail
        # Set previous of tail to previous node
        before_cur.next = self.tail
        self.tail.prev = before_cur

        return value

    def popleft(self) -> int:
        # If queue is empty
        if self.isEmpty():
            return -1
        # assign variables to node being removed and node before
        curr = self.head.next
        value = curr.value
        after_cur = curr.next

        # Set next of previous node to tail
        # Set previous of tail to previous node
        self.head.next = after_cur
        after_cur.prev = self.head

        return value
