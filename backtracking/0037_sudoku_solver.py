"""
LeetCode Question #37: Sudoku Solver

Problem Statement:
Write a program to solve a Sudoku puzzle by filling the empty cells.
A Sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character represents empty cells.

Constraints:
- The given board contains only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
"""

def solveSudoku(board):
    """
    Solves the given Sudoku puzzle in-place.
    :param board: List[List[str]] - 9x9 grid representing the Sudoku puzzle
    """
    def is_valid(board, row, col, num):
        # Check if `num` can be placed at board[row][col]
        box_row, box_col = row // 3, col // 3
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * box_row + i // 3][3 * box_col + i % 3] == num:
                return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'  # Undo the move
                    return False  # No valid number found, backtrack
        return True  # Puzzle solved

    backtrack()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solveSudoku(board1)
    print("Solved Sudoku Board 1:")
    for row in board1:
        print(row)

    # Test Case 2
    board2 = [
        [".", ".", "9", "7", "4", "8", ".", ".", "."],
        ["7", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", "2", ".", "1", ".", "9", ".", ".", "."],
        [".", ".", "7", ".", ".", ".", "2", "4", "."],
        [".", "6", "4", ".", "1", ".", "5", "9", "."],
        [".", "9", "8", ".", ".", ".", "3", ".", "."],
        [".", ".", ".", "8", ".", "3", ".", "2", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "6"],
        [".", ".", ".", "2", "7", "5", "9", ".", "."]
    ]
    solveSudoku(board2)
    print("\nSolved Sudoku Board 2:")
    for row in board2:
        print(row)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The backtracking algorithm explores all possible configurations of the board.
- In the worst case, there are 9 choices for each of the 81 cells, leading to a time complexity of O(9^(81)).
- However, due to constraints and pruning (validity checks), the actual runtime is much smaller.

Space Complexity:
- The space complexity is O(1) since the board is modified in-place and no additional data structures are used.
- The recursion stack depth is at most 81, so the space complexity due to recursion is O(81) = O(1).

Topic: Backtracking
"""