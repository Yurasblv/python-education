"""Test for queue data structure"""
import pytest
from data_structure.queue import Queue


@pytest.fixture()
def queue():
    """Fixture for instance Queue object"""
    return Queue()


@pytest.mark.parametrize('param', ['1', 11, [111], [None]])
def test_enqueue(queue, param):
    """Test add to queue a value"""
    queue.enqueue(param)
    assert queue.head.value == param


def test_peak(queue):
    """Test add to start of queue a value"""
    queue.enqueue(11)
    assert queue.peak() == 11


def test_dequeue(queue):
    """Test remove a value from queue"""
    queue.enqueue('1')
    queue.enqueue(11)
    queue.enqueue([111])
    queue.enqueue("+309324")
    assert queue.head.next.value == 11
    assert queue.dequeue()
    assert queue.head.value == 11
    assert queue.tail.value == "+309324"
