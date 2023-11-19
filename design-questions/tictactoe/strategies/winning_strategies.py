from strategies.winning_strategy import WinningStrategy

class RowWinningStrategy(WinningStrategy):
    def has_won(self, board, symbol) -> bool:
        for row in board.cells:
            if all(cell.symbol == symbol for cell in row):
                return True
        return False