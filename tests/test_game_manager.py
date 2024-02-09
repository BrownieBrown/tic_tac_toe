from src.enums import GameState
from src.game_manager import GameManager


def test_display_stats(mocker, capfd):
    mocker.patch('builtins.input', return_value='')  # Mock input to simulate pressing Enter
    game_manager = GameManager()
    game_manager.game.players[0].wins = 1  # Set up some wins for player 1

    game_manager.display_stats()
    out, err = capfd.readouterr()

    assert "X wins: 1" in out


def test_handle_input_stats(mocker):
    mocker.patch('builtins.input', return_value='p')  # Mock input to simulate pressing 'p'
    game_manager = GameManager()

    assert game_manager.handle_input() == GameState.CONTINUE


def test_handle_input_exit(mocker):
    mocker.patch('builtins.input', return_value='e')  # Mock input to simulate pressing 'e'
    game_manager = GameManager()

    assert game_manager.handle_input() == GameState.EXIT


def test_process_move_valid(mocker):
    mocker.patch('src.utils.parse_input', return_value=(0, 0))  # Mock a valid move
    game_manager = GameManager()

    game_manager.game.board = mocker.MagicMock()  # Mock the board to prevent actual game logic
    game_manager.game.play_turn = mocker.MagicMock(return_value=True)  # Mock play_turn to always succeed

    assert game_manager.process_move("1:1") == GameState.VALID


def test_process_move_invalid(mocker):
    mocker.patch('src.utils.parse_input', return_value=(None, None))  # Mock an invalid move
    game_manager = GameManager()

    game_manager.display_error = mocker.MagicMock()  # Mock display_error to prevent actual game logic

    assert game_manager.process_move("invalid") == GameState.INVALID


def test_process_move_occupied(mocker):
    mocker.patch('src.utils.parse_input', return_value=(0, 0))  # Mock a valid move
    game_manager = GameManager()

    game_manager.display_error = mocker.MagicMock()  # Mock display_error to prevent actual game logic
    game_manager.game.board = mocker.MagicMock()  # Mock the board to prevent actual game logic
    game_manager.game.play_turn = mocker.MagicMock(return_value=False)
    # Mock play_turn to always fail
    assert game_manager.process_move("1:1") == GameState.OCCUPIED


def test_process_move_out_of_bounds(mocker):
    mocker.patch('src.utils.parse_input', return_value=(3, 3))  # Mock a move out of bounds
    game_manager = GameManager()

    game_manager.display_error = mocker.MagicMock()  # Mock display_error to prevent actual game logic

    assert game_manager.process_move("4:4") == GameState.INVALID


def test_display_game_over_winner(mocker, capfd):
    mocker.patch('src.game_manager.clear_screen')
    game_manager = GameManager()

    game_manager.game.winner = game_manager.game.players[0]  # Simulate player 1 winning
    game_manager.display_game_over()
    captured = capfd.readouterr()

    assert f"Game Over. {game_manager.game.current_player.symbol} wins!" in captured.out


def test_display_game_over_draw(mocker, capfd):
    mocker.patch('src.game_manager.clear_screen')
    game_manager = GameManager()
    game_manager.game.winner = None  # Simulate a draw

    game_manager.display_game_over()
    captured = capfd.readouterr()

    assert "It's a draw!" in captured.out
