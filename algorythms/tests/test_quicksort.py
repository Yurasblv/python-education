"""Module tests quicksort algorythm"""
import pytest
from algorythms.quick_sort import QuickSort


@pytest.fixture()
def instance():
    """Create instance"""
    a = [26, 17, 100, 1203, 500, 3443, 77, 98, 11]
    QuickSort(a, 0, len(a) - 1)
    return a


def test_instance(instance):
    """Test sorting"""
    a = [11, 17, 26, 77, 98, 100, 500, 1203, 3443]
    assert instance == a
    assert instance != [26, 17, 100, 1203, 500, 3443, 77, 98, 11]
