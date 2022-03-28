"""Class for Waiter initialising"""
import itertools
import random
from table import Table


class Waiter(Table):
    """Contains functions for waiter"""
    id_iter = itertools.count()

    STAFF = ['Liam', 'Olivia', 'Noah', 'Emma', 'Oliver',
             'Ava', 'Elijah', 'Charlotte', 'William', 'Megan']


    def __init__(self):
        super(Waiter, self).__init__()
        self._waiter_id = next(Waiter.id_iter)
        self.waiter_name = random.choice(self.STAFF)
        self.recieved_order = False
        self.complete_order = False

    def _recieve_order(self, order):
        """Function where waiter get order"""
        if order:
            self.recieved_order = True
            print('Заказ получен')
            return self.recieved_order

    def _complete_order(self,order):
        """Function to show status of Waiters order"""
        if order:
            self.complete_order = True
            return self.complete_order

    def waiter(self):
        """All info about waiter"""
        print(f'Официант № {self._waiter_id}\nИмя {self.waiter_name}')
        return self._waiter_id, self.waiter_name


