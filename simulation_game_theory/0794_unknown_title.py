"""
LeetCode Problem #794: Valid Tic-Tac-Toe State

Problem Statement:
-------------------
A Tic-Tac-Toe board is represented as a 3x3 array of characters, where each character is either 'X', 'O', or ' '. 
The game follows these rules:
1. Players take turns placing characters into empty squares (' ').
2. The first player always places 'X' characters, while the second player always places 'O' characters.
3. 'X' and 'O' characters are placed into empty squares, never on filled ones.
4. The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
5. The game also ends if all squares are non-empty.

Given a Tic-Tac-Toe board `board`, return `True` if and only if it is possible to reach this board position during the course of a valid Tic-Tac-Toe game.

The board is a list of strings `board` where each string represents a row of the board. 
The character `board[i][j]` is either 'X', 'O', or ' '.

Constraints:
- `board.length == 3`
- `board[i].length == 3`
- `board[i][j]` is either 'X', 'O', or ' '.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: False
Explanation: The first player always places "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: False
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XOX", "O O", "XOX"]
Output: True
"""

def validTicTacToe(board):
    """
    Determines if the given Tic-Tac-Toe board is a valid state.
    
    :param board: List[str] - A 3x3 Tic-Tac-Toe board
    :return: bool - True if the board is valid, False otherwise
    """
    def is_winner(player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(board[i][j] == player for j in range(3)):  # Check row
                return True
            if all(board[j][i] == player for j in range(3)):  # Check column
                return True
        if all(board[i][i] == player for i in range(3)):  # Check main diagonal
            return True
        if all(board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
            return True
        return False

    # Count the number of X's and O's
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)

    # Rule 1: X goes first, so there must be at least as many X's as O's
    if o_count > x_count:
        return False

    # Rule 2: The difference between X's and O's must not exceed 1
    if x_count > o_count + 1:
        return False

    # Rule 3: If X is a winner, there must be exactly one more X than O
    if is_winner('X') and x_count != o_count + 1:
        return False

    # Rule 4: If O is a winner, there must be exactly the same number of X's and O's
    if is_winner('O') and x_count != o_count:
        return False

    # If all rules are satisfied, the board is valid
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = ["O  ", "   ", "   "]
    print(validTicTacToe(board1))  # Output: False

    # Test Case 2
    board2 = ["XOX", " X ", "   "]
    print(validTicTacToe(board2))  # Output: False

    # Test Case 3
    board3 = ["XOX", "O O", "XOX"]
    print(validTicTacToe(board3))  # Output: True

    # Test Case 4
    board4 = ["XXX", "   ", "OOO"]
    print(validTicTacToe(board4))  # Output: False

    # Test Case 5
    board5 = ["XOX", "OXO", "XOX"]
    print(validTicTacToe(board5))  # Output: True

"""
Time and Space Complexity Analysis:
------------------------------------
Time Complexity:
- Counting X's and O's: O(3 * 3) = O(1) since the board size is fixed at 3x3.
- Checking for a winner: O(3 + 3 + 2) = O(1) since there are 3 rows, 3 columns, and 2 diagonals to check.
- Overall: O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Simulation, Game Theory
"""