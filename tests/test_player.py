from app.player import Player


def test_player_init():
    player_x = Player(symbol="X", name="Player X")
    player_o = Player(symbol="O")

    assert player_x.symbol == "X"
    assert player_x.name == "Player X"
    assert player_x.wins == 0
    assert player_x.losses == 0
    assert player_x.draws == 0

    assert player_o.symbol == "O"
    assert player_o.name == "O"  # Name defaults to symbol if not provided
    assert player_o.wins == 0
    assert player_o.losses == 0
    assert player_o.draws == 0


def test_record_win():
    player_x = Player(symbol="X", name="Player X")
    player_x.record_win()
    assert player_x.wins == 1
    assert player_x.losses == 0
    assert player_x.draws == 0


def test_record_loss():
    player_x = Player(symbol="X", name="Player X")
    player_x.record_loss()
    assert player_x.wins == 0
    assert player_x.losses == 1
    assert player_x.draws == 0


def test_record_draw():
    player_x = Player(symbol="X", name="Player X")
    player_x.record_draw()
    assert player_x.wins == 0
    assert player_x.losses == 0
    assert player_x.draws == 1


def test_record_multiple():
    player_x = Player(symbol="X", name="Player X")
    player_x.record_win()
    player_x.record_win()
    player_x.record_loss()
    player_x.record_draw()
    assert player_x.wins == 2
    assert player_x.losses == 1
    assert player_x.draws == 1
