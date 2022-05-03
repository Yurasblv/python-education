"""Module for creating base linked list """


class Node:
    """Class node have attributes of current node and node past current node"""

    def __init__(self, node_value=None, next_value=None):
        self.node_value = node_value
        self.next_value = next_value


class LinkedList:
    """Class that performs list"""

    def __init__(self):
        self.head_value = None
        self.idx = 0

    def __iter__(self):
        node = self.head_value
        while node:
            yield node
            node = node.next_value

    def __getitem__(self, index):
        if index < 0:
            index = self.idx + index
        if index > self.idx - 1:
            return "Index out of range!"
        current = self.head_value
        for _ in range(index):
            current = current.next_value
        return current.node_value

    def lenght(self):
        if self.__empty():
            return 0
        head = self.head_value
        count = 0
        while head:
            count += 1
            head = head.next_value
        return count

    def prepend(self, val):
        """Add new node at beginning"""
        new_head = Node(val)
        new_head.next_value = self.head_value
        self.head_value = new_head

    def append(self, val=None):
        """Add new to node to the end of list"""
        new_head = Node(val)
        if self.head_value is None:
            self.head_value = new_head
        else:
            last = self.head_value
            while last.next_value:
                last = last.next_value
            last.next_value = new_head
        self.idx += 1

    def insert(self, val, idx):
        """Add new node at index"""
        node = Node(val)
        current = self.head_value
        if idx < 0 or idx > self.lenght():
            raise Exception("invalid input")
        if idx == 0:
            self.head_value = node
            self.head_value.next_value = current
        while current is not None:
            if self.idx == idx:
                node.next_value = Node(val, node.next_value)
                current.next_value = node
                break
            current = current.next_value
        self.idx += 1

    def __listprint(self):
        """Print all values from list"""
        print_value = self.head_value
        while print_value is not None:
            yield print_value.node_value
            print_value = print_value.next_value

    def lookup(self, val):
        """Check available of value"""
        while self.head_value:
            if val == self.head_value.node_value:
                return True
            self.head_value = self.head_value.next_value
        else:
            raise ValueError

    def __empty(self):
        """Private func of available of head"""
        return self.head_value is None

    def delete(self, position):
        """Class that delete node by position"""
        if self.head_value is None:
            return
        if position == 0:
            self.head_value = self.head_value.next_value
            return self.head_value
        index = 0
        current = self.head_value
        prev = self.head_value
        temp = self.head_value
        while current is not None:

            if index == position:
                temp = current.next_value
                break
            prev = current
            current = current.next_value
            index += 1
        prev.next = temp
        return prev
