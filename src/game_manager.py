from src.enums import Command, GameState
from src.game import Game
from src.utils import clear_screen, parse_input


def introduce_game():
    print("Welcome to Tic Tac Toe!")
    print("To make a move, enter the row and column number (e.g. 1:1).")
    print("You can also type 'p' to display the current score or 'e' to exit the game.")
    input("Press Enter to start the game...")


class GameManager:
    def __init__(self):
        self.game = Game()

    def start_game(self):
        clear_screen()
        introduce_game()
        self.run_game_loop()

    def display_stats(self):
        clear_screen()

        print("Stats:")
        print(f"{self.game.players[0].symbol} wins: {self.game.players[0].wins}")
        print(f"{self.game.players[1].symbol} wins: {self.game.players[1].wins}")
        input("Press enter to resume the game...")

    def handle_input(self):
        move_input = input(
            f"{self.game.current_player.symbol}: Please enter the position of your mark (Row:Column), 'p' for stats, "
            f"'e' to exit:\n").strip().lower()

        if move_input == Command.STATS.value:
            self.display_stats()
            return GameState.CONTINUE
        elif move_input == Command.EXIT.value:
            clear_screen()
            print("Exiting game. Thanks for playing!")
            return GameState.EXIT
        else:
            return self.process_move(move_input)

    def process_move(self, move_input):
        row, col = parse_input(move_input)
        if row is None or col is None:
            self.display_error("The inserted field is not valid. Try again.")
            return GameState.INVALID

        if not (0 <= row < 3 and 0 <= col < 3):
            self.display_error("The inserted field is out of bounds. Try again.")
            return GameState.INVALID

        if not self.game.play_turn((row, col)):
            self.display_error("That space is already occupied. Try again.")
            return GameState.OCCUPIED

        return GameState.VALID

    def run_game_loop(self):
        while True:
            clear_screen()
            self.game.board.print_board()

            outcome = self.handle_input()
            if outcome == GameState.EXIT:
                break
            elif outcome in [GameState.CONTINUE, GameState.INVALID, GameState.OCCUPIED]:
                continue

            if self.game.is_game_over:
                self.display_game_over()
                input("Press Enter to start a new round...")
                self.game.restart()

    def display_game_over(self):
        clear_screen()
        self.game.board.print_board()
        if self.game.winner:
            print(f"Game Over. {self.game.current_player.symbol} wins!")
        else:
            print("It's a draw!")

    def display_error(self, message):
        clear_screen()
        self.game.board.print_board()
        print(message)
        input("Press Enter to continue...")
