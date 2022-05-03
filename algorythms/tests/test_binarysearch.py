"""Module tests binary search algorythm"""
import pytest
from algorythms.binary_search import BinarySearch


@pytest.fixture()
def instance():
    """Create instance"""
    f = BinarySearch([22,3,57,5,20,15,50,39,67,1,88])
    return f

def test_instance(instance):
    """Tests algorythm"""
    assert instance.search_method(22) == 5
    assert type(instance.search_method(22)) == int
    assert instance.search_method(3) == BinarySearch([22,3,57,5,20,15,50,39,67,1,88]).search_method(3)