"""
LeetCode Question #782: Transform to Chessboard

Problem Statement:
An `n x n` binary grid `board` is said to be a chessboard if:
1. Each row of the board is a binary string that alternates between 0 and 1.
2. Each column of the board is a binary string that alternates between 0 and 1.
3. No two rows are the same, and no two columns are the same.

Given an `n x n` binary grid `board`, return the minimum number of moves to transform the board into a chessboard. If the task is impossible, return -1.

In one move, you can swap any two rows with each other, or any two columns with each other.

Constraints:
- `n == board.length`
- `n == board[i].length`
- `2 <= n <= 30`
- `board[i][j]` is either `0` or `1`.

Example:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation: Swap the first and second row, and the first and second column.

"""

from typing import List

class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        
        # Check if the board can be transformed into a chessboard
        for i in range(n):
            for j in range(n):
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0:
                    return -1
        
        # Count row and column patterns
        row_count = sum(board[0])
        col_count = sum(board[i][0] for i in range(n))
        row_swap = sum(board[i][0] == i % 2 for i in range(n))
        col_swap = sum(board[0][i] == i % 2 for i in range(n))
        
        # Check if the number of 1s in rows and columns is valid
        if not (n // 2 <= row_count <= (n + 1) // 2) or not (n // 2 <= col_count <= (n + 1) // 2):
            return -1
        
        # Calculate the minimum swaps needed
        if n % 2 == 0:
            row_swap = min(row_swap, n - row_swap)
            col_swap = min(col_swap, n - col_swap)
        else:
            if row_swap % 2 == 1:
                row_swap = n - row_swap
            if col_swap % 2 == 1:
                col_swap = n - col_swap
        
        return (row_swap + col_swap) // 2

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    board1 = [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]
    print(solution.movesToChessboard(board1))  # Output: 2

    # Test Case 2
    board2 = [[1, 0], [0, 1]]
    print(solution.movesToChessboard(board2))  # Output: 0

    # Test Case 3
    board3 = [[1, 1, 0], [0, 0, 1], [1, 1, 0]]
    print(solution.movesToChessboard(board3))  # Output: -1

    # Test Case 4
    board4 = [[0, 1], [1, 0]]
    print(solution.movesToChessboard(board4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over the board to check the validity of the transformation (O(n^2)).
- It then calculates the row and column counts and swaps (O(n)).
- Overall, the time complexity is O(n^2).

Space Complexity:
- The algorithm uses a constant amount of extra space (O(1)).

Primary Topic: Arrays, Matrix
"""