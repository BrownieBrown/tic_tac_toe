from app.board import Board


def test_init():
    board = Board()
    assert all(cell == " " for row in board.board for cell in row), "Initial Board should be empty"


def test_print_board(capsys):
    board = Board()
    board.print_board()
    captured = capsys.readouterr()
    assert captured.out == " | | \n-----\n | | \n-----\n | | \n-----\n", "Initial Board should be empty"


def test_make_move():
    board = Board()
    assert board.make_move((0, 0), "X"), "Should return True for valid move"
    assert not board.make_move((0, 0), "O"), "Should return False for invalid move"
    assert not board.make_move((3, 3), "X"), "Should return False for invalid move"
    assert not board.make_move((0, 0), " "), "Should return False for invalid move"
    assert not board.make_move(("wrong input", 0), "O"), "Should return False for invalid move"


def test_is_valid_move():
    board = Board()
    assert board.is_valid_move((0, 0)), "Should return True for valid move"
    assert not board.is_valid_move((3, 3)), "Should return False for invalid move"
    assert not board.is_valid_move(("wrong input", 0)), "Should return False for invalid move"


def test_get_rows():
    board = Board()
    board.make_move((0, 0), 'X')
    board.make_move((1, 1), 'X')
    board.make_move((2, 2), 'O')
    expected_rows = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'O']]
    assert board.get_rows() == expected_rows, "Rows should match expected rows"


def test_get_columns():
    board = Board()
    board.make_move((0, 0), 'X')
    board.make_move((1, 0), 'X')
    board.make_move((2, 2), 'O')
    expected_columns = [['X', 'X', ' '], [' ', ' ', ' '], [' ', ' ', 'O']]
    assert board.get_columns() == expected_columns, "Columns should match expected columns"


def test_get_diagonals():
    board = Board()
    board.make_move((0, 0), 'X')
    board.make_move((1, 1), 'X')
    board.make_move((2, 2), 'X')
    expected_diagonals = [['X', 'X', 'X'], [' ', 'X', ' ']]
    assert board.get_diagonals() == expected_diagonals, "Diagonals should match expected diagonals"
