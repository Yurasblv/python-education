"""Class define hash table data structure"""
from data_structure.linked_list import LinkedList


class Node:
    """Init node"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"{{ {self.key} : {self.value} }}"


class HashTable:
    """Init table"""

    def __init__(self):
        self.capacity = 30
        self.size = 0
        self.buckets = [LinkedList() for i in range(self.capacity)]

    def hash(self, key):
        """Count hash sum"""
        ctrl_sum = 0
        for i, c in enumerate(key):
            ctrl_sum += (i + len(key)) ** ord(c)
            ctrl_sum = ctrl_sum % self.capacity
        return ctrl_sum

    def insert(self, key, value):
        """Add new k,v to hash table"""
        index = self.hash(key)
        node = Node(key, value)
        if self.size <= self.capacity:
            if self.buckets[index].head_value is None:
                self.size += 1
                self.buckets[index] = node
            if self.buckets[index] == index:
                self.buckets.append(node)
        else:
            print('No memory')

    def lookup(self, key):
        """Search a node"""
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node[index].next
        if node is None:
            return None
        else:
            return node.value

    def delete(self, key):
        """Remove value by key"""
        index = self.hash(key)
        node = self.buckets[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
