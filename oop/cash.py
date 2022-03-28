"""Class for Cash initialising"""


from bill import Bill

class Cash(Bill):
    """Methods for cash payment method"""

    def __init__(self,amount):
        super(Bill, self).__init__()
        self._amount = amount

    def recieve(self):
        """Change status when bill recieves"""
        self.paid_status = True
        print('Оплачено')
        return self.paid_status

