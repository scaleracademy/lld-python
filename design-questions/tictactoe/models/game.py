import random
from dataclasses import dataclass, field
from typing import List, Optional

from models.board import Board
from models.player import Player
from models.game_status import GameStatus
from models.cell import Cell
from strategies.winning_strategy import WinningStrategy
from strategies.winning_strategies import RowWinningStrategy


@dataclass
class Game:
    next_player_index: int
    board: Board
    players: List[Player] = field(default_factory=list)
    winner: Player = None
    winning_strategies: List[WinningStrategy] = field(
        default_factory=lambda: [RowWinningStrategy()]
    )
    status: GameStatus = field(init=False)


    def start(self):
        self.current_player_index = random.randint(0, len(self.players) - 1)
        self.status = GameStatus.IN_PROGRESS

    def get_current_player(self) -> Player:
        return self.players[self.current_player_index]

    def play(self):
        current_player = self.get_current_player()
        move: Cell = current_player.play(self.board)
        self.validate_move(move)

        self.board.update(move)

        if self.has_won():
            self.status = GameStatus.FINISHED
            return

        if self.is_draw():
            self.status = GameStatus.DRAW
            return

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def validate_move(self, move: Cell) -> bool:
        if move.row < 0 or move.row >= self.board.size:
            return False

        if move.column < 0 or move.column >= self.board.size:
            return False

        return True

    def has_won(self) -> bool:
        for strategy in self.winning_strategies:
            if strategy.has_won(self.board, self.get_current_player().symbol):
                self.winner = self.get_current_player()
                return True
        return False

    def is_draw(self) -> bool:
        return len(self.board.get_available_cells()) == 0

    def get_winner(self) -> Optional[Player]:
        return self.winner
