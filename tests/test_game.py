from src.enums import PlayerSymbol, BoardSymbol
from src.game import Game


def test_initial_state():
    game = Game()
    assert game.players[0].symbol == PlayerSymbol.PLAYER_1.value, "First player should be X"
    assert game.players[1].symbol == PlayerSymbol.PLAYER_2.value, "Second player should be O"
    assert game.current_player_index == 0, "Initial current player should be X"
    assert game.winner is None, "There should be no winner initially"
    assert not game.is_game_over, "Game should not be over initially"
    empty_board = [[BoardSymbol.EMPTY.value for _ in range(3)] for _ in range(3)]
    assert game.board.board == empty_board, "Board should be initially empty"


def test_current_player():
    game = Game()
    assert game.current_player == game.players[0], "Current player should be the first player"
    game.switch_player()
    assert game.current_player == game.players[1], "Current player should be the second player"
    game.switch_player()
    assert game.current_player == game.players[0], "Current player should be the first player"
    game.switch_player()
    assert game.current_player == game.players[1], "Current player should be the second player"


def test_switch_player():
    game = Game()
    game.switch_player()
    assert game.current_player_index == 1, "Should switch to O"
    game.switch_player()
    assert game.current_player_index == 0, "Should switch back to X"


def test_check_win():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2)]
    for move in moves:
        game.board.make_move(move, PlayerSymbol.PLAYER_1.value)
    assert game.check_win(), "Should return True for winning move"
    assert game.winner.symbol == PlayerSymbol.PLAYER_1.value, "Winner should be X"


def test_check_draw():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 1)]
    for move in moves:
        game.board.make_move(move, PlayerSymbol.PLAYER_1.value)
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
    assert game.current_player.symbol == PlayerSymbol.PLAYER_2.value, "Should not switch player on invalid move"


def test_play_turn_out_of_bounds():
    game = Game()
    response = game.play_turn((-1, 0))  # Invalid move
    assert response is None, "Should not allow play out of bounds"
    assert game.current_player.symbol == PlayerSymbol.PLAYER_1.value, "Should not switch player on invalid move"


def test_sequence_of_plays():
    game = Game()
    moves_and_players = [((0, 0), PlayerSymbol.PLAYER_1.value), ((0, 1), PlayerSymbol.PLAYER_2.value),
                         ((1, 1), PlayerSymbol.PLAYER_1.value), ((1, 0), PlayerSymbol.PLAYER_2.value)]

    for move, player in moves_and_players:
        game.play_turn(move)
        assert game.current_player.symbol != player, "Player should switch after a valid move"
    assert not game.check_win(), "Should not have a winner yet"
    assert not game.check_draw(), "Should not be a draw yet"


def test_restart():
    game = Game()
    game.play_turn((0, 0))
    game.restart()
    assert game.current_player.symbol == PlayerSymbol.PLAYER_1.value, "Current player should be X"
    assert game.winner is None, "Winner should be None"
    assert not game.is_game_over, "Game should not be over"
    empty_board = [[BoardSymbol.EMPTY.value for _ in range(3)] for _ in range(3)]
    assert game.board.board == empty_board, "Board should be empty"


def test_restart_after_win():
    game = Game()
    # Simulate a winning condition for 'X'
    game.play_turn((0, 0))  # 'X'
    game.play_turn((1, 0))  # 'O'
    game.play_turn((0, 1))  # 'X'
    game.play_turn((1, 1))  # 'O'
    game.play_turn((0, 2))  # 'X' wins
    game.restart()
    # Expect 'O' to start since 'X' won the last game
    assert game.current_player.symbol == PlayerSymbol.PLAYER_2.value, "O should start after X's win"


def test_restart_after_draw():
    game = Game()
    moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 1)]
    for move in moves:
        game.play_turn(move)
    assert game.check_draw()
    game.restart()
    assert game.current_player.symbol == PlayerSymbol.PLAYER_2.value, "O should start after a draw if X started the last game"
