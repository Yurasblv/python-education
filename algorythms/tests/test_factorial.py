"""Module tests factorial algorythm"""
import pytest
from algorythms.factorial import Factorial


@pytest.fixture()
def instance():
    """Create instance"""
    f = Factorial(5)
    return f.print_result

def test_instance(instance):
    """Tests instance"""
    assert str(instance) == '120'
    assert type(instance) == int
    assert instance == 120
