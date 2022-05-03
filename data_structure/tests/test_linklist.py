"""
Basic data structure that will be used
in construct of else structures
"""

import pytest
from data_structure.linked_list import LinkedList


@pytest.fixture(name='ll')
def ll():
    """Create fixture"""
    ll = LinkedList()
    return ll


@pytest.mark.parametrize('values', ['AAA', 'BBB', 'CCC'])
def test_append(ll, values):
    """Testing add to end of list a value"""
    ll.append(values)
    assert ll.head_value.node_value == values


@pytest.mark.parametrize('values', ['AAA', 'BBB', 'CCC'])
def test_prepend(ll, values):
    """Testing add at beginning of list a value"""
    ll.append('HELLO WORLD')
    ll.append('GOOD BYE WORLD')
    ll.prepend(values)
    assert ll.head_value.node_value == values


def test_insert(ll):
    """Add value to index of list"""
    ll.append('Safari')
    assert ll.head_value.node_value == 'Safari'
    ll.insert('Edge', 1)
    assert ll.head_value.next_value.node_value == 'Edge'


def test_lookup(ll):
    """Test a method of searching a value"""
    ll.append('Safari')
    ll.append('Chrome')
    ll.append('Edge')
    ll.append(['1'])
    assert ll.lookup('Safari') is True
    assert ll.lookup('Chrome') is True
    assert ll.lookup(['1']) is True


def test_delete(ll):
    """Test a method of removing a value"""
    ll.insert('Safari', 0)
    ll.insert('Chrome', 1)
    ll.insert('Edge', 2)
    ll.delete(0)
    assert ll.head_value.node_value != 'Chrome'
    ll.delete(1)
    ll.delete(2)
    assert ll.head_value.next_value.node_value == 'Edge'
    ll.prepend('Digital')
    assert ll.head_value.node_value == 'Digital'
