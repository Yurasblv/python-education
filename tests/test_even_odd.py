"""Module testing even and odd values coming in"""
import unittest
import pytest
from tests.to_test import even_odd


class MyTest(unittest.TestCase):
    """Main class"""

    def test_odd(self):
        """Tests odd values"""
        self.assertEqual(even_odd(15), 'odd')

    def test_even(self):
        """Tests even values"""
        self.assertEqual(even_odd(2), 'even')


@pytest.mark.parametrize('num', [2, 4, 6])
def test_eve(num):
    """Tests combine values"""
    assert even_odd(num) == 'even'
    assert even_odd(num) != 'odd'


if __name__ == '__main__':
    unittest.main()
