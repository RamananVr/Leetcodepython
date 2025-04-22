"""
LeetCode Problem #419: Battleships in a Board

Problem Statement:
Given an `m x n` board where each cell is a battleship ('X') or empty ('.'), return the number of battleships on the board. 
Battleships can only be placed horizontally or vertically on the board. In other words, they can only occupy a contiguous 
segment of cells horizontally or vertically. Furthermore, there must be at least one horizontal or vertical cell separating 
each battleship (i.e., no adjacent battleships).

Constraints:
- The board is a 2D array of characters with dimensions `m x n` where `1 <= m, n <= 200`.
- The board contains only the characters 'X' and '.'.
- Battleships on the board are represented by contiguous 'X' characters horizontally or vertically.
- There are no adjacent battleships.

Example:
Input: board = [
  ["X", ".", ".", "X"],
  [".", ".", ".", "X"],
  [".", ".", ".", "X"]
]
Output: 2

Explanation:
There are two battleships in the board.
- One is located horizontally at the top-right corner.
- The other is located vertically in the rightmost column.

Follow-up:
Could you do it in one-pass, using O(1) extra memory, and without modifying the board?
"""

# Solution
def countBattleships(board):
    """
    Counts the number of battleships on the board.

    :param board: List[List[str]] - 2D board containing 'X' and '.' characters
    :return: int - Number of battleships
    """
    if not board or not board[0]:
        return 0

    m, n = len(board), len(board[0])
    count = 0

    for i in range(m):
        for j in range(n):
            # Only count the top-left cell of each battleship
            if board[i][j] == 'X':
                if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        ["X", ".", ".", "X"],
        [".", ".", ".", "X"],
        [".", ".", ".", "X"]
    ]
    print(countBattleships(board1))  # Output: 2

    # Test Case 2
    board2 = [
        ["X", "X", ".", "."],
        [".", ".", ".", "."],
        ["X", ".", ".", "."],
        ["X", ".", ".", "."]
    ]
    print(countBattleships(board2))  # Output: 3

    # Test Case 3
    board3 = [
        ["X"]
    ]
    print(countBattleships(board3))  # Output: 1

    # Test Case 4
    board4 = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."]
    ]
    print(countBattleships(board4))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through every cell in the board exactly once. 
If the board has dimensions `m x n`, the time complexity is O(m * n).

Space Complexity:
The algorithm uses O(1) extra space since no additional data structures are used, and the board is not modified.
"""

# Topic: Arrays