"""Class for Client initialising"""


import datetime
import itertools
from order import Order


class Client:
    """Client methods"""

    id_iter = itertools.count()

    def __init__(self, name=None, address=None, phone=None):
        self._client_id = int
        self.name = name
        self.address = address
        self.phone = phone
        self.client_order = None

    def make_order(self, position):
        """Make an order"""
        self._client_id = next(Client.id_iter)
        self.client_order = Order(position=position)
        return self.client_order.total_order

    def _last_visited(self):
        """Return time of last visit"""
        self.last_visited = datetime.datetime.now()
        return self.last_visited

    def _last_ordered(self):
        """Return time of last order"""
        self.last_ordered = datetime.datetime.now()
        return self.last_ordered
