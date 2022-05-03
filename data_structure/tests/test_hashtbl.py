"""Module for testing hash table data structure"""
import pytest
from data_structure.hash_table import HashTable


@pytest.fixture()
def instance():
    """Creating instance fixture"""
    ht = HashTable()
    return ht


@pytest.mark.parametrize('marks', ['Toyota', 'Subaru', 'Honda'])
def test_insertnlooup(instance, marks):
    """Tests both method of insert and loop through table"""
    instance.insert('mark', marks)
    assert instance.lookup('mark') == marks
    instance.insert('author', 'Will Smith')
    assert instance.lookup('author') == 'Will Smith'


def test_hash(instance):
    """Tests hashing algorythm"""
    value = 'Something interesting'
    assert type(instance.hash(value)) == int
    assert instance.hash(value) < 30 or instance.hash(value) >= 0


def test_delete(instance):
    """Tests removing an item from table"""
    instance.insert('mark1', 'Honda')
    instance.insert('mark2', 'Brabus')
    assert instance.lookup('mark1') == 'Honda'
    assert instance.lookup('mark2') == 'Brabus'
    instance.delete('mark1')
    assert instance.lookup('mark1') is not True
    instance.delete('mark2')
    assert instance.lookup('mark2') is None
