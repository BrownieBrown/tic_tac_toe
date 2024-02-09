from src.board import Board
from src.enums import BoardSymbol, PlayerSymbol


def test_init():
    board = Board()
    assert all(cell == BoardSymbol.EMPTY.value for row in board.board for cell in row), "Initial Board should be empty"


def test_print_board(capsys):
    board = Board()
    board.print_board()
    captured = capsys.readouterr()
    assert captured.out == " | | \n-----\n | | \n-----\n | | \n-----\n", "Initial Board should be empty"


def test_make_move():
    board = Board()
    assert board.make_move((0, 0), PlayerSymbol.PLAYER_1.value), "Should return True for valid move"
    assert not board.make_move((0, 0), PlayerSymbol.PLAYER_2.value), "Should return False for invalid move"
    assert not board.make_move((3, 3), PlayerSymbol.PLAYER_1.value), "Should return False for invalid move"
    assert not board.make_move((0, 0), " "), "Should return False for invalid move"
    assert not board.make_move(("wrong input", 0), PlayerSymbol.PLAYER_2.value), "Should return False for invalid move"


def test_is_valid_move():
    board = Board()
    assert board.is_valid_move((0, 0)), "Should return True for valid move"
    assert not board.is_valid_move((3, 3)), "Should return False for invalid move"
    assert not board.is_valid_move(("wrong input", 0)), "Should return False for invalid move"


def test_get_rows():
    board = Board()
    board.make_move((0, 0), PlayerSymbol.PLAYER_1.value)
    board.make_move((1, 1), PlayerSymbol.PLAYER_1.value)
    board.make_move((2, 2), PlayerSymbol.PLAYER_2.value)
    expected_rows = [[BoardSymbol.PLAYER_1.value, BoardSymbol.EMPTY.value, BoardSymbol.EMPTY.value],
                     [BoardSymbol.EMPTY.value, BoardSymbol.PLAYER_1.value, BoardSymbol.EMPTY.value],
                     [BoardSymbol.EMPTY.value, BoardSymbol.EMPTY.value, BoardSymbol.PLAYER_2.value]]
    assert board.get_rows() == expected_rows, "Rows should match expected rows"


def test_get_columns():
    board = Board()
    board.make_move((0, 0), PlayerSymbol.PLAYER_1.value)
    board.make_move((1, 0), PlayerSymbol.PLAYER_1.value)
    board.make_move((2, 2), PlayerSymbol.PLAYER_2.value)
    expected_columns = [[BoardSymbol.PLAYER_1.value, BoardSymbol.PLAYER_1.value, BoardSymbol.EMPTY.value],
                        [BoardSymbol.EMPTY.value, BoardSymbol.EMPTY.value, BoardSymbol.EMPTY.value],
                        [BoardSymbol.EMPTY.value, BoardSymbol.EMPTY.value, BoardSymbol.PLAYER_2.value]]
    assert board.get_columns() == expected_columns, "Columns should match expected columns"


def test_get_diagonals():
    board = Board()
    board.make_move((0, 0), PlayerSymbol.PLAYER_1.value)
    board.make_move((1, 1), PlayerSymbol.PLAYER_1.value)
    board.make_move((2, 2), PlayerSymbol.PLAYER_1.value)
    expected_diagonals = [[BoardSymbol.PLAYER_1.value, BoardSymbol.PLAYER_1.value, BoardSymbol.PLAYER_1.value],
                          [BoardSymbol.EMPTY.value, BoardSymbol.PLAYER_1.value, BoardSymbol.EMPTY.value]]
    assert board.get_diagonals() == expected_diagonals, "Diagonals should match expected diagonals"
