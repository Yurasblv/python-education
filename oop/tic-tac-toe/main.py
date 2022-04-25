from controller import Controller
from view import Console
from models import Board

if __name__ == '__main__':
    Controller(Console, Board).show_menu()
