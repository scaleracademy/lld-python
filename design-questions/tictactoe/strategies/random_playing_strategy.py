from random import choice
from models.board import Board
from models.cell import Cell
from models.symbol import Symbol
from strategies.bot_playing_strategy import BotPlayingStrategy


class RandomBotStrategy(BotPlayingStrategy):
    def get_move(self, board: Board, symbol: Symbol) -> Cell:
        available_cells = board.get_available_cells()
        move = choice(available_cells)
        move.symbol = symbol
        return move
