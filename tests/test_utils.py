from src.utils import parse_input


def test_parse_input():
    assert parse_input("1:1") == (0, 0), "Should return (0, 0) for input '1:1'"
    assert parse_input("3:3") == (2, 2), "Should return (2, 2) for input '3:3'"
    assert parse_input("invalid") == (None, None), "Should return (None, None) for non-numeric input"
    assert parse_input("1,2") == (None, None), "Should return (None, None) for incorrect delimiter"
    assert parse_input("wrong input") == (None, None), "Should return (None, None) for input 'wrong input'"
    assert parse_input("4:4") == (3, 3), ("Should convert '4:4' to (3, 3) even though it's out of bounds for a 3x3 Tic "
                                          "Tac Toe board")
