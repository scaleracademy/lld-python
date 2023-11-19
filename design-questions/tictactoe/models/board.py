from dataclasses import dataclass, field
from typing import List

from models.cell import Cell


@dataclass
class Board:
    size: int
    cells: List[List[Cell]] = field(init=False)

    def __post_init__(self):
        self.cells = self.initialize_cells()

    def initialize_cells(self) -> List[List[Cell]]:
        cells = []
        for row in range(self.size):
            row_cells = [Cell(row=row, column=column) for column in range(self.size)]
            cells.append(row_cells)
        return cells

    def get_available_cells(self) -> List[Cell]:
        return [cell for row in self.cells for cell in row if cell.symbol is None]

    def update(self, cell: Cell):
        self.cells[cell.row][cell.column].symbol = cell.symbol

    def print(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol.value if cell.symbol else "_", end=" ")
            print()
