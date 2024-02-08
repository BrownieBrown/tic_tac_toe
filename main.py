from app.game import Game
from app.utils import clear_screen, display_stats, parse_input


def main():
    game = Game()
    clear_screen()
    print("Welcome to Tic Tac Toe!")

    while True:
        clear_screen()
        game.board.print_board()

        valid_move = False
        while not valid_move:
            move = input(
                f"{game.current_player.name}: Please enter the position of your mark (Row:Column):\n").strip().lower()

            if move == "p":
                display_stats(game.players)
                continue
            if move == "e":
                print("Exiting game. Thanks for playing!")
                return

            row, col = parse_input(move)
            if row is None or col is None or not game.play_turn((row, col)):
                print(f"Input {row}:{col}")
                print("The inserted field is not valid. Try again:")
            else:
                valid_move = True

        if game.is_game_over:
            clear_screen()
            game.board.print_board()
            print("Game Over!")
            if game.winner:
                print(f"Game Over. {game.current_player.symbol} wins!")
            else:
                print("It's a draw!")

            input("Press Enter to start a new round...")
            game.restart()


if __name__ == "__main__":
    main()
