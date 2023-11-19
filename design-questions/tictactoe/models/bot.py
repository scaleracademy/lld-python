from dataclasses import dataclass

from models.level import Level
from models.player import Player
from models.board import Board
from models.cell import Cell

from strategies.bot_playing_strategy import BotPlayingStrategy


@dataclass
class BotPlayer(Player):
    difficulty_level: Level
    playing_strategy: BotPlayingStrategy

    def play(self, board: Board) -> Cell:
        return self.playing_strategy.get_move(board, self.symbol)
