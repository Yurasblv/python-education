"""Main file for shown test classes
Contains all classes with showing work of each
To run use command :
            python main.py
"""

from restaurant import Restaurant
from table import Table
from waiter import Waiter
from client import Client
from menu import Menu
from order import Order
from bill import Bill
from card import Card
from delivery_service import DeliveryService
from cash import Cash

if __name__ == '__main__':
    restaurant = Restaurant().open()
    table = Table().seat_table()
    menu = Menu.show_menu()
    client = Client('Mark', 'Hamilton area №38').make_order({'Grilled fish of the day': 1,
                                                             'Vegetable chili': 1,
                                                             'Beer': 1})
    order = Order(client).check_order()
    waiter = Waiter()
    waiter._recieve_order(order)
    print('\n')
    waiter.waiter()
    process = waiter._complete_order(order)
    print('\n')
    if process is True:
        bill = Bill(order).create_bill('Card')
        card = Card('ПриватБанк', bill).paid_status
    print('-' * 70)
    delivery = DeliveryService(75835957, 'Nauki 82',
                               {
                                   'Cheese and tomato pizza': 3,
                                   'Orange juice': 5
                               }).check_order()
    bill = Bill(delivery[2]).create_bill('Card')
    pay = Cash(bill[2]).recieve()
