"""Class for input data from user"""
from abc import abstractmethod, ABC


class View(ABC):
    """Abstract class of view"""

    @staticmethod
    @abstractmethod
    def menu_panel():
        """Print panel for menu"""
        pass

    @staticmethod
    @abstractmethod
    def game_helper():
        """Print description for game"""
        pass

    @staticmethod
    @abstractmethod
    def end_session():
        """Print end session description"""
        pass

    @staticmethod
    @abstractmethod
    def input_menu():
        """Have values for changing mode"""
        pass

    @staticmethod
    @abstractmethod
    def input_chess_num():
        """Take chess number"""
        pass

    @staticmethod
    @abstractmethod
    def input_approve():
        """Return str value"""
        pass

    @staticmethod
    @abstractmethod
    def input_player_name():
        """Return player name"""
        pass

    @staticmethod
    @abstractmethod
    def player_turn(player):
        pass

    @staticmethod
    @abstractmethod
    def player_winner(player):
        pass

    @staticmethod
    @abstractmethod
    def create_game_board(model):
        """Draw a field for the game"""
        pass

    @staticmethod
    @abstractmethod
    def create_player():
        pass

class Console(View):

    @staticmethod
    def menu_panel():
        """Print panel for menu"""
        print("Option \n1.Play\n2.History\n3.Exit")
        print("Enter number: ")

    @staticmethod
    def game_helper():
        """Print description for game"""
        print('*** Welcome to tic-tac-toe game ***')
        print(
            '\n- Rules: Write numeric value in range from 1 to 9 to square cage.'
            ' \n- First who make combination from 3 values '
            'will be winner. Good luck =)  \n')

    @staticmethod
    def end_session():
        """Print end session description"""
        print('-----------------------\n'
              'Try again?\n'
              'Enter Yes to continue\n'
              'Enter No to exit\n'
              'Enter Score to look statistic\n'
              '------------------------\n')

    @staticmethod
    def input_menu():
        while True:
            try:
                value = int(input())
                if value not in range(1, 4):
                    raise ValueError
                if value == 3:
                    print('Good bye ;]')
            except ValueError:
                print('Select 1,2 or 3 ')
                continue
            return value

    @staticmethod
    def input_chess_num():
        while True:
            try:
                value = int(input())
                if value not in range(1, 10):
                    raise ValueError
            except ValueError:
                print(' Only number from 1 to 9 ')
                continue
            return value

    @staticmethod
    def input_approve():
        """Return str value"""
        menu_val = str(input().capitalize())
        if menu_val not in ['Score', 'Yes']:
            print('Good Luck')
        return menu_val

    @staticmethod
    def input_player_name():
        """Return player name"""
        player1 = str(input('Enter name for 1 player'))
        player2 = str(input('Enter name for 2 player'))
        while True:
            try:
                if not player1:
                    raise NotImplementedError
                if not player2:
                    raise NotImplementedError
                if player1 == player2:
                    print('This name is already busy!')
            except NotImplementedError:
                print('Name is empty!')
            return player1,player2

    @staticmethod
    def player_turn(player):
        """Return turn name player"""
        print(f'--- {player} enter number(1-9): ')

    @staticmethod
    def player_winner(player):
        """Return turn name player"""
        print(f'{player} won!')

    @staticmethod
    def create_game_board(model):
        """Draw a field for the game"""
        print('*' * 13 + '\n')
        for i in range(3):
            print("|", model[0 + i * 3], "|",
                  model[1 + i * 3], "|", model[2 + i * 3], '|')
            print('' * 13)
        print('*' * 13)
