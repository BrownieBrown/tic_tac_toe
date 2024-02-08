import os


def display_stats(players):
    # Clear the screen (works on Windows and Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Stats:")
    print(f"{players[0].symbol} wins: {players[0].wins}")
    print(f"{players[1].symbol} losses: {players[1].wins}")
    print("Press enter to resume the game...")

    input()  # Wait for the user to press Enter

    # Optionally clear the screen again here if you want to return to a clean state
    os.system('cls' if os.name == 'nt' else 'clear')


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
