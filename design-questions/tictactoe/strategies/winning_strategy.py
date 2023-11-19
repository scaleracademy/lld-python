from abc import ABC, abstractmethod

from models.board import Board
from models.symbol import Symbol

class WinningStrategy(ABC):
    @abstractmethod
    def has_won(self, board: Board, symbol: Symbol) -> bool:
        pass