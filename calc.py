"""That's module define Calculator class with four methods"""


class Calculator:
    """ This class was created for math operations with two digit variables """

    def __init__(self, first_val, second_val):
        self.first_val = first_val
        self.second_val = second_val

    def addition(self):
        """ This method is for addition variables """
        return self.first_val + self.second_val

    def subtraction(self):
        """This method is for subtraction variables"""
        return self.first_val - self.second_val

    def multiplication(self):
        """This method is for multiplication variables"""
        return self.first_val * self.second_val

    def division(self):
        """This method is for division variables"""
        try:
            return self.first_val / self.second_val
        except ZeroDivisionError:
            return 'На ноль делить нельзя!'
