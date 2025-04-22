"""
LeetCode Problem #909: Snakes and Ladders

Problem Statement:
You are given an `n x n` integer matrix `board` where the cells are labeled from `1` to `n^2` in a Boustrophedon style 
(i.e., left-to-right, then right-to-left for the next row, and so on). The board contains snakes and ladders:

- A ladder at cell `i` moves you to cell `j` (i < j).
- A snake at cell `i` moves you to cell `j` (i > j).

Each cell's value is `-1` if it does not have a snake or ladder. Otherwise, it contains the destination of the snake or ladder.

You start on square `1` of the board. In each move, you can roll a six-sided die, advancing the number of cells shown on the die. 
You can only move to a square `n^2` or less. If you land on a square with a ladder or snake, you must move to the destination of 
that snake or ladder. Note that you only take a snake or ladder at most once per move.

Return the least number of moves required to reach the square `n^2`. If it is not possible to reach the square, return `-1`.

Constraints:
- `n == board.length == board[i].length`
- `2 <= n <= 20`
- `board[i][j]` is either `-1` or in the range `[1, n^2]`.
"""

from collections import deque

def snakesAndLadders(board):
    def get_coordinates(square):
        """Convert a square number to board coordinates."""
        quot, rem = divmod(square - 1, n)
        row = n - 1 - quot
        col = rem if (n - 1 - row) % 2 == 0 else n - 1 - rem
        return row, col

    n = len(board)
    visited = set()
    queue = deque([(1, 0)])  # (current square, moves)

    while queue:
        square, moves = queue.popleft()
        if square == n * n:
            return moves

        for dice_roll in range(1, 7):
            next_square = square + dice_roll
            if next_square > n * n:
                break

            row, col = get_coordinates(next_square)
            if board[row][col] != -1:
                next_square = board[row][col]

            if next_square not in visited:
                visited.add(next_square)
                queue.append((next_square, moves + 1))

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1]
    ]
    print(snakesAndLadders(board1))  # Output: 4

    # Test Case 2
    board2 = [
        [-1, -1],
        [-1, 3]
    ]
    print(snakesAndLadders(board2))  # Output: 1

    # Test Case 3
    board3 = [
        [-1, -1, -1],
        [-1, 9, 8],
        [-1, 8, 9]
    ]
    print(snakesAndLadders(board3))  # Output: 1

"""
Time Complexity:
- The board has `n^2` cells. In the worst case, we visit each cell once, and for each cell, we consider up to 6 possible moves 
  (dice rolls). Thus, the time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n^2) due to the `visited` set and the queue used for BFS.

Topic: Breadth-First Search (BFS), Matrix
"""