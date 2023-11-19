from dataclasses import dataclass
from models.player import Player
from models.user import User
from models.board import Board
from models.cell import Cell


@dataclass
class HumanPlayer(Player):
    user: User

    def play(self, board: Board) -> Cell:
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        return Cell(row, col, self.symbol)
