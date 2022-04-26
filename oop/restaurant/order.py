"""Class for Order initialising"""

import datetime
import itertools


class Order:
    """Contains methods for order"""
    id_iter = itertools.count()

    def __init__(self, position):
        self._order_id = next(Order.id_iter)
        self.order_date = datetime.date
        self.order_status = None
        self.order_paid = None
        self.total_order = {}
        for position, count in position.items():
            self.add_to_order(position, count)

    def add_to_order(self, position, count):
        """Append to the order name and count of menu position"""
        self.total_order[position] = count
        self.order_status = 'Placed'
        self.order_date = datetime.date.today()
        return self._order_id, self.order_date, self.order_status, self.total_order

    def check_order(self):
        """Return final order"""
        print(f'\nУточняю заказ:\n')
        for k,v in self.total_order.items():
            print(f'{k} = {v} позиции')
        return self.total_order

    def search_order(self, position):
        """Search a position on order"""
        if self.total_order[position]:
            return f'{self.total_order[position]} существует!'
        return 'Такой заказ отсутствует'

    def edit_order(self, position, count):
        """Make some changes in ready order"""
        self.total_order[position] = count
        return self.total_order

    def delete_order(self, position):
        """Remove order"""
        del self.total_order[position]
        return self.total_order


