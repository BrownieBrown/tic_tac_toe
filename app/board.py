class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, move, player):
        row, col = move
        if self.is_valid_move(move):
            self.board[row][col] = player
            return True
        return False

    def is_valid_move(self, move):
        row, col = move
        if not (isinstance(row, int) and isinstance(col, int)):
            return False
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        if self.board[row][col] != " ":
            return False
        return True

    def get_rows(self):
        return self.board

    def get_columns(self):
        return [list(col) for col in zip(*self.board)]

    def get_diagonals(self):
        return [[self.board[i][i] for i in range(3)], [self.board[i][2 - i] for i in range(3)]]
