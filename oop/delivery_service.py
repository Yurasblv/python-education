"""Class for Delivery Service initialising"""


from restaurant import Restaurant
from order import Order
from menu import Menu


class DeliveryService(Restaurant, Order):
    """Methods for delivery functionality"""

    def __init__(self, phone, address, order):
        super(DeliveryService, self).__init__()
        self.phone = f'+{phone}'
        self.address = address
        self.worktime = '12:00 - 22:00'
        self.total_order = {}
        for position, count in order.items():
            self.take_order(position, count)

    def take_order(self, position, count):
        """Get an order"""
        self.total_order[position] = count
        return self.total_order

    def check_order(self):
        """Checks the order"""
        print(f'Заказ от {self.phone}\n'
              f'{self.address}')
        print(f'\nУточняю заказ:\n')
        for k, v in self.total_order.items():
            print(f'{k} = {v} позиции')
        return self.phone, self.address, self.total_order

    def delete_delivery(self):
        """Remove order"""
        del self.total_order
        return self.total_order

    @staticmethod
    def show_menu():
        """Just show menu in delivery"""
        return Menu.show_menu()
