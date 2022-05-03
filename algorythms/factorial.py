"""Module contains binary search algorythm"""


class Factorial:
    """Main class"""

    def __init__(self, value: int):
        self._result = self.factorial_fun(value)

    @property
    def print_result(self):
        """Print result"""
        return self._result

    def factorial_fun(self, value=None):
        """Main function"""
        # BASE CASE
        if value < 2:
            return value
        # RECURSIVE CASE
        else:
            return value * self.factorial_fun(value - 1)
