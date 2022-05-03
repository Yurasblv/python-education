"""Class for binary tree object initialization"""


class BSTNode:
    """Class init node for tree"""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        if self.left:
            return f'value={self.value} <left={self.left}>'
        if self.right:
            return f'value={self.value} <right={self.right}>'
        return f'{self.value}'


class BST:
    """Tree init"""

    def __init__(self, node: BSTNode):
        self.node = node

    def __repr__(self):
        return "Node: {}".format(self.node)

    def insert(self, data):
        """Insert a data to node"""
        if data == self.node.value:
            return
        if self.node.value > data:
            if self.node.left:
                self.node.left.insert(data)
            else:
                self.node.left = BST(BSTNode(data))
        else:
            if self.node.right:
                self.node.right.insert(data)
            else:
                self.node.right = BST(BSTNode(data))

    def lookup(self, data):
        """Search a data in tree"""
        if self.node.value == data:
            return True
        if data < self.node.value:
            if self.node.left:
                return self.node.left.lookup(data)
            else:
                return False
        if data > self.node.value:
            if self.node.right:
                return self.node.right.lookup(data)
            else:
                return False

    def delete(self, key):
        """Delete a node by key"""
        if key < self.node.value:
            if self.node.left is None:
                raise ValueError("Value not found in tree")
            self.node.left = self.node.left.delete(key)
            return self
        elif key > self.node.value:
            if self.node.right is None:
                raise ValueError("Value not found in tree")
            self.node.right = self.node.right.delete(key)
            return self
        else:
            if self.node.left is None and self.node.right is None:
                return None
            if self.node.left is None:
                return self.node.right
            if self.node.right is None:
                return self.node.left
            parent, node = self.node, self.node.left
            while node.right is not None:
                parent, node = node, node.right
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            self.node.value = node.value
            return self
