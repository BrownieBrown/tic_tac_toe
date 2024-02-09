from src.board import Board
from src.enums import PlayerSymbol, BoardSymbol
from src.player import Player


class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player(PlayerSymbol.PLAYER_1.value), Player(PlayerSymbol.PLAYER_2.value)]
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
            if line.count(line[0]) == 3 and line[0] != BoardSymbol.EMPTY.value:
                self.winner = self.current_player
                return True

        return False

    def check_draw(self):
        for row in self.board.get_rows():
            if BoardSymbol.EMPTY.value in row:
                return False

        return True

    def handle_win(self):
        self.is_game_over = True
        self.current_player.record_win()
        self.players[1 - self.current_player_index].record_loss()

    def handle_draw(self):
        self.is_game_over = True
        for player in self.players:
            player.record_draw()

    def play_turn(self, move):
        if self.board.make_move(move, self.current_player.symbol):
            if self.check_win():
                self.handle_win()
                return f"Player {self.current_player.name} wins!"
            if self.check_draw():
                self.handle_draw()
                return "It's a draw!"

            self.switch_player()

            return f"{self.current_player.name}'s turn"

    def restart(self):
        self.board = Board()
        if self.is_game_over:
            if self.winner:
                self.current_player_index = 1 if self.winner == self.players[0] else 0
            else:
                # If it's a draw, the starting player should be X according to the rules
                self.current_player_index = 0
        else:
            self.current_player_index = 0

        self.winner = None
        self.is_game_over = False
        self.starting_player_index = self.current_player_index

        return "Game restarted!"
