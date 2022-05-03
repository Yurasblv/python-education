import pytest
from data_structure.binary_srch_tree import BST, BSTNode


@pytest.fixture
def instance():
    """Creates instance for fixture"""
    n = BSTNode(1)
    c = BST(n)
    return c


def test_insert(instance):
    """Tests adding instance to the tree"""
    assert instance.node.value == 1
    instance.insert(4)
    assert str(instance.node.right) == 'Node: 4'
    instance.insert(3)
    assert instance.node.right != 'Node 3'
    with pytest.raises(TypeError):
        instance.insert('vagabund')


@pytest.mark.parametrize('values', [4, 10, 8, 12, 15])
def test_lookup(instance, values):
    """Tests search method """
    instance.insert(values)
    assert instance.lookup(values) is True
    instance.insert(3.20)
    assert instance.lookup(3.20) is True


def test_delete(instance):
    """Tests remove node method """
    instance.insert(4)
    instance.insert(3)
    instance.insert(3.20)
    instance.insert(20)
    assert str(instance.delete(20)) == 'Node: value=1 <right=Node: value=4 <left=Node: value=3 <right=Node: 3.2>>>'
    assert instance.lookup(20) is False
    assert instance.delete(4)
    assert instance.lookup(4) is False



