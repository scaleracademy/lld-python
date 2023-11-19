import unittest
from models.board import Board
from models.game import Game
from models.human_player import HumanPlayer
from models.bot import BotPlayer
from models.symbol import Symbol
from models.level import Level
from models.user import User
from models.game_status import GameStatus
from strategies.random_playing_strategy import RandomBotStrategy

class TestTicTacToe(unittest.TestCase):
    def test_create_board(self):
        board = Board(3)

        self.assertEqual(
            board.size, 3, "If the board size is 3, then the board should have 3 rows"
        )

        first_row = board.cells[0]
        self.assertEqual(
            len(first_row),
            3,
            "If the board size is 3, then the board should have 3 columns",
        )

    def test_create_game(self):
        board = Board(3)

        human = HumanPlayer(Symbol.X, User("Tantia Tope", "t@t.com", "image.png"))
        bot = BotPlayer(Symbol.O, Level.EASY, RandomBotStrategy())

        game = Game(0, board=board, players=[human, bot])

        self.assertEqual(
            game.next_player_index,
            0,
            "The first player should be the first player in the list of players",
        )
        self.assertEqual(len(game.board.cells), 3, "The board size should be 3")


if __name__ == "__main__":
    unittest.main()
