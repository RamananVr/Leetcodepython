"""
LeetCode Question #130: Surrounded Regions

Problem Statement:
Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are surrounded by `'X'`.

A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. A region is considered surrounded if it is completely surrounded by `'X'`s on all sides (including diagonals).

The `'O'`s on the border of the board, and any `'O'`s connected to them (directly or indirectly), are not considered surrounded and should not be flipped.

Example:
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]
Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]

Constraints:
- `m == board.length`
- `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`.
"""

# Python Solution
from collections import deque

def solve(board):
    """
    Modify the input board in-place to capture all surrounded regions.
    """
    if not board or not board[0]:
        return

    rows, cols = len(board), len(board[0])

    # Helper function to perform DFS/BFS from border 'O's
    def mark_border_connected(row, col):
        queue = deque([(row, col)])
        while queue:
            r, c = queue.popleft()
            if 0 <= r < rows and 0 <= c < cols and board[r][c] == 'O':
                board[r][c] = 'B'  # Mark as border-connected
                # Add neighbors to the queue
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    queue.append((r + dr, c + dc))

    # Step 1: Mark all 'O's connected to the border as 'B'
    for r in range(rows):
        for c in [0, cols - 1]:  # Left and right borders
            if board[r][c] == 'O':
                mark_border_connected(r, c)
    for c in range(cols):
        for r in [0, rows - 1]:  # Top and bottom borders
            if board[r][c] == 'O':
                mark_border_connected(r, c)

    # Step 2: Flip all remaining 'O's to 'X' and 'B's back to 'O'
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'  # Surrounded region
            elif board[r][c] == 'B':
                board[r][c] = 'O'  # Restore border-connected region

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [["X", "X", "X", "X"],
              ["X", "O", "O", "X"],
              ["X", "X", "O", "X"],
              ["X", "O", "X", "X"]]
    solve(board1)
    print(board1)  # Expected: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    # Test Case 2
    board2 = [["X", "X", "X"],
              ["X", "O", "X"],
              ["X", "X", "X"]]
    solve(board2)
    print(board2)  # Expected: [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

    # Test Case 3
    board3 = [["O", "O", "O"],
              ["O", "X", "O"],
              ["O", "O", "O"]]
    solve(board3)
    print(board3)  # Expected: [["O", "O", "O"], ["O", "X", "O"], ["O", "O", "O"]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm visits each cell at most once during the marking phase and flipping phase.
- Therefore, the time complexity is O(m * n), where m is the number of rows and n is the number of columns.

Space Complexity:
- The space complexity is O(m * n) in the worst case due to the queue used in BFS. However, in practice, the space usage is proportional to the number of border-connected 'O's.
- Therefore, the space complexity is O(m * n) in the worst case.

Primary Topic: Matrix, Depth-First Search (DFS), Breadth-First Search (BFS)
"""