# Tic Tac Toe Game

Welcome to my Tic Tac Toe game, a timeless classic now available to play right in your command line. This Python-based
version allows you to enjoy quick games against a friend, with easy-to-follow commands and a clean, intuitive command
line interface.

## Features

- **Simple CLI Interface**: Play directly from your terminal.
- **Two Player Mode**: Challenge a friend to a match.
- **Score Tracking**: Keep tabs on wins and draws.
- **Immediate Feedback**: Get notified of wins, draws, or invalid moves instantly.
- **Restart Option**: Easily start a new game once the current game concludes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

### Prerequisites

Make sure you have Docker installed on your system to run the game in a containerized environment. This ensures
compatibility and ease of use across any platform.

- [Install Docker](https://docs.docker.com/get-docker/)
- [Python 3.8+](https://www.python.org/downloads/)

### Installation & Running The Game

#### Running the Game with Docker

If you have Docker installed, you can run the game in a containerized environment. This method ensures compatibility
across any platform.

1. **Build the Docker Image**

Next, build the Docker image using the provided `Dockerfile`:

   ```bash
   docker build -t tic-tac-toe .
   ```

2. **Run the Game with Docker**

Finally, run the game using the following command:

   ```bash
   docker run -it tic-tac-toe
   ```

You should now see the game's welcome message and be prompted to start a new game.

#### Running the Game Locally

If you prefer not to use Docker or do not have it installed, you can run the game directly using Python.

1. **Clone the Repository**

   Start by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/BrownieBrown/tic_tac_toe
   cd tic-tac-toe
   ```

2. **(Optional) Create a Virtual Environment**

   It's a good practice to create a virtual environment to manage your dependencies. If you don't have `virtualenv`
   installed, you can install it using pip:

   ```bash
   pip install virtualenv
   ```

   Then, create a virtual environment and activate it:

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Next, install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Game**

   Finally, run the game using the following command from the project's root directory:

   ```bash
   python3 main.py
   ```

   You should now see the game's welcome message and be prompted to start a new game.

## How to Play

After starting the game, you will interact with the Tic Tac Toe board via the command line.Here's what you need to know:

- **Board Layout**: The board is a 3x3 grid, with each cell numbered from 1 to 9. These numbers correspond to the
  positions you can play in.
- **Player Turns**: Players take turns to place their marks (X or O) on the board. The game starts with Player 1
- **Move Input**: When it's your turn, simply enter the number of the cell you want to play in the following format row:
  column. For example, to play in the top-right cell, you would enter 1:3.
- **Invalid Moves**: If you enter an invalid move (e.g., a cell that's already occupied or a non-existent cell), you
  will be prompted to try again.
- **Draws**: If all cells are filled without a winner, the game ends in a draw.
- **Score Tracking**: The game will keep track of the number of wins for each player, as well as the number of draws.
  You can view the current score at any time by entering the command "p".
- **Winning**: The game ends when a player gets three of their marks in a row, column, or diagonal. The winning player
  will be announced, and the game will end.

## Running the Tests

To ensure everything is working as expected, you can run the provided tests using pytest. Ensure you have pytest and
pytest-mock installed:

```bash
pip install pytest pytest-mock
```

Then, run the tests using the following command from the project's root directory

```bash
pytest
```

## Built With

- [Python](https://www.python.org/) - The programming language used
- [Docker](https://www.docker.com/) - Containerization and environment management

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


