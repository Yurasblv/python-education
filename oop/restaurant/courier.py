"""Class for Courier initialising"""


import itertools
from delivery_service import DeliveryService


class Courier(DeliveryService):
    """Methods for courier"""
    id_iter = itertools.count()

    def __init__(self, phnum, name):
        super(Courier, self).__init__()
        self.courier_id = next(Courier.id_iter)
        self.courier_phnum = f'+{phnum}'
        self.courier_name = name

    def recieve_order(self):
        """Get an order"""
        if self.order:
            self.order.order_status = 'Recieved'
        else:
            return 'Courier dont have order'

    def _place_order(self):
        """Change status if order done"""
        if self.order.order_status == 'Done':
            return 'Order Done'
        else:
            return 'Order in work'

    def change_order(self, position, count):
        """Courier can remake order"""
        self.order = self.edit_order(position={position: count})
        return self.order
