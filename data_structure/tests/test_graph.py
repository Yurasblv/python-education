from data_structure.graph import Graph
import pytest

@pytest.fixture()
def instance():
    graph = Graph()
    return graph


def test_insert(instance):
    """Tests inserting a instance to graph linkedlist"""
    instance.insert('A')
    assert instance.nodes[0].data == 'A'
    instance.insert('B')
    assert instance.nodes[1].data == 'B'
    instance.insert('C')
    assert instance.nodes[2].data == 'C'


def test_add_and_lookup(instance):
    """Tests add and search an instance by the key"""
    instance.insert('a')
    instance.add_node('a','b')
    assert instance.nodes[0].edges.head_value.node_value != 'a'
    assert instance.nodes[0].edges.head_value.node_value == 'b'
    assert instance.lookup('a') == 'b'

def test_delete(instance):
    """Tests delete  an instance by the key"""
    instance.insert('a')
    instance.add_node('a', 'b')
    instance.delete('a')
    assert instance.lookup('a') != 'a'

