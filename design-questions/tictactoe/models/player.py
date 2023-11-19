from abc import ABC, abstractmethod
from dataclasses import dataclass
from models.symbol import Symbol
from models.board import Board
from models.cell import Cell


@dataclass
class Player(ABC):
    symbol: Symbol

    @abstractmethod
    def play(self, board: Board) -> Cell:
        pass
