"""
LeetCode Question #36: Valid Sudoku

Problem Statement:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are represented by the character '.'.

Constraints:
- The board is a 2D array of size 9x9.
- Each element of the board is either a digit ('1'-'9') or '.'.

Example:
Input: 
board = 
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Explanation:
The board is valid according to the rules of Sudoku.

"""

def isValidSudoku(board):
    """
    Function to determine if a given 9x9 Sudoku board is valid.
    :param board: List[List[str]] - 2D list representing the Sudoku board
    :return: bool - True if the board is valid, False otherwise
    """
    def is_valid_group(group):
        """Helper function to check if a group (row, column, or sub-box) is valid."""
        elements = [x for x in group if x != '.']
        return len(elements) == len(set(elements))
    
    # Check rows
    for row in board:
        if not is_valid_group(row):
            return False
    
    # Check columns
    for col in zip(*board):
        if not is_valid_group(col):
            return False
    
    # Check 3x3 sub-boxes
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sub_box = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_group(sub_box):
                return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid Sudoku
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board1))  # Output: True

    # Test Case 2: Invalid Sudoku (duplicate in row)
    board2 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"]  # Duplicate '5' in the last row
    ]
    print(isValidSudoku(board2))  # Output: False

    # Test Case 3: Invalid Sudoku (duplicate in column)
    board3 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        ["5",".",".","4","1","9",".",".","5"],  # Duplicate '5' in the first column
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(isValidSudoku(board3))  # Output: False

    # Test Case 4: Invalid Sudoku (duplicate in sub-box)
    board4 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    board4[0][0] = "9"  # Introduce duplicate '9' in the top-left sub-box
    print(isValidSudoku(board4))  # Output: False

"""
Time and Space Complexity Analysis:
- Time Complexity: O(9^2) = O(81), as we iterate through all rows, columns, and sub-boxes (constant size).
- Space Complexity: O(1), as we use a fixed amount of extra space for validation.

Topic: Arrays
"""