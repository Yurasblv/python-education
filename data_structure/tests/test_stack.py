"""Test for stack data structure"""
import pytest
from data_structure.stack import Stack


@pytest.fixture(name='stuck')
def instance():
    """Fixture for instance Stack object"""
    stack = Stack()
    stack.push('Alabama')
    stack.push('Nebraska')
    stack.push('Missuori')
    stack.push('Texas')
    return stack


def test_push(stuck):
    """Test push a value to stack"""
    assert stuck.size == 4
    assert stuck.top.data == 'Texas'


def test_popandpeek(stuck):
    """
    Test both methods for pop from stack
    and peek
    """

    stuck.pop()
    stuck.pop()
    assert stuck.size == 2
    assert stuck.peek() == 'Nebraska'


def test_empty(stuck):
    """Test for checking empty stack of not"""
    for i in range(4):
        stuck.pop()
    assert stuck.is_empty() == True
