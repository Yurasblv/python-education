"""Main module with queue object (first coming , last passing)"""


class Node:
    """Node init"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return "Node {}".format(self.value)


class Queue:
    """Queue obj with operations"""

    def __init__(self):
        self.head = None
        self.tail = None

    def peak(self):
        """Give first value in queue"""
        return self.head.value

    def enqueue(self, value):
        """Add new element"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        """Cut element"""
        if self.head is None:
            raise Exception("Dequeue from empty queue.")

        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value


queue = Queue()
queue.enqueue('1')
queue.enqueue(11)
queue.enqueue([111])
queue.enqueue("+309324")
print(queue.dequeue())
print(queue.dequeue())
queue.dequeue()
