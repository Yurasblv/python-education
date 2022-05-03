"""Module with graph data structure"""
from data_structure.linked_list import LinkedList


class GraphNode:
    """Create node that consisth from lists of edges"""
    def __init__(self, data):
        self.data = data
        self.edges = LinkedList()


class Graph:
    """Main class contains list of nodes"""

    def __init__(self):
        self.nodes = LinkedList()

    def __iter__(self):
        for i in self.nodes:
            yield i

    def insert(self, data):
        """Insert a node to graph"""
        new_node = GraphNode(data)
        for node in self.nodes:
            node.node_value.edges.append(new_node)
        self.nodes.append(new_node)
        return self.nodes

    def add_node(self,key,path):
        """Add value to node in the nodes"""
        for i in self.nodes:
            if i.node_value.data == key:
                i.node_value.edges.append(path)
            elif i.node_value.data != key:
                pass

    def lookup(self, key):
        """Search a node by key data"""
        for i in self.nodes:
            if i.node_value.data == key:
                for i in i.node_value.edges:
                    return i.node_value
            else:
                print('Key not found')

    def delete(self, idx):
        """Remove node from Graph list"""
        for i in self.nodes:
            if i.node_value.data == idx:
                i.node_value.edges.delete(idx)
            elif i.node_value.data != idx:
                pass


g = Graph()
g.insert('a')
g.insert('b')
g.insert('c')
g.add_node('a','b')
g.delete('a')

# for i in g.nodes:
#     print(i)
#     print(i.node_value.data)





