"""Class for Tables initialising"""

import random
from restaurant import Restaurant


class Table(Restaurant):
    """Contains method for table object"""
    def __init__(self):
        super(Table, self).__init__()
        self.table_id = random.randint(1, 20)
        self.table_status = None

    def seat_table(self):
        """Func for returning table status free or not"""
        self.table_status = "Занят"
        print(f'Table:{self.table_id}\nСтатус:{self.table_status}')
        return self.table_status
