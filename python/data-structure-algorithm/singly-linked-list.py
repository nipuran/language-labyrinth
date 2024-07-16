class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        """Appends a node with the given data to the end of the list."""
        node = Node(data)

        if self.tail is None:  # If the list is empty
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def preappend(self, data):
        """Pre-appends a node with the given data to the beginning of the list."""
        node = Node(data)

        if self.head is None:  # If the list is empty
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def remove(self, index):
        """Removes a node at the specified index."""
        if self.head is None:
            print("List is empty")
            return

        if index < 0 or index >= self.length:
            print("Index out of range")
            return

        i = 0
        prev, curr = None, self.head
        while i < index:
            prev = curr
            curr = curr.next
            i += 1

        if curr == self.head:  # Remove head
            self.head = curr.next
            if self.head is None:  # If the list becomes empty
                self.tail = None
        elif curr == self.tail:  # Remove tail
            self.tail = prev
            self.tail.next = None
        else:  # Remove middle node
            prev.next = curr.next

        self.length -= 1

    def insert(self, index, data):
        """Inserts a node with the given data at the specified index."""
        if index < 0:
            print("Index cannot be negative")
            return

        node = Node(data)
        
        if self.head is None:  # If the list is empty
            self.head = node
            self.tail = node
            self.length += 1
            return

        if index == 0:  # Insert at head
            node.next = self.head
            self.head = node
            self.length += 1
            return

        i = 0
        prev, curr = None, self.head
        while i < index and curr:
            prev = curr
            curr = curr.next
            i += 1

        if curr is None:  # Insert at tail
            prev.next = node
            self.tail = node
        else:  # Insert in the middle
            prev.next = node
            node.next = curr

        self.length += 1

    def print(self):
        """Prints the elements of the linked list."""
        curr = self.head
        while curr:
            print(curr.data, " -> ", end="")
            curr = curr.next
        print(None)
