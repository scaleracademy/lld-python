from models.game import Game
from models.game_status import GameStatus
from models.level import Level
from models.symbol import Symbol
from models.user import User
from models.human_player import HumanPlayer
from models.bot import BotPlayer
from models.board import Board

from typing import Tuple
from strategies.random_playing_strategy import RandomBotStrategy

GAME_SIZE = 3
DIFFICULTY_LEVEL = Level.EASY


def get_user_input() -> Tuple[str, str, Symbol]:
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    user_symbol = input("Enter your symbol: ")
    parsed_symbol: Symbol = Symbol[user_symbol]

    return user_name, user_email, parsed_symbol


def create_game() -> Game:
    name, email, symbol = get_user_input()
    user = User(name, email)
    human = HumanPlayer(symbol, user)

    bot = BotPlayer(decide_bot_symbol(symbol), DIFFICULTY_LEVEL, RandomBotStrategy())

    board = Board(GAME_SIZE)
    return Game(0, board=board, players=[human, bot])


def decide_bot_symbol(user_symbol: Symbol) -> Symbol:
    return Symbol.X if user_symbol == Symbol.O else Symbol.O


def main():
    print("Welcome to Tic Tac Toe!")
    
    game = create_game()
    game.start()

    while game.status == GameStatus.IN_PROGRESS:
        current_player = game.get_current_player()
        print(f"Next turn: {current_player.symbol.name}")

        game.play()
        
        game.board.print()
        
        if (game.status == GameStatus.FINISHED):
            print(f"{game.get_winner().symbol} has won!")
            break
        
        if (game.status == GameStatus.DRAW):
            print("The game is a draw!")
            break


if __name__ == "__main__":
    main()
