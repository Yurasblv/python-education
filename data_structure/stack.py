"""Class imitate stack object """

class Node(object):
    """Node element init"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Stack(object):
    """Main class of stack"""

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        """Add node to stack"""
        new_node = Node(data)
        if self.top:
            new_node.next_node = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Cut last element"""
        if self.top is None:
            return None
        result = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return result

    def peek(self):
        """Returns first node from stack"""
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        """Check on amount"""
        if self.top is None:
            return True
        else:
            return False
