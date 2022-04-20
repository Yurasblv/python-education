"""Main file to play tic-tac-toe"""
from models import Board, Player
from log_conf import logger
from view import Console


class Controller:

    def __init__(self, view: Console, board: Board):
        self.view = view
        self.board = board
        self.player_1 = None
        self.player_2 = None

    def create_player(self):
        """Create players"""
        player_1,player_2 = self.view.input_player_name()
        self.player_1 = Player(player_1, 'X')
        self.player_2 = Player(player_2, 'O')
        return self.player_1, self.player_2

    def show_score(self):
        """Show log score"""
        score = open("Tic-Tac-Toe Log", "r", encoding='utf-8').read()
        try:
            if len(score) == 0:
                raise Exception
        except Exception:
            raise FileNotFoundError

    def show_menu(self):
        """ Title of game """
        self.view.menu_panel()
        while True:
            p_choice = self.view.input_menu()
            if p_choice == 1:
                self.main()
            elif p_choice == 2:
                self.show_score()
                self.show_menu()
            elif p_choice == 3:
                break

    def player_turn(self):
        """Loop players turn"""
        while True:
            self.view.create_game_board(self.board.board)
            self.view.player_turn(self.player_1.name)
            player_1_position = self.view.input_chess_num()
            self.player_1.save_position(player_1_position)
            self.board.board[player_1_position - 1] = self.player_1.symbol
            if self.board.win_combination(self.player_1.history):
                self.player_1.wins(1)
                self.view.player_winner(self.player_1.name)
                logger.info(f'{self.player_1.name} won')
                logger.info(f'{self.player_1.name} - {self.player_1.counter} : '
                            f'{self.player_2.name} - {self.player_2.counter}')
                break

            self.view.create_game_board(self.board.board)
            self.view.player_turn(self.player_2.name)
            player_2_position = self.view.input_chess_num()
            self.player_1.save_position(player_2_position)
            self.board.board[player_2_position - 1] = self.player_2.symbol
            if self.board.win_combination(self.player_1.history):
                self.player_1.wins(1)
                self.view.player_winner(self.player_2.name)
                logger.info(f'{self.player_2.name} won')
                logger.info(f'{self.player_2.name} - {self.player_2.counter} : '
                            f'{self.player_1.name} - {self.player_1.counter}')
                break

    def main(self):
        """Launch function"""
        self.view.game_helper()
        if self.player_1 is None and self.player_2 is None:
            self.player_1, self.player_2 = self.create_player()
        self.board = Board()
        self.player_turn()
        self.view.end_session()
        restart = self.view.input_approve()
        if restart == 'Yes':
            self.player_1.delete_history()
            self.player_1.delete_history()
            Controller.main(self.player_1, self.player_2)
        if restart == 'Score':
            self.show_score()
        else:
            return
