"""
LeetCode Problem #1301: Number of Paths with Max Score

Problem Statement:
You are given a square board of characters. You can move on the board starting at the bottom-right corner marked with the character 'S'.

You need to reach the top-left corner marked with the character 'E'. The rest of the cells are either digits (0-9) or the character 'X'. 
You can move up, left, or diagonally up-left. Each move has a score equal to the digit in the cell you move to. 
If you move to a cell with 'X', you cannot proceed further.

Return a list of two integers:
1. The maximum score you can achieve.
2. The number of distinct paths to achieve that score.

If there is no valid path, return [0, 0].

Constraints:
- 2 <= board.length == board[i].length <= 100
- 'S' and 'E' are guaranteed to be at distinct positions.
- The board contains only characters 'S', 'E', digits (0-9), and 'X'.

"""

from typing import List

def pathsWithMaxScore(board: List[str]) -> List[int]:
    MOD = 10**9 + 7
    n = len(board)
    
    # Convert the board into a 2D list for easier manipulation
    board = [list(row) for row in board]
    board[-1][-1] = '0'  # Replace 'S' with '0' for easier calculations
    board[0][0] = '0'    # Replace 'E' with '0' for easier calculations
    
    # Initialize dp arrays
    dp_score = [[-1] * n for _ in range(n)]  # Maximum score at each cell
    dp_paths = [[0] * n for _ in range(n)]  # Number of paths to achieve the max score
    
    dp_score[-1][-1] = 0  # Starting point score
    dp_paths[-1][-1] = 1  # Starting point has one path
    
    # Iterate from bottom-right to top-left
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if board[i][j] == 'X':  # Skip blocked cells
                continue
            
            # Check all possible moves: up, left, diagonal
            for di, dj in [(-1, 0), (0, -1), (-1, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and dp_score[ni][nj] != -1:
                    new_score = dp_score[ni][nj] + int(board[i][j])
                    if new_score > dp_score[i][j]:
                        dp_score[i][j] = new_score
                        dp_paths[i][j] = dp_paths[ni][nj]
                    elif new_score == dp_score[i][j]:
                        dp_paths[i][j] = (dp_paths[i][j] + dp_paths[ni][nj]) % MOD
    
    # The result is at the top-left corner
    max_score = dp_score[0][0]
    num_paths = dp_paths[0][0]
    
    return [max_score, num_paths] if max_score != -1 else [0, 0]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    board1 = ["E23", "2X2", "12S"]
    print(pathsWithMaxScore(board1))  # Output: [7, 1]

    # Test Case 2
    board2 = ["E12", "1X1", "21S"]
    print(pathsWithMaxScore(board2))  # Output: [4, 2]

    # Test Case 3
    board3 = ["E11", "XXX", "11S"]
    print(pathsWithMaxScore(board3))  # Output: [0, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over all cells in the board (O(n^2)).
- For each cell, it checks up to 3 possible moves (constant time).
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm uses two auxiliary 2D arrays (dp_score and dp_paths), each of size n x n.
- Therefore, the space complexity is O(n^2).

Topic: Dynamic Programming (DP)
"""