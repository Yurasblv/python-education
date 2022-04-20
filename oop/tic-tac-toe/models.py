"""Module define board and player objects that with special methods"""


class Board:
    """Main class of board"""

    def __init__(self):
        self.board = list(range(1, 10))


    def __getitem__(self, item):
        return self.board[item]


    @staticmethod
    def win_combination(combination):
        """Return players win combo """
        combinations = {2, 5, 8}, {1, 2, 3}, {1, 4, 7}, {1, 5, 9}, \
                       {3, 5, 7}, {3, 6, 9}, {4, 5, 6}, {7, 8, 9}
        for combo in combinations:
            if len(combo - combination) == 0:
                return combo



class Player:
    """Main class of player"""

    def __init__(self,name=None,symbol=None):
        self.symbol = symbol
        self.name = name
        self.history = set()
        self.counter = int()

    def __str__(self):
        return f'{self.name} has {self.counter} wins'


    def save_position(self, position) -> set:
        """Return history of turns"""
        self.history.add(position)
        return self.history

    def delete_history(self):
        self.history.clear()
        return self.history

    def wins(self, count):
        self.counter += count
        return self.counter
