"""Module testing math properities"""
import unittest
from tests import to_test


class SumAL(unittest.TestCase):
    """ Class with methods to make operations with numbers """

    def test_sum_all_true(self):
        """Tests the true sum"""
        return self.assertEqual(to_test.sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9), 45)

    def test_sum_all_false(self):
        """Test the false sum"""
        return self.assertFalse(to_test.sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9) == 190)

    def test_input_type(self):
        """Tests input value type"""
        return self.assertRaises(TypeError, to_test.sum_all, 'fdsl', {1: []})


if __name__ == '__main__':
    unittest.main()
