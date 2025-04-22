"""
LeetCode Problem #37: Sudoku Solver

Problem Statement:
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

Constraints:
- The given board contains only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.
"""

def solveSudoku(board):
    """
    Solves the Sudoku puzzle in-place.
    :param board: List[List[str]] - 9x9 grid representing the Sudoku board
    """
    def is_valid(num, row, col):
        # Check if num is valid in the current row, column, and 3x3 sub-box
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
            if board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] == num:
                return False
        return True

    def backtrack():
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for num in map(str, range(1, 10)):
                        if is_valid(num, row, col):
                            board[row][col] = num
                            if backtrack():
                                return True
                            board[row][col] = '.'  # Undo the move
                    return False  # No valid number found, backtrack
        return True  # Solved

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

# Topic: Backtracking