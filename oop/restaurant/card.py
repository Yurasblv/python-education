"""Class for Card initialising"""


class Card:
    """Methods for card payment method"""

    def __init__(self, bank, currency):
        self._amount = currency
        self.bank = bank
        self.recieve()

    def recieve(self):
        """Change status when cash recieves"""
        self.paid_status = True
        print(f'Оплачено')
        return self.paid_status
