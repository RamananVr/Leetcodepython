"""
LeetCode Problem #1275: Find Winner on a Tic Tac Toe Game

Problem Statement:
Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
1. Players take turns placing characters into empty squares (" ").
2. The first player A always places "X" characters, while the second player B always places "O" characters.
3. "X" and "O" are placed alternately until either:
   - One player wins, or
   - All squares are filled.
4. A player wins if there are three of their characters in a row, column, or diagonal.

Given an array `moves` where each element is a pair `[row, col]` indicating the row and column of the grid where the player places their character in order, return the winner of the game if it exists (`"A"` or `"B"`). If the game ends in a draw, return `"Draw"`. If there are still moves to be played, return `"Pending"`.

You can assume that `moves` is valid (i.e., it follows the rules of Tic-Tac-Toe), and the grid is initially empty.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins by filling the diagonal.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins by filling the second column.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves left.

Example 4:
Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.

Constraints:
- 1 <= moves.length <= 9
- moves[i].length == 2
- 0 <= moves[i][j] <= 2
- There are no repeated elements on `moves`.
- moves follow the rules of tic-tac-toe.

"""

def tictactoe(moves):
    """
    Determine the winner of a Tic-Tac-Toe game or the game's status.

    :param moves: List[List[int]] - A list of moves where each move is a pair [row, col].
    :return: str - "A", "B", "Draw", or "Pending".
    """
    # Initialize the board
    board = [[""] * 3 for _ in range(3)]
    
    # Fill the board based on moves
    for i, (row, col) in enumerate(moves):
        board[row][col] = "A" if i % 2 == 0 else "B"
    
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    
    # Check if the game is still pending
    if len(moves) < 9:
        return "Pending"
    
    # Otherwise, it's a draw
    return "Draw"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: A wins
    moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    print(tictactoe(moves1))  # Output: "A"

    # Test Case 2: B wins
    moves2 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    print(tictactoe(moves2))  # Output: "B"

    # Test Case 3: Draw
    moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    print(tictactoe(moves3))  # Output: "Draw"

    # Test Case 4: Pending
    moves4 = [[0,0],[1,1]]
    print(tictactoe(moves4))  # Output: "Pending"

# Time Complexity Analysis:
# - Filling the board: O(n), where n is the number of moves (at most 9).
# - Checking rows, columns, and diagonals: O(1) since the board size is fixed (3x3).
# Overall: O(1) since the board size is constant.

# Space Complexity Analysis:
# - The board requires O(1) space since its size is fixed (3x3).
# Overall: O(1).

# Topic: Arrays, Simulation