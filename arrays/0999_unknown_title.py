"""
LeetCode Problem #999: Available Captures for Rook

Problem Statement:
On an 8x8 chessboard, there is exactly one white rook ('R') and some number of white bishops ('B') and black pawns ('p'). 
These are represented by characters on a grid. Empty squares are represented by the character '.'.

The rook moves horizontally and vertically through empty squares until it is blocked by either another piece or the edge of the board. 
It can capture a black pawn by moving onto the same square as the pawn.

Return the number of pawns the rook can capture in one move.

Example:
Input: 
board = [
  [".",".",".",".",".",".",".","."],
  [".",".",".","p",".",".",".","."],
  [".",".",".","R",".",".",".","p"],
  [".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".","."],
  [".",".",".","p",".",".",".","."],
  [".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".","."]
]
Output: 3

Constraints:
- board.length == board[i].length == 8
- board[i][j] is either 'R', '.', 'B', or 'p'
- There is exactly one 'R' on the board.
"""

# Python Solution
def numRookCaptures(board):
    def find_rook():
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    return i, j
        return -1, -1  # Should never happen due to constraints

    def count_pawns_in_direction(x, y, dx, dy):
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == 'B':  # Blocked by a bishop
                return 0
            if board[x][y] == 'p':  # Found a pawn
                return 1
            x += dx
            y += dy
        return 0

    # Find the rook's position
    rook_x, rook_y = find_rook()

    # Count pawns in all four directions
    captures = 0
    captures += count_pawns_in_direction(rook_x, rook_y, -1, 0)  # Up
    captures += count_pawns_in_direction(rook_x, rook_y, 1, 0)   # Down
    captures += count_pawns_in_direction(rook_x, rook_y, 0, -1)  # Left
    captures += count_pawns_in_direction(rook_x, rook_y, 0, 1)   # Right

    return captures

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    print(numRookCaptures(board1))  # Output: 3

    # Test Case 2
    board2 = [
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","."],
        [".",".",".",".","B",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    print(numRookCaptures(board2))  # Output: 2

    # Test Case 3
    board3 = [
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","R",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]
    print(numRookCaptures(board3))  # Output: 0

# Time and Space Complexity Analysis
# Time Complexity: O(8 * 8) = O(64) = O(1)
#   - Finding the rook takes O(64) in the worst case (fixed size board).
#   - Counting pawns in each direction takes O(8) per direction (fixed size board).
#   - Overall, the operations are constant due to the fixed board size.

# Space Complexity: O(1)
#   - No additional data structures are used; only a few variables are allocated.

# Topic: Arrays