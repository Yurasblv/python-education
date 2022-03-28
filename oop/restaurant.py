""" Start class for Restaurant initialising"""


class Restaurant:
    """Contains methods for restaurant"""
    NAME = 'ProjectProvenance№7'

    def __init__(self, name=NAME):
        self.name = name
        self.work_status = 'Closed'

    def open(self):
        """Opens restaurant"""
        self.work_status = 'Opened'
        print(f'{Restaurant.NAME} : {self.work_status}')

    def close(self):
        """Close restaurant"""
        self.work_status = 'Closed'
        print(f'{Restaurant.NAME} : {self.work_status}')
