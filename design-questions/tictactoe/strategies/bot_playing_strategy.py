from abc import ABC, abstractmethod
from models.board import Board
from models.cell import Cell
from models.symbol import Symbol

class BotPlayingStrategy(ABC):
    @abstractmethod
    def get_move(self, board: Board, symbol: Symbol) -> Cell:
        pass