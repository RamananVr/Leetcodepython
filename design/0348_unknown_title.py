"""
LeetCode Problem #348: Design Tic-Tac-Toe

Problem Statement:
Design a Tic-Tac-Toe game that is played between two players on a n x n grid.

You may assume the following rules:
1. A move is guaranteed to be valid and is placed on an empty block.
2. Once a winning condition is reached, no more moves are allowed.
3. A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Implement the `TicTacToe` class:
- `TicTacToe(int n)` Initializes the object with the size of the board `n`.
- `int move(int row, int col, int player)` Indicates that the player with id `player` (1 or 2) makes a move at the cell `(row, col)` of the board. The move is guaranteed to be a valid move.

Returns:
- 0 if no one wins after the move.
- 1 if player 1 wins after the move.
- 2 if player 2 wins after the move.

Constraints:
- `1 <= n <= 100`
- `player` is either 1 or 2.
- `0 <= row, col < n`
- `(row, col)` are guaranteed to be a valid and empty cell.

Follow-up:
Could you do better than O(n^2) per move?
"""

class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize the TicTacToe board.
        """
        self.n = n
        self.rows = [0] * n  # Track row sums for each player
        self.cols = [0] * n  # Track column sums for each player
        self.diagonal = 0    # Track diagonal sum
        self.anti_diagonal = 0  # Track anti-diagonal sum

    def move(self, row: int, col: int, player: int) -> int:
        """
        Make a move and check if the player wins.
        """
        # Determine the score to add based on the player
        score = 1 if player == 1 else -1

        # Update row, column, diagonal, and anti-diagonal sums
        self.rows[row] += score
        self.cols[col] += score
        if row == col:
            self.diagonal += score
        if row + col == self.n - 1:
            self.anti_diagonal += score

        # Check if the player wins
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player

        # No one wins
        return 0


# Example Test Cases
if __name__ == "__main__":
    # Initialize a TicTacToe game with a 3x3 board
    game = TicTacToe(3)

    # Player 1 moves at (0, 0)
    print(game.move(0, 0, 1))  # Output: 0 (no one wins)

    # Player 2 moves at (0, 2)
    print(game.move(0, 2, 2))  # Output: 0 (no one wins)

    # Player 1 moves at (2, 2)
    print(game.move(2, 2, 1))  # Output: 0 (no one wins)

    # Player 2 moves at (1, 1)
    print(game.move(1, 1, 2))  # Output: 0 (no one wins)

    # Player 1 moves at (2, 0)
    print(game.move(2, 0, 1))  # Output: 0 (no one wins)

    # Player 2 moves at (1, 0)
    print(game.move(1, 0, 2))  # Output: 0 (no one wins)

    # Player 1 moves at (2, 1)
    print(game.move(2, 1, 1))  # Output: 1 (Player 1 wins)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The `move` method runs in O(1) time since it only updates a few variables and performs constant-time checks.

Space Complexity:
- The space complexity is O(n) due to the storage of `rows` and `cols` arrays, which each have size `n`. The `diagonal` and `anti_diagonal` variables use O(1) space.

Topic: Design
"""