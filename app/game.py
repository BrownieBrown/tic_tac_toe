from app.board import Board
from app.player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player_index = 0
        self.starting_player_index = 0
        self.winner = None
        self.is_game_over = False

    @property
    def current_player(self):
        return self.players[self.current_player_index]

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def check_win(self):
        rows = self.board.get_rows()
        columns = self.board.get_columns()
        diagonals = self.board.get_diagonals()
        all_lines = rows + columns + diagonals
        for line in all_lines:
            if line.count(line[0]) == 3 and line[0] != " ":
                self.winner = self.current_player
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
                self.current_player.record_win()
                self.players[1 - self.current_player_index].record_loss()
                return f"Player {self.current_player.name} wins!"
            if self.check_draw():
                self.is_game_over = True
                for player in self.players:
                    player.record_draw()
                return "It's a draw!"
            self.switch_player()

            return f"{self.current_player.name}'s turn"

    def restart(self):
        self.board = Board()
        if self.is_game_over:
            if self.winner:
                self.current_player_index = 1 if self.winner == self.players[0] else 0
            else:
                self.current_player_index = 1 - self.starting_player_index
        else:
            self.current_player_index = 0

        return "Game restarted!"
