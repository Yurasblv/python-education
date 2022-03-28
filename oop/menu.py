"""Class for Menu initialising"""


class Menu:
    """Contains menu and methods for working"""
    def __init__(self):
        self.menu = {
        'Grilled fish of the day': 8.00,
        'Steak with chips or salad': 12.00,
        'Sausage and roast tomato pasta': 7.00,
        'Chicken salad with garlic yoghurt dressing': 7.00,
        'Cheese and tomato pizza': 7.00,
        'Mushroom omelette': 6.00,
        'Vegetable chili': 7.00,
        'Soup of the day with brown or white bread': 4.00,
        'Homemade carrot cake': 3.50,
        'Homemade banana cake': 3.50,
        'Chocolate ice cream with chocolate sauce': 3.50,
        "Fresh fruit salad with grapes, mango, melon and apple, served with cream or ice cream": 3.50,
        'Cup of coffee': 2.00,
        'Cup of tea': 1.50,
        'Glass of wine, white or red': 3.00,
        'Beer': 3.00,
        'Water': 1.00,
        'Orange juice': 2.00,
    }

    def add_food(self, position):
        """Add new item in menu"""
        for p, c in position.items():
            self.menu[p] = c
            return self.menu

    def delete_food(self, position):
        """Delete position from current menu"""
        del self.menu[str(position).capitalize()]
        return self.menu

    @staticmethod
    def show_menu():
        """Shows menu"""
        return Menu().menu


