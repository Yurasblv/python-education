"""Class for Bill initialising"""


import datetime
import itertools
from menu import Menu


class Bill:
    """Methods for clients bill"""
    id_iter = itertools.count()

    def __init__(self, order):
        self.order_date = None
        self._currency = str
        self.method = str
        self.paid_status = False
        self.order = dict(order)

    def create_bill(self, method, ):
        """Create a bill"""
        self.method = method
        self.order_date = datetime.datetime.now().time()
        price_list = []
        for k in self.order.keys():
            if k in Menu.show_menu():
                price_list.append(Menu.show_menu()[k])
        self._currency = sum(price_list)
        print(f'Оплата {self.method}\nВремя {self.order_date}\nСтоимость {self._currency}')
        return self.method, self.order_date, self._currency

    def update_bill(self, currency, method):
        """Change bill """
        self.order_date = datetime.datetime.now()
        self._currency = currency
        self.method = method
        return self.method, self.order_date, self._currency

    def paid(self):
        """Return paid status"""
        self.paid_status = True
        return self.paid_status
