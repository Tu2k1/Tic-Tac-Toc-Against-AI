# Tic Tac Toe Game

Welcome to the Tic Tac Toe Game! This project is a simple implementation of the classic Tic Tac Toe game using Python and the Pygame library. The game allows you to play against an AI that uses the minimax algorithm for optimal gameplay.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [AI (Minimax Algorithm)](#ai-minimax-algorithm)
- [Contributing](#contributing)

## Features

- Classic Tic Tac Toe gameplay
- Play against an intelligent AI opponent
- Smooth graphics and interactive interface using Pygame

## Installation

1. **Clone the repository**:
    ```
    git clone https://github.com/yourusername/tictactoe.git
    cd tictactoe
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```
    pip install -r requirements.txt
    ```

## Usage

To start the game, simply run the `runner.py` file:
```
python runner.py
```

## Game Rules

- The game is played on a 3x3 grid.
- You have the choice to play as 'X' or 'O'. The AI will play as the other symbol.
- Players take turns placing their marks (X or O) in empty squares.
- The first player to get 3 of their marks in a row (vertically, horizontally, or diagonally) wins the game.
- If all 9 squares are filled and neither player has 3 in a row, the game is a draw.

## AI (Minimax Algorithm)

The AI opponent uses the minimax algorithm to determine the best possible move. In the minimax algorithm, we consider 'X' as the maximizing player and 'O' as the minimizing player. This algorithm is a decision-making algorithm used for minimizing the possible loss in a worst-case scenario.

### How Minimax Works:

1. **Generate all possible moves**: The algorithm evaluates all possible moves from the current state.
2. **Evaluate game states**: Each possible move leads to a new game state, which is evaluated recursively.
3. **Choose the optimal move**: The AI chooses the move that maximizes its minimum gain (hence "minimax").

By considering 'X' as the maximum and 'O' as the minimum, the AI can make strategic decisions to maximize its chances of winning or minimize its chances of losing.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or improvements, feel free to create an issue or submit a pull request.
