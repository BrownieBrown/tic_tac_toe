from app.board import Board
import pytest


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"
        self.winner = None
        self.is_game_over = False

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_win(self):
        rows = self.board.get_rows()
        columns = self.board.get_columns()
        diagonals = self.board.get_diagonals()
        all_lines = rows + columns + diagonals
        for line in all_lines:
            if line.count(line[0]) == 3 and line[0] != " ":
                self.winner = line[0]
                return True
        return False

    def check_draw(self):
        for row in self.board.get_rows():
            if " " in row:
                return False
        return True

    def play_turn(self, move):
        if self.board.make_move(move, self.current_player):
            if self.check_win():
                self.is_game_over = True
                return f"Player {self.current_player} wins!"
            if self.check_draw():
                self.is_game_over = True
                return "It's a draw!"
            self.switch_player()
            return f"{self.current_player}'s turn"

    def restart(self):
        self.board = Board()
        self.current_player = "X" if self.winner is None else "O" if self.winner == "X" else "X"
        self.winner = None
        self.is_game_over = False
        return "Game restarted!"

