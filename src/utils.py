import os


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def parse_input(input_str):
    """Parse the user input from 'Row:Column' format into row and column indices."""
    try:
        row, col = map(int, input_str.split(":"))
        return row - 1, col - 1  # Adjust for 0-indexed board
    except ValueError:
        return None, None
