from app.game import Game


def test_initial_state():
    game = Game()
    assert game.current_player == "X", "Initial current player should be X"
    assert game.winner is None, "There should be no winner initially"
    assert not game.is_game_over, "Game should not be over initially"
    empty_board = [[" " for _ in range(3)] for _ in range(3)]
    assert game.board.board == empty_board, "Board should be initially empty"


def test_switch_player():
    game = Game()
    game.switch_player()
    assert game.current_player == "O", "Should switch to O"
    game.switch_player()
    assert game.current_player == "X", "Should switch to X"
    game.switch_player()
    assert game.current_player == "O", "Should switch to O"
    game.switch_player()
    assert game.current_player == "X", "Should switch to X"


def test_check_win():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2)]
    for move in moves:
        game.board.make_move(move, "X")
    assert game.check_win(), "Should return True for winning move"
    assert game.winner == "X", "Winner should be X"


def test_check_draw():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 1)]
    for move in moves:
        game.board.make_move(move, "X")
    assert game.check_draw(), "Should return True for draw"


def test_play_turn_win():
    game = Game()
    assert game.play_turn((0, 0)) == "O's turn", "Should return O's turn"
    assert game.play_turn((0, 1)) == "X's turn", "Should return X's turn"
    assert game.play_turn((1, 1)) == "O's turn", "Should return O's turn"
    assert game.play_turn((0, 2)) == "X's turn", "Should return X's turn"
    assert game.play_turn((2, 2)) == "Player X wins!", "Should return X wins!"
    assert game.is_game_over, "Game should be over"


def test_play_turn_draw():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 1)]
    for move in moves:
        game.play_turn(move)
    assert game.check_draw()
    assert game.is_game_over, "Game should be over"


def test_play_turn_on_occupied_space():
    game = Game()
    game.play_turn((0, 0))
    response = game.play_turn((0, 0))  # Attempt to play on the same spot
    assert response is None, "Should not allow play on an occupied space"
    assert game.current_player == "O", "Should not switch player on invalid move"


def test_play_turn_out_of_bounds():
    game = Game()
    response = game.play_turn((-1, 0))  # Invalid move
    assert response is None, "Should not allow play out of bounds"
    assert game.current_player == "X", "Should not switch player on invalid move"


def test_sequence_of_plays():
    game = Game()
    moves_and_players = [((0, 0), "X"), ((0, 1), "O"), ((1, 1), "X"), ((1, 0), "O")]
    for move, player in moves_and_players:
        game.play_turn(move)
        assert game.current_player != player, "Player should switch after a valid move"
    assert not game.check_win(), "Should not have a winner yet"
    assert not game.check_draw(), "Should not be a draw yet"


def test_restart():
    game = Game()
    game.play_turn((0, 0))
    game.restart()
    assert game.current_player == "X", "Current player should be X"
    assert game.winner is None, "Winner should be None"
    assert not game.is_game_over, "Game should not be over"
    empty_board = [[" " for _ in range(3)] for _ in range(3)]
    assert game.board.board == empty_board, "Board should be empty"


def test_restart_after_win():
    game = Game()
    # Simulate a winning condition for X
    game.play_turn((0, 0))
    game.play_turn((1, 0))
    game.play_turn((0, 1))
    game.play_turn((1, 1))
    game.play_turn((0, 2))
    assert game.winner == "X", "X should be the winner"
    game.restart()
    assert game.current_player == "O", "Initial current player should be O after X's win"
    assert game.winner is None, "There should be no winner initially"
    assert not game.is_game_over, "Game should not be over initially"
    empty_board = [[" " for _ in range(3)] for _ in range(3)]
    assert game.board.board == empty_board, "Board should be initially empty"
