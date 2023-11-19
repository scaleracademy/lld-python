from dataclasses import dataclass
from models.symbol import Symbol


@dataclass
class Cell:
    row: int
    column: int
    symbol: Symbol = None
